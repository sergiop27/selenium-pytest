from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest
    
@pytest.mark.front
def test_checkout_exitoso(driver_setup):
    """
    Flujo positivo:
    - Login - Agregar producto - Ir al carrito - Checkout con datos válidos - Validar pantalla de éxito
    """
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    items = cart_page.get_item_names()
    assert "Sauce Labs Backpack" in items

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("Sergio", "Pace", "1000")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    success_message = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_message

@pytest.mark.front
def test_checkout_sin_nombre_muestra_error(driver_setup):
    """
    Caso negativo de checkout: - No se completa el nombre - Se valida el mensaje de error requerido
    """
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("", "Pace", "1000")
    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()
    assert "First Name is required" in error_message