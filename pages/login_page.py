from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- Localizadores ---
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """
        Ejecuta la secuencia completa de inicio de sesión.
        """
        self.go_to_url(self.URL)

        # Escribir nombre de usuario y clave
        self._find_element(self.USERNAME_FIELD).send_keys(username)
        self._find_element(self.PASSWORD_FIELD).send_keys(password)
        
        # Hacer clic en el botón de login
        self._find_element(self.LOGIN_BUTTON).click()
