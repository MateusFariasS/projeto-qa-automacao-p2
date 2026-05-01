import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()


@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=options)
    yield navegador
    navegador.quit()


@pytest.fixture
def credenciais():
    return {
        "usuario": os.getenv("LOGIN_USER"),
        "senha": os.getenv("LOGIN_PASSWORD"),
    }