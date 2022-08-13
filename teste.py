
from selenium import webdriver    
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os 

diretorio = os.path.dirname(os.path.realpath(__file__))
driver = "\drivers\chromedriver"
s = Service(diretorio+driver)
navegador = webdriver.Chrome(service=s)
    
def login():
    navegador.get('http://www.saucedemo.com/v1')
    time.sleep(3)
    navegador.find_element_by_id('user-name').send_keys('standard_user')
    time.sleep(3)
    navegador.find_element_by_id('password').send_keys('secret_sauce')
    time.sleep(3)
    navegador.find_element_by_css_selector('.btn_action').click()
    assert "/inventory.html" in navegador.current_url
    time.sleep(5)
login()

def produtoOrdem():
    opcao = Select(navegador.find_element_by_class_name('product_sort_container'))
    opcao.select_by_index(2)
    time.sleep(2)
produtoOrdem()

def selecionaProdutos():
    botoes1 = navegador.find_element_by_xpath("(//button[text()[contains(.,'ADD TO CART')]])[1]")
    botoes1.click()
    time.sleep(3)
    botoes4 = navegador.find_element_by_xpath("(//button[text()[contains(.,'ADD TO CART')]])[3]")
    time.sleep(3)
    botoes4.click()
    time.sleep(2)
selecionaProdutos()

def selecionaCarrinho():
    navegador.find_element_by_xpath("//a[@class='shopping_cart_link fa-layers fa-fw']").click()
    assert "/cart.html" in navegador.current_url
    time.sleep(3)
selecionaCarrinho()

def selecionaCheckout():
    checkout = navegador.find_element_by_xpath("//a[@class='btn_action checkout_button']")
    time.sleep(3)
    checkout.click()
    assert "/checkout-step-one.html" in navegador.current_url
    time.sleep(3)
selecionaCheckout()

def preencheFormulario():
    navegador.find_element_by_id("first-name").send_keys("Letícia")
    time.sleep(3)
    navegador.find_element_by_id("last-name").send_keys("Silva")
    time.sleep(3)
    navegador.find_element_by_id("postal-code").send_keys("231323131")
    time.sleep(3)
    continuar =  navegador.find_element_by_xpath("//input[@type='submit']").click()
preencheFormulario()


time.sleep(5) 
finalizar = navegador.find_element_by_css_selector(".btn_action.cart_button").click()
assert "/checkout-complete.html" in driver.current_url