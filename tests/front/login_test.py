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

def test_login_exitoso(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    titulo_productos = login_page._get_element_text((By.XPATH, "//span[text()='Products']"))
    assert titulo_productos == "Products"

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("", "", "Username is required"),
        ("usuario_invalido", "secret_sauce", "Epic sadface: Username and password do not match"),
        ("standard_user", "clave_invalida", "Epic sadface: Username and password do not match"),
    ],
)

def test_login_negativo(driver_setup, username, password, expected_error):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login(username, password)

    error_text = login_page.get_error_message()
    assert expected_error in error_text
    
def test_login_usuario_bloqueado(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_text