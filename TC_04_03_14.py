from base import *
from selenium.webdriver.common.keys import Keys

dc_login()
dc_validatepage(7)
dc_publishedtab()
time.sleep(4)
#get SKU
skuname = browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")
print(skuname)
#click the SKU
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").click()
time.sleep(7)
imageClose = browser.find_element_by_css_selector("#imagesLightGalleryEdit > div > div > div.img_wrp.ng-scope > md-icon")
browser.execute_script("arguments[0].scrollIntoView()", imageClose)
imageClose.click()
browser.find_element_by_css_selector("#customConfirmAlert > form > md-dialog-actions > button.default-teal-btn.md-button.md-ink-ripple").click()
#toaster wait
time.sleep(7)
#not always the price field, but an input field
priceLabel = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-group > md-content > div > md-card:nth-child(1) > md-card-content > div > div > div > div > div:nth-child(6) > div.p-l-25.flex-xs-50.flex-sm-60.flex-60 > div > div > md-input-container > input")
browser.execute_script("arguments[0].scrollIntoView()", priceLabel)
priceLabel.send_keys(Keys.PAGE_UP, Keys.PAGE_UP)
time.sleep(1)
#update button
updateButton = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-header > md-content > div > div.product-action-panel.margin-t-50.layout-align-end-stretch.layout-row.flex-100 > div > button:nth-child(2)")
updateButton.click()
#toaster wait
time.sleep(10)
dc_pendingvalidationtab()
dc_findandpublish(skuname)
print("exit")