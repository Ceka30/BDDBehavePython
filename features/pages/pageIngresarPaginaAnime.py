from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.webBasePage.webBasePage import webBasePage


class pageIngresarPaginaAnime(webBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sendKeys(self, etiqueta, atributo, valor, texto, index):
        driver = self.driver
        try:
            xpath = "(//"+etiqueta+"[@"+atributo+"='"+valor+"'])["+index+"]"
            element = driver.find_element(By.XPATH, xpath)
            super().waitUntilElementIsVisible(xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            element.clear()
            element.send_keys(texto)
        except Exception as ex:
            print(str(ex))
            raise

    def clickButton(self, etiqueta, atributo, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[@" + atributo + "='" + valor + "'])[" + index + "]"
            element = driver.find_element(By.XPATH, xpath)
            super().waitUntilElementIsVisible(xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))))
        except Exception as ex:
            print(str(ex))
            raise

    def clickButtonTexto(self, etiqueta, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[contains(text(),'" + valor + "')])[" + index + "]"
            element = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            super().waitUntilElementIsVisible(xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            element.click()
        except Exception as ex:
            print(str(ex))
            raise

    def getTextforClass(self, etiqueta, atributo, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[@" + atributo + "='" + valor + "'])[" + index + "]"
            element = driver.find_element(By.XPATH, xpath)
            super().waitUntilElementIsVisible(xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            return element.text
        except Exception as ex:
            print(str(ex))
            raise

    def getTextforText(self, etiqueta, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[contains(text(),'"+valor+"')])[" + index + "]"
            print(xpath)
            element = driver.find_element(By.XPATH, xpath)
            super().waitUntilElementIsVisible(xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            return element.text
        except Exception as ex:
            print(str(ex))
            raise