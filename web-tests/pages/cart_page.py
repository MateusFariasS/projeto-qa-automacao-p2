from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class CartPage(BasePage):
    ITEM_NO_CARRINHO = (By.CLASS_NAME, "cart_item")
    BTN_CHECKOUT = (By.ID, "checkout")

    def obter_itens(self):
        self.find(self.ITEM_NO_CARRINHO)
        return self.driver.find_elements(*self.ITEM_NO_CARRINHO)

    def ir_para_checkout(self):
        self.click(self.BTN_CHECKOUT)
        try:
            self.short_wait.until(EC.url_contains("checkout-step-one"))
        except TimeoutException:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            self.wait.until(EC.url_contains("checkout-step-one"))
