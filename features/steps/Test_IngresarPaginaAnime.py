import time
#Imports
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from features.pages.pageIngresarPaginaAnime import pageIngresarPaginaAnime

@Given(u'Abrir el navegador con URL de Google')
def step_impl(context):
    global driver
    global busqueda

    options = webdriver.EdgeOptions()
    options.add_argument("--enable-chrome-browser-cloud-management")
    driver = webdriver.Edge(options=options)
    busqueda = pageIngresarPaginaAnime(driver)

    busqueda.navegar("https://www.google.com/")
    driver.maximize_window()

@step(u'Buscar "{texto}" en buscador')
def step_impl(context, texto):
    try:
        busqueda.sendKeys("textarea", "name", "q", texto + Keys.TAB, "1")
        time.sleep(1)
        busqueda.clickButton("input", "name", "btnK", "2")
        time.sleep(3)
        assert texto in busqueda.getTextforClass("h3", "class", "LC20lb MBeuO DKV0Md", "1")
    except AssertionError as ex:
        print(ex)
        raise

@when(u'Seleccionar resultado de la busqueda "{texto}"')
def step_impl(context, texto):
    try:
        match texto:
            case "AnimeFLV":
                url = "https://www3.animeflv.net/"
            case "Crunchyroll":
                url = "https://www.crunchyroll.com/es/"
            case _:
                url = ""
        busqueda.clickButton("a", "href", url, "1")
    except Exception as ex:
        print(ex)
        raise

@then(u'Ingresar exitosamente a la pagina "{texto}"')
def step_impl(context, texto):
    try:
        match texto:
            case "AnimeFLV":
                txt = "ANIMES EN EMISIÓN"
                etiqueta = "strong"
            case "Crunchyroll":
                txt = "¡Anime que puedes mirar gratis!"
                etiqueta = "h2"
            case _:
                txt = ""
                etiqueta = ""

        time.sleep(10)
        assert txt in busqueda.getTextforText(etiqueta, txt, "1")
    except AssertionError as ex:
        print(ex)
        raise
