<div align="center">
  <img width="250" height="250" alt="avatar" src="https://github.com/user-attachments/assets/27c5e884-bb12-4847-b2a5-31ac2ba5d5d8" />
  <h3 align="center">
    Adicione <b>DJ Pinhas<b/> no seu servidor <a href="https://shre.ink/djpinhas-musicbot">AQUI!</a>
  <h3/>
</div>

# 🤖 DJ PINHAS

> Um bot de música para servidores no Discord, desenvolvido com Python. Toca músicas buscadas diretamente do YouTube com um sistema de busca e fila.

## 🚀 Tecnologias Utilizadas

* **[discord.py](https://discordpy.readthedocs.io/)** - A biblioteca para interagir com a API do Discord.
* **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Para buscar e extrair os dados de áudio do YouTube.
* **[Flask](https://flask.palletsprojects.com/)** - Usado para criar um pequeno servidor web que mantém o bot ativo em plataformas de hospedagem.

## 🛠️ Como Configurar e Rodar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/pinheirosdev/pinhas-musicbot.git
cd pinhas-musicbot
```

### 2. Crie um Bot no Discord

* Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).
* Crie uma nova aplicação e adicione um bot.
* Copie o Token do seu bot.
* Ative a permissão "Intenção do conteúdo da mensagem" na seção "Intenções de Gateway Privilegiadas".

### 3. Instale as Dependências

É recomendado usar um ambiente virtual (`venv`) para isolar as dependências do projeto.
```bash
# Crie o ambiente virutal na pasta raíz do projeto
python -m venv venv

# Ative o venv
venv\Scripts\activate

# Instale as bibliotecas necessárias
pip install discord.py yt-dlp PyNaCl
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione seu token

**.env**
```
TOKEN="seu_token_aqui"
```

### 5. Execute o Bot

Com tudo configurado, inicie o bot com o seguinte comando:

```bash
python code/main.py
```
Será exibida uma mensagem no terminal confirmando que o bot está online caso der certo.

## 🎮 Comandos do Bot

Use os seguintes comandos em um canal de texto do seu servidor do Discord:

`!pinhas <nome da música>`
<br/>
> Busca a música no YouTube e reproduz na call, se já houver outra música tocando entra na fila.

`!fila`
<br/>
> Mostra a lista de músicas que estão na fila de reprodução.

`!prox`
<br/>
> Pula a música que está tocando e passa para a próxima da fila.

`!desc`
<br/>
> Desconecta o bot da call e limpa a fila de músicas.

### Bot em Execução
* Executando o código
<p align="left">
  <img width="805" height="97" alt="image" src="https://github.com/user-attachments/assets/b7a89bdf-761d-40cf-99c1-cd3ce5d75b55" />
</p>

<br/>

* Buscando a música
<p align="left">
  <img width="805" height="304" alt="image" src="https://github.com/user-attachments/assets/4030ef7b-6a8c-4be9-82b5-487c6f69e668" />
  <img width="805" height="225" alt="image" src="https://github.com/user-attachments/assets/5677c2f1-32b6-4f0a-9abf-a63d398c3197" />
</p>

<br/>

* Adicionando duas músicas, pulando para a próxima e exibindo a fila
<p align="left">
  <img width="805" height="454" alt="image" src="https://github.com/user-attachments/assets/d1c7fbc5-1bd2-4967-a214-817a6de09390" />
  <img width="805" height="782" alt="image" src="https://github.com/user-attachments/assets/6c7e89bc-509d-444a-8dcc-47dc4f159f4d" />
</p>

<br/>

* Desconectando o bot
<p align="left">
  <img width="805" height="74" alt="image" src="https://github.com/user-attachments/assets/80762614-426c-48cf-90b0-ffc77734b0f0" />
  <img width="694" height="134" alt="image" src="https://github.com/user-attachments/assets/7f0476a3-34d1-4871-96ae-06e3c7def38f" />
</p>

### 👨‍💻 Desenvolvedores

<table>
  <tr>
    <td>
      <a href="https://github.com/pinheirosdev">
        <img src="https://avatars.githubusercontent.com/u/124714182?v=4" width="100px;" alt="Lucas Pinheiro"/><br>
        <sub>
          <b>Lucas Pinheiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

### ☎️ Contato

Se você quiser entrar em contato comigo, pode me encontrar no [Gmail](mailto:cttpinheiros.dev@gmail.com).

### 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](README.md)<br>
