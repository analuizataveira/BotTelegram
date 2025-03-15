import string
import os
import pytest
from dotenv import load_dotenv # Biblioteca para conversão de token  
from telegram import Bot

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de token 
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token do bot
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ID do chat/grupo

# Teste para verificar se os tokens estão definidos 
def test_tokens():
    assert TELEGRAM_BOT_TOKEN is not None, "TELEGRAM_BOT_TOKEN não está definido"
    assert CHAT_ID is not None, "CHAT_ID não está definido"

# Teste para verificar se os tokens são válidos
def test_valid_tokens():
    assert TELEGRAM_BOT_TOKEN[0] in string.digits, "TELEGRAM_BOT_TOKEN inválido" 
    assert CHAT_ID.startswith("-"), "CHAT_ID inválido"

# Teste para verificar exatamente o Token 
def test_my_token():
    assert TELEGRAM_BOT_TOKEN == "8042266734:AAHFtPs83ZwuOJfbSSheAMePHWvNP4OnPug", "Token inválido"
    assert CHAT_ID == "-4608791451", "CHAT_ID inválido"

