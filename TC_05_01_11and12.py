from base import *

dc_openStore()
browser.implicitly_wait(30)
#click the product(3rd product)
browser.find_element_by_css_selector("#product-grid-list > li:nth-child(3) > div > a > div").click()
#click add to cart button
browser.find_element_by_css_selector("#reactionAppContainer > main > span > div > div > div > div > div > div.rui.layout-base.items.flex > div:nth-child(3) > div.pdp.add-to-cart.block > button").click()
#toaster wait
time.sleep(6)
#click the home button
browser.find_element_by_css_selector("#reactionAppContainer > div:nth-child(1) > div.rui.navbar > a > div").click()
browser.implicitly_wait(10)
#click the product(2nd product)
browser.find_element_by_css_selector("#product-grid-list > li:nth-child(2) > div > a > div").click()
#click add to cart button
browser.find_element_by_css_selector("#reactionAppContainer > main > span > div > div > div > div > div > div.rui.layout-base.items.flex > div:nth-child(3) > div.pdp.add-to-cart.block > button").click()
#toaster wait
time.sleep(6)
#click the cart button
browser.find_element_by_css_selector("#reactionAppContainer > div:nth-child(1) > div.rui.navbar > div.cart-container > div.cart > div").click()
time.sleep(4)
for i in range(2): #to remove 2 items
    #click the remove button
    browser.find_element_by_css_selector("#cart-drawer-container > div > div > div:nth-child(2) > div.cart-body > div:nth-child(1) > div > div.item-action > button").click()
    #confirm delete
    browser.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled").click()
    time.sleep(6)
print("exit")