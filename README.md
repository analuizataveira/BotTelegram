
# Telegram Notification Bot

Este projeto é um **bot de notificações** no Telegram, criado para enviar mensagens automatizadas para um chat ou grupo do Telegram usando o **Python** e a biblioteca `python-telegram-bot`. Além disso, ele é empacotado e gerido com o **Poetry** e pode ser compilado em um executável com **PyInstaller**.

## Funcionalidades

- Envio de mensagens para um grupo ou chat do Telegram.
- Utiliza variáveis de ambiente para armazenar o token do bot e o ID do chat.
- Possui build automatizado com **Poetry** e geração de executável com **PyInstaller**.

## Tecnologias Usadas

- **Python 3.11 ou superior**
- **Poetry**: Gerenciamento de dependências e build
- **python-telegram-bot**: Para interagir com a API do Telegram
- **PyInstaller**: Para gerar um executável do bot

## Requisitos

- **Python 3.11 ou superior** (recomenda-se usar uma versão < 3.14 para compatibilidade com PyInstaller)
- **Poetry**: Para gerenciamento de dependências
- **Bot do Telegram**: Crie seu bot [aqui](https://core.telegram.org/bots#botfather) e obtenha seu `TELEGRAM_BOT_TOKEN`.

## Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <diretorio_do_repositorio>
```

### 2. Instale as dependências

Certifique-se de ter o Poetry instalado. Se não, instale o Poetry com o comando:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Em seguida, instale as dependências do projeto:

```bash
poetry install
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

- **TELEGRAM_BOT_TOKEN**: Token gerado ao criar o bot no BotFather.
- **TELEGRAM_CHAT_ID**: ID do chat ou grupo onde as mensagens serão enviadas. Você pode obter o chat ID enviando uma mensagem para o bot e usando a API do Telegram para recuperá-lo.

### 4. Executando o bot

Para rodar o bot e enviar uma notificação, use o seguinte comando:

```bash
poetry run python main.py
```

### 5. Criando o Executável

Se preferir, você pode criar um executável do bot usando o **PyInstaller**.

Primeiro, instale o **PyInstaller**:

```bash
poetry add pyinstaller --dev
```

Para gerar o executável, use o seguinte comando:

```bash
poetry run pyinstaller --onefile main.py
```

Isso criará um executável na pasta `dist/` que pode ser rodado sem a necessidade de um ambiente Python.

## Como Contribuir

1. Faça um **fork** do projeto.
2. Crie uma **branch** para a sua funcionalidade (`git checkout -b minha-feature`).
3. Faça o **commit** das suas alterações (`git commit -am 'Adicionando nova funcionalidade'`).
4. Envie para o **branch** do seu repositório (`git push origin minha-feature`).
5. Abra um **pull request**.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
