import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token do bot
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ID do chat/grupo

# Verifica se as variáveis de ambiente estão definidas
if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
    print("Erro: TELEGRAM_BOT_TOKEN ou CHAT_ID não estão definidos.")
    exit(1)

async def send_notification(message):
    """
    Envia uma notificação para o chat especificado.
    
    Args:
        message (str): A mensagem a ser enviada.
    """
    try:
        # Cria uma instância do bot com o token fornecido
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        # Envia a mensagem para o chat especificado
        await bot.send_message(chat_id=CHAT_ID, text=message)  # Removido timeout
        print("Notificação enviada com sucesso!")  # Confirmação de envio
    except TelegramError as e:
        # Captura e imprime erros ao enviar a notificação
        print(f"Erro ao enviar notificação: {e}")

async def main():
    """
    Função principal que executa o envio de uma notificação de teste.
    """
    # Mensagem de exemplo
    message = "Olá, este é um teste de notificação do bot!"
    await send_notification(message)  # Chama a função para enviar a notificação

if __name__ == "__main__":
    asyncio.run(main())