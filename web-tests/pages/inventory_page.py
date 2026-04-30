from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITULO = (By.CLASS_NAME, "title")
    BTN_ADD_PRODUTO = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    ICONE_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")

    def obter_titulo(self):
        return self.find(self.TITULO).text

    def adicionar_produto_ao_carrinho(self):
        self.click(self.BTN_ADD_PRODUTO)

    def ir_para_carrinho(self):
        self.click(self.ICONE_CARRINHO)