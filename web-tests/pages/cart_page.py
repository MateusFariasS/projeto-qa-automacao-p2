from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    ITEM_NO_CARRINHO = (By.CLASS_NAME, "cart_item")
    BTN_CHECKOUT = (By.ID, "checkout")

    def obter_itens(self):
        self.find(self.ITEM_NO_CARRINHO)
        return self.driver.find_elements(*self.ITEM_NO_CARRINHO)

    def ir_para_checkout(self):
        self.click(self.BTN_CHECKOUT)
        self.wait_for_url("checkout-step-one.html")