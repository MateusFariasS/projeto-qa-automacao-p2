from selenium.webdriver.common.by import By
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
        self.click(self.BTN_CONTINUAR)

    def finalizar_compra(self):
        self.click(self.BTN_FINALIZAR)

    def obter_mensagem_sucesso(self):
        return self.find(self.MENSAGEM_SUCESSO).text