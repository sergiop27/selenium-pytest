from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # --- Localizadores Step One ---
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_TITLE = (By.CLASS_NAME, "complete-header")

    # --- Métodos ---
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self._find_element(self.FIRST_NAME).clear()
        self._find_element(self.LAST_NAME).clear()
        self._find_element(self.POSTAL_CODE).clear()

        self._find_element(self.FIRST_NAME).send_keys(first_name)
        self._find_element(self.LAST_NAME).send_keys(last_name)
        self._find_element(self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self):
        self._find_element(self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        self._find_element(self.FINISH_BUTTON).click()

    def get_error_message(self) -> str:
        return self._get_element_text(self.ERROR_MESSAGE)

    def get_success_message(self) -> str:
        return self._get_element_text(self.COMPLETE_TITLE)