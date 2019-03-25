from base import *
from selenium.webdriver.support.select import Select
from random import randint

dc_login()
dc_validatepage(4)
dc_publishedtab()
time.sleep(3)
#click the UOM
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(8) > div > span").click()
#click the UOM again to open dropdown
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(8) > div > form > div > select").click()
#uom 'Select'
uom = Select(browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(8) > div > form > div > select"))
#get uom options
uomOptions = uom.options
#generate a random number
randomuom = randint(1, len(uomOptions))
#select a random UOM
uom.select_by_index(randomuom-1)
browser.implicitly_wait(4)
#click outside
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-left._md._md-toolbar-transitions > div").click()
#checkbox
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
#copy sku of item
skuname = browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")
print(skuname)
#action menu
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > md-menu:nth-child(7) > button").click()
browser.implicitly_wait(2)
#update option
browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(1)").click()
#toaster wait
time.sleep(6)
dc_pendingvalidationtab()
dc_findandpublish(skuname)
print("exit")
