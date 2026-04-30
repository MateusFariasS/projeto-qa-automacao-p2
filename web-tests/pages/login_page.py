from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir(self):
        self.driver.get(self.URL)

    def fazer_login(self, usuario, senha):
        self.type(self.USERNAME, usuario)
        self.type(self.PASSWORD, senha)
        self.click(self.BTN_LOGIN)

    def obter_erro(self):
        return self.find(self.ERROR_MSG).text