from base import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
#scroll until image attachment button
n = 2
headerName = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-group > md-content > div > md-card:nth-child("+str(n)+") > md-toolbar > div > div.md-accordion-item-header.layout-align-start-stretch.layout-row.flex-90 > div.accordion-title > span")
while (headerName.text != 'Images'):
    print("header is ", headerName.text)
    n = n+1
    time.sleep(1)
    #re-initialize header name with updated 'n'
    headerName = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-group > md-content > div > md-card:nth-child("+str(n)+") > md-toolbar > div > div.md-accordion-item-header.layout-align-start-stretch.layout-row.flex-90 > div.accordion-title > span")
    #print("n is incremented")
imageEdit = browser.find_element_by_css_selector("#imagesLightGalleryEdit")
browser.execute_script("arguments[0].scrollIntoView()", imageEdit)
#move the first image to last place(drag and drop)
attachButton = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-group > md-content > div > md-card:nth-child("+str(n)+") > md-toolbar > div > div.layout-align-end-stretch.layout-row.flex-10 > div")
source = browser.find_element_by_css_selector("#imagesLightGalleryEdit > div:nth-child(1)")
destination = attachButton
ActionChains(browser).drag_and_drop(source, destination).perform()
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