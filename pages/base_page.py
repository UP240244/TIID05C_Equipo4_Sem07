from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Abstracción de interacciones elementales sobre el DOM gobernadas por WebDriverWait.
    """
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        """Espera a que el elemento sea visible en el DOM."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Espera a que el elemento sea cliqueable antes de interactuar."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text):
        """Limpia el cuadro de texto y escribe la cadena indicada."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)