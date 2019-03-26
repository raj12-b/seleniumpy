from base import *

dc_login()
dc_validatepage(4)
dc_publishedtab()
time.sleep(3)
browser.execute_script("window.scrollTo(1000, 0)")
#get old value
Price = browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > span").text
#click Price
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > span").click()
#enter new value by incrementing old value by 1
Price = int(Price, 10) + 1 #value of Price in string, converting to int of base 10 and adding 1
print(Price)
#clear Price field
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > form > div > input").clear()
#change the Price
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > form > div > input").send_keys(str(Price))
skuname = dc_update()
dc_pendingvalidationtab()
dc_findandpublish(skuname)
print("exit")
