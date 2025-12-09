from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver_setup():
    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.set_capability("acceptInsecureCerts", True)
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(5) 
    yield driver
    
    driver.quit()

@pytest.mark.front
def test_login_exitoso(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    assert products_page.is_loaded(), "La página de productos no se cargó correctamente"

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

@pytest.mark.front
def test_login_negativo(driver_setup, username, password, expected_error):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login(username, password)

    error_text = login_page.get_error_message()
    assert expected_error in error_text
    
@pytest.mark.front
def test_login_usuario_bloqueado(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_text