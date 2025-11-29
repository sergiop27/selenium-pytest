from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:
    URL = "https://www.saucedemo.com/"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def go_to_url(self, url: str):
        self.driver.get(url)

    def quit_driver(self):
        self.driver.quit()

    def _find_element(self, locator: tuple[str, str]):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def _get_element_text(self, locator: tuple[str, str]) -> str:
        element = self._find_element(locator)
        return element.text