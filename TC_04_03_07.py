from base import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
dc_login()
dc_validatepage(4) #go to validate page and select the store(nth store sent as argument)
browser.implicitly_wait(6)
dc_publishedtab()
#get SKU
skuname = browser.find_element_by_css_selector("#validProducts > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")
print(skuname)
#print("done")
#click the SKU
time.sleep(4)
sku = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a")))
sku.click()
time.sleep(5)
#clear manufacturer field and enter 'changed'
manufacturer = browser.find_element_by_name("manufacturer")
manufacturer.clear()
manufacturer.send_keys("changed")
manufacturer.send_keys(Keys.PAGE_UP)
time.sleep(1)
#click update button
browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-header > md-content > div > div.product-action-panel.margin-t-50.layout-align-end-stretch.layout-row.flex-100 > div > button:nth-child(2)").click()
#toaster wait
time.sleep(8)
dc_pendingvalidationtab()
dc_findandpublish(skuname)#find a product using SKU in pendingvalidation tab and publish the product
print("exit")