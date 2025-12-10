from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import datetime
import pytest
import os

@pytest.fixture(scope="function")
def driver_setup(request):
    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.add_argument("--disable-infobars")
    edge_options.set_capability("acceptInsecureCerts", True)

    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(5)

    yield driver

    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    test_name = request.node.name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    try:
        driver.save_screenshot(filepath)
    except Exception:
        pass

    driver.quit()