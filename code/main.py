import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# config do token, das intenções do bot e do prefixo de comando
TOKEN = os.getenv("TOKEN") 
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
botCmd = commands.Bot(command_prefix="!", intents=intents)

# guarda as filas de cada server em um dicionário, permitindo funcionar em vários servidores sem misturar filas
filas = {}

# func p gerenciar fila
async def proxima_msc(bot):
    # func chamada p tocar próxima msc
    if bot.guild.id in filas and filas[bot.guild.id]:
        # busca primeira msc da fila
        proxMsc = filas[bot.guild.id].pop(0)
        urlMsc = proxMsc['url']
        msc = proxMsc['titulo']

        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        src = await discord.FFmpegOpusAudio.from_probe(urlMsc, **FFMPEG_OPTS)
        
        # cria um loop, tocando a próxima msc e logo depois programa para a função ser chamada novamente quando a msc atual terminar
        bot.voice_client.play(src, after=lambda _: botCmd.loop.create_task(proxima_msc(bot)))
        
        await bot.send(f"▶️ Tocando a seguir: **{msc}**")

# evento e comando do bot
@botCmd.event
async def on_ready():
    print(f'{botCmd.user.name} está online!')

@botCmd.command(name='pinhas')
async def tocar(bot, *, query: str):
    if bot.author.voice is None:
        await bot.send("Você precisa estar em uma call!")
        return
    
    call = bot.author.voice.channel
    if bot.voice_client is None:
        await call.connect()
    else:
        await bot.voice_client.move_to(call)

    YDL_OPTS = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'default_search': 'auto'
    }

    try:
        await bot.send(f"🔍 DJ Pinhas está procurando por **`{query}`** no YouTube...")
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        
        urlMsc = info['url']
        nomeMsc = info['title']
        msc = {'url': urlMsc, 'titulo': nomeMsc}

        if bot.guild.id not in filas:
            filas[bot.guild.id] = []
        
        if bot.voice_client.is_playing() or bot.voice_client.is_paused():
            filas[bot.guild.id].append(msc)
            await bot.send(f"✅ DJ Pinhas adicionou **{nomeMsc}** à fila (YouTube)")
        else:
            FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            src = await discord.FFmpegOpusAudio.from_probe(urlMsc, **FFMPEG_OPTS)
            # quando termina de tocar a msc(src) executa a func proxima_msc
            bot.voice_client.play(src, after=lambda _: botCmd.loop.create_task(proxima_msc(bot)))
            await bot.send(f"▶️ DJ Pinhas está tocando agora (YouTube): **{nomeMsc}**")

    except Exception as e:
        await bot.send("Não consegui encontrar no YouTube, vou buscar no SoundCloud🤨🤨🤨")
        try:
            with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
                # muda a busca para o SoundCloud
                info = ydl.extract_info(f"scsearch:{query}", download=False)['entries'][0]
            
            url_audio = info['url']
            titulo_video = info['title']
            musica = {'url': url_audio, 'titulo': titulo_video}

            if bot.guild.id not in filas:
                filas[bot.guild.id] = []
            
            if bot.voice_client.is_playing() or bot.voice_client.is_paused():
                filas[bot.guild.id].append(musica)
                await bot.send(f"✅ DJ Pinhas adicionou **{nomeMsc}** à fila (SoundCloud)")
            else:
                FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                source = await discord.FFmpegOpusAudio.from_probe(url_audio, **FFMPEG_OPTS)
                bot.voice_client.play(source, after=lambda _: botCmd.loop.create_task(proxima_msc(bot)))
                await bot.send(f"▶️ DJ Pinhas está tocando agora agora (SoundCloud): **{titulo_video}**")

        except Exception as e_sc:
            await bot.send(f"Também não consegui encontrar **`{query}`** no SoundCloud😔😔😭😭😭")
            print(f"Erro ao buscar no YouTube: {e}")
            print(f"Erro ao buscar no SoundCloud: {e_sc}")

@botCmd.command(name='prox')
async def pular(bot):
    if bot.voice_client and bot.voice_client.is_playing():
        bot.voice_client.stop() # quando a msc atual é parada aciona a func after, chamando a func proxima_msc, pulando a msc
        await bot.send("DJ Pinhas pulou a música! ⏭️")
    else:
        await bot.send("DJ Pinhas não está tocando nenhuma música no momento.")

@botCmd.command(name='fila')
async def fila(bot):
    if bot.guild.id in filas and filas[bot.guild.id]:
        lista = "```🎵 Fila de Músicas do DJ Pinhas 🎵\n\n"
        for i, msc in enumerate(filas[bot.guild.id]):
            lista += f"{i + 1}. {msc['titulo']}\n"
        lista += "```"
        await bot.send(lista)
    else:
        await bot.send("A fila está vazia! Use `!pinhas` para adicionar músicas.")
        
@botCmd.command(name='desc')
async def sair(bot):
    # limpa a fila do server antes de sair
    if bot.guild.id in filas:
        filas[bot.guild.id] = []

    if bot.voice_client:
        await bot.voice_client.disconnect()
        await bot.send("Até mais! DJ Pinhas limpou a fila de músicas.")
    else:
        await bot.send("DJ Pìnhas não está em um canal de voz.")

botCmd.run(TOKEN)