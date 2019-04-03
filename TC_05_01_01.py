from base import *
dc_openStore()
browser.implicitly_wait(25)
#click the product(3rd product)
browser.find_element_by_css_selector("#product-grid-list > li:nth-child(3) > div > a > div").click()
#click the second image of the product in product detail page
browser.find_element_by_css_selector("#reactionAppContainer > main > span > div > div > div > div > div > div.rui.layout-base.items.flex > div:nth-child(2) > div > div > div > div.rui.gallery-thumbnails > div:nth-child(2) > img").click()
print("exit")