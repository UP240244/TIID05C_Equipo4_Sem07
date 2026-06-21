import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@pytest.fixture(scope="function")
def driver():
    """Configura el navegador Brave/Chrome en segundo plano."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    posibles_rutas = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"C:\Users\\" + os.getlogin() + r"\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"C:\Users\\" + os.getlogin() + r"\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]
    
    binario_encontrado = None
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            binario_encontrado = ruta
            break
            
    if binario_encontrado:
        chrome_options.binary_location = binario_encontrado

    if binario_encontrado and "BraveSoftware" in binario_encontrado:
        manager = ChromeDriverManager(chrome_type=ChromeType.BRAVE)
    else:
        manager = ChromeDriverManager()

    driver_path = manager.install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    driver.quit()