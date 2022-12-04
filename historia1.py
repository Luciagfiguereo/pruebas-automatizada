import HtmlTestRunner
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginUsuario_lucia(unittest.TestCase):

    def setUp(self):
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        #chromedriver_autoinstaller.install()
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=5)

    def test_login_page_correct01(self):
        usuario = self.driver.find_element(By.NAME, "username").send_keys("Admin")
        password = self.driver.find_element(By.NAME, 'password').send_keys("admin123")
        login = self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        msj = self.driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb")
        self.assertTrue(msj)

        print("Prueba Correcta - Historia 01 | Caso de prueba 01 | Validar Login Usuario Correcto")



    def test_login_page_incorrect01(self):
        usuario = self.driver.find_element(By.NAME, 'username').send_keys("Admin1")
        password = self.driver.find_element(By.NAME, 'password').send_keys("admin12345")
        login = self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        #welcome = self.driver.find_element(By.ID, 'welcome').click()
        msj_error = self.driver.find_element(By.CLASS_NAME, "oxd-alert-content-text")
        #msj_error = self.driver.find_element(By.XPATH, "//[contains(text(), 'Invalid credentials')]”")
        self.assertTrue(msj_error)
        
        print("Prueba Correcta - Historia 01 | Caso de prueba 02 | Validar Login Usuario Incorrecto")




    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    print("prueba exitosa")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Numbers Tech\\Desktop\Python\\pruebas-automatizada\\Reportes'))
    #unittest.main()


