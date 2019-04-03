from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base import *
dc_openStore()
#wait until cart button is displayed
element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#reactionAppContainer > div:nth-child(1) > div.rui.navbar > div.cart-container"))
    )
#click the cart button
element.click()
print("exit")