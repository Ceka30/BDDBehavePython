
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import *

class webBasePage:

    def __init__(self, driver):
        self.driver = driver

    def navegar(self, URL):
        self.driver.maximize_window()
        self.driver.get(URL)

    def isDisplayed(self, element):
        try:
            return element.is_displayed()
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception: "+element)
            return False
            raise

    def isEnabled(self, element):
        try:
            return element.is_enabled()
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception: "+element)
            return False
            raise

    def waitUntilElementIsVisible(self, xpath):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath))))
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as ex:
            print("No se encuentra el elemento despues de 30 segundos: "+str(ex))
            raise