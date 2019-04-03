from base import *
dc_openStore()
browser.implicitly_wait(25)
#click the product with zero price(2nd product)
browser.find_element_by_css_selector("#product-grid-list > li:nth-child(2) > div > a > div").click()
#click add to cart button
browser.find_element_by_css_selector("#reactionAppContainer > main > span > div > div > div > div > div > div.rui.layout-base.items.flex > div:nth-child(3) > div.pdp.add-to-cart.block > button").click()
#toaster wait
time.sleep(6)
#click the cart button
browser.find_element_by_css_selector("#reactionAppContainer > div:nth-child(1) > div.rui.navbar > div.cart-container > div.cart > div").click()
#click the punchout button
browser.find_element_by_css_selector("#cart-drawer-container > div > div > div:nth-child(3) > div > div:nth-child(2) > div.checkout-btn > button").click()
#click the request button(comment above line, change the product in line 5 and uncomment the next line for TC_05_01_17)
#browser.find_element_by_css_selector("#cart-drawer-container > div > div > div:nth-child(3) > div > div:nth-child(2) > div.quote-req-section > button").click()
print("exit")