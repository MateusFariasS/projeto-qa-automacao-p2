from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

TIMEOUT = 20
NAV_TIMEOUT = 5

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)
        self.short_wait = WebDriverWait(driver, NAV_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(btn).click().perform()

    def type(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def wait_for_url(self, fragment):
        self.wait.until(EC.url_contains(fragment))
