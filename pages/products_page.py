from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    # --- Localizadores ---
    TITLE = (By.XPATH, "//span[@class='title' and text()='Products']")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # --- Métodos ---
    def is_loaded(self) -> bool:
        """
        Verificar que la página de productos esté cargada.
        """
        title_text = self._get_element_text(self.TITLE)
        return title_text == "Products"

    def add_backpack_to_cart(self):
        """
        Agregar BackPack al carrito.
        """
        self._find_element(self.BACKPACK_ADD_BUTTON).click()

    def go_to_cart(self):
        """
        Hacer click en el icono del carrito para navegar a la página del carrito.
        """
        self._find_element(self.CART_ICON).click()

    def get_cart_badge_count(self) -> int:
        """
        Devuelve el número que aparece en el carrito.
        Si no hay nada, interpreta que el carrito está vacío.
        """
        elements = self.driver.find_elements(*self.CART_BADGE)
        if not elements:
            return 0
        return int(elements[0].text)

    def get_all_product_names(self) -> list[str]:
        """
        Devuelve la lista de nombres de productos visibles.
        """
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [e.text for e in elements]