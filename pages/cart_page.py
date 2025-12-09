from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # --- Localizadores ---
    TITLE = (By.XPATH, "//span[@class='title' and text()='Your Cart']")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # --- Métodos ---
    def is_loaded(self) -> bool:
        return self._get_element_text(self.TITLE) == "Your Cart"

    def get_item_names(self) -> list[str]:
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [e.text for e in elements]

    def click_checkout(self):
        self._find_element(self.CHECKOUT_BUTTON).click()
