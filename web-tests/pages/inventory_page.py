from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITULO = (By.CLASS_NAME, "title")
    BTN_ADD_PRODUTO = (By.ID, "add-to-cart-sauce-labs-backpack")
    ICONE_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")
    BADGE_CARRINHO = (By.CLASS_NAME, "shopping_cart_badge")

    def obter_titulo(self):
        return self.find(self.TITULO).text

    def adicionar_produto_ao_carrinho(self):
        self.click(self.BTN_ADD_PRODUTO)
        self.wait.until(EC.presence_of_element_located(self.BADGE_CARRINHO))

    def ir_para_carrinho(self):
        self.click(self.ICONE_CARRINHO)
        self.wait_for_url("cart.html")