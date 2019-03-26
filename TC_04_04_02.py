from base import *

dc_login()
dc_validatepage(4)
dc_publishedtab()
time.sleep(3)
# copy sku of item
skuname = browser.find_element_by_css_selector(
        "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute(
        "text")
print(skuname)
deleteButton = browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(15) > span > span:nth-child(1)")
browser.execute_script("arguments[0].scrollIntoView();", deleteButton)
deleteButton.click()
#confirm delete
browser.find_element_by_css_selector("#dialogContent_customAlert > div > div > md-dialog-actions > button.default-teal-btn.md-button.md-ink-ripple").click()
#toaster wait
time.sleep(8)
#skuname = 'WATR048592'  #WATR045797 #WATR048584
#store = 4
dc_searchandmove(4, skuname)
dc_validatepage(4)
dc_findandpublish(skuname)
print("exit")