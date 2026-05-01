import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_login_com_sucesso(driver, credenciais):
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login(credenciais["usuario"], credenciais["senha"])

    inventario = InventoryPage(driver)
    assert inventario.obter_titulo() == "Products"


def test_login_invalido_exibe_erro(driver):
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("usuario_errado", "senha_errada")

    assert "Epic sadface" in login.obter_erro()


def test_fluxo_completo_de_compra(driver, credenciais):

    login = LoginPage(driver)
    login.abrir()
    login.fazer_login(credenciais["usuario"], credenciais["senha"])

    inventario = InventoryPage(driver)
    inventario.adicionar_produto_ao_carrinho()
    inventario.ir_para_carrinho()

    carrinho = CartPage(driver)
    assert len(carrinho.obter_itens()) == 1
    carrinho.ir_para_checkout()

    checkout = CheckoutPage(driver)
    checkout.preencher_dados("Estudante", "QA", "60000-000")
    checkout.finalizar_compra()

    assert checkout.obter_mensagem_sucesso() == "Obrigado, pedido realizado com sucesso!"