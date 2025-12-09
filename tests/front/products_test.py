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
def test_agregar_producto_al_carrito_actualiza_badge(driver_setup):
    """
    Agregar la backpack al carrito y validar el badge.
    """
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert products_page.get_cart_badge_count() == 0

    products_page.add_backpack_to_cart()
    assert products_page.get_cart_badge_count() == 1

@pytest.mark.front
def test_carrito_vacio_no_muestra_badge(driver_setup):
    """
    Entrar por primera vez no debería haber nada en el carrito.
    """
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert products_page.get_cart_badge_count() == 0