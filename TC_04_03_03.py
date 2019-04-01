from base import *
from selenium.webdriver.common.keys import Keys

dc_login()
dc_validatepage(4)
time.sleep(2)
#click the Description of a product
browser.find_element_by_css_selector("#validProductsGrid > div > pending-validation-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span > span").click()
browser.implicitly_wait(6)
#go to the end of description
browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child(1) > td:nth-child(3) > div > form > div > textarea").send_keys(Keys.END)
#backspace one letter
browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child(1) > td:nth-child(3) > div > form > div > textarea").send_keys(Keys.BACKSPACE)
#click outside
browser.find_element_by_css_selector("#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-left._md._md-toolbar-transitions > div").click()
#click the checkbox
browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
#copy sku
skuname = browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child(1) > td:nth-child(2) > div > span:nth-child(2) > a").get_attribute("text")
print(skuname)
#action button
browser.find_element_by_css_selector("#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > md-menu:nth-child(6) > button").click()
browser.implicitly_wait(3)
#click update option
browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(3) > button").click()
#toaster wait
time.sleep(8)
dc_findandpublish(skuname)
#toaster wait
time.sleep(8)
dc_logout()
print("exit")