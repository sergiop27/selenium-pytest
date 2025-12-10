from data.login_data_reader import load_login_data
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
import pytest

login_data = load_login_data()

@pytest.mark.front
def test_login_exitoso(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    valid_user = login_data["valid_user"]
    login_page.login(valid_user["username"], valid_user["password"])
    
    products_page = ProductsPage(driver)
    assert products_page.is_loaded(), "La página de productos no se cargó correctamente"

@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (case["username"], case["password"], case["error"])
        for case in login_data["invalid_users"]
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
    locked = login_data["locked_user"]
    login_page.login(locked["username"], locked["password"])

    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_text