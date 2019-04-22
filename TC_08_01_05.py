from base import *

dc_login()
browser.implicitly_wait(20)
#Inventory&Price page
browser.find_element_by_css_selector("#tab-item-15").click()
time.sleep(5)
#upload inventory button
#enter the upload file location
browser.find_element_by_css_selector("#fileInput").send_keys("C:/Users/WINDOWS/Documents/Automation/Inventory/TC_08_01_05.xlsx")
#toastr message
msg = browser.find_element_by_class_name("toast-message").get_attribute("innerHTML")
print("msg is",msg)
#toaster wait
time.sleep(8)
#click refresh button in Inventory tab
browser.find_element_by_css_selector("#quoteGrid > md-content > div > div > inventory-price-upload-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
#click the id
browser.find_element_by_css_selector("#quoteGrid > md-content > div > div > inventory-price-upload-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(1) > span:nth-child(2) > a").click()
browser.implicitly_wait(5)
#get UOM
uom = browser.find_element_by_css_selector("#productGrid > inventory-price-products-grid > md-content > md-card > md-table-container > table > tbody > tr > td:nth-child(7) > span:nth-child(1)").get_attribute("innerHTML")
if uom is '':
    print("File is uploaded without UOM")
else:
    print("UOM is", uom)
print("exit")