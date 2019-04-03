from base import *

dc_openStore()
browser.implicitly_wait(25)
#click the product(3rd product)
browser.find_element_by_css_selector("#product-grid-list > li:nth-child(3) > div > a > div").click()
#click add to cart button
browser.find_element_by_css_selector("#reactionAppContainer > main > span > div > div > div > div > div > div.rui.layout-base.items.flex > div:nth-child(3) > div.pdp.add-to-cart.block > button").click()
#toaster wait
time.sleep(6)
#click the cart button
browser.find_element_by_css_selector("#reactionAppContainer > div:nth-child(1) > div.rui.navbar > div.cart-container > div.cart > div").click()
print("exit")