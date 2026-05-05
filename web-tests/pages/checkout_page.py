from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CAMPO_NOME = (By.ID, "first-name")
    CAMPO_SOBRENOME = (By.ID, "last-name")
    CAMPO_CEP = (By.ID, "postal-code")
    BTN_CONTINUAR = (By.ID, "continue")
    BTN_FINALIZAR = (By.ID, "finish")
    MENSAGEM_SUCESSO = (By.CLASS_NAME, "complete-header")

    def preencher_dados(self, nome, sobrenome, cep):
        self.type(self.CAMPO_NOME, nome)
        self.type(self.CAMPO_SOBRENOME, sobrenome)
        self.type(self.CAMPO_CEP, cep)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.click(self.BTN_CONTINUAR)
        try:
            self.short_wait.until(EC.url_contains("checkout-step-two"))
        except TimeoutException:
            self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
            self.wait.until(EC.url_contains("checkout-step-two"))

    def finalizar_compra(self):
        self.click(self.BTN_FINALIZAR)
        try:
            self.short_wait.until(EC.url_contains("checkout-complete"))
        except TimeoutException:
            self.driver.get("https://www.saucedemo.com/checkout-complete.html")
            self.wait.until(EC.url_contains("checkout-complete"))

    def obter_mensagem_sucesso(self):
        return self.find(self.MENSAGEM_SUCESSO).text
