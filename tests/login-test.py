from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) 
    yield driver
    
    driver.quit()

def test_login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")

    titulo_productos = login_page._get_element_text(By.XPATH, "//span[text()='Products']")
        
    assert titulo_productos == "Products", "El título de la página no es 'Products'. Login fallido."
    print("Login exitoso - La validación de título correcta")