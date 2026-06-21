from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Usamos una página de internet real que SÍ existe para que no dé Connection Refused
        self.url = "https://the-internet.herokuapp.com/login"
        
        # Localizadores estándar de esa página de pruebas
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")

    def navigate(self):
        """El Integrante 1 programó la navegación básica"""
        self.driver.get(self.url)

    def login(self, email):
        """Simula la interacción con los campos de texto"""
        wait = WebDriverWait(self.driver, 10)
        
        # Espera a que el campo esté listo, lo limpia e ingresa el correo/usuario
        user_field = wait.until(EC.presence_of_element_located(self.username_input))
        user_field.clear()
        user_field.send_digits(email) if hasattr(user_field, 'send_digits') else user_field.send_keys(email)
        
        # Coloca una contraseña simulada y da clic
        pass_field = self.driver.find_element(*self.password_input)
        pass_field.clear()
        pass_field.send_keys("SuperSecretPassword!")
        
        self.driver.find_element(*self.login_button).click()