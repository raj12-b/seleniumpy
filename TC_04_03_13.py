from base import *
from selenium.webdriver.common.keys import Keys

dc_login()
dc_validatepage(4)
dc_publishedtab()
time.sleep(3)
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

attachButton = browser.find_element_by_css_selector("#wrap > div.mar-top-50.ng-scope > form > div.product-info-group > md-content > div > md-card:nth-child("+str(n)+") > md-toolbar > div > div.layout-align-end-stretch.layout-row.flex-10 > div")

for i in range(2): #to add multiple images
    #click image attach button
    attachButton.click()
    #enter image url
    url = 'http://chemindigest.com/wp-content/uploads/2018/09/Waters-Sponsors-New-Research-Centre-to-Address-Global-Food-and-Water-Safety-Challenges.jpg'
    textField = browser.find_element_by_css_selector("#dialogContent_customConfirmAlert > div > div > md-input-container.m-b-10.ng-scope.md-input-has-placeholder > input")
    n = 10 #time to wait
    while (True): #equivalent of do while loop in python
        print("in while loop")
        textField.clear() #clear the input field
        textField.send_keys(url) #enter the value
        browser.implicitly_wait(n)
        typed = textField.get_attribute("value") #get the text from input field after send_keys
        print("typed value is ", typed)
        if(typed == url): #check the send_keys_value and text in input field are same, if same quit the loop
            print(n)
            break
        n = n+10 #if not same continue the loop with increased waiting time
    #click upload button
    browser.find_element_by_css_selector("#customConfirmAlert > form > md-dialog-actions > button.default-teal-btn.md-button.ng-scope.md-ink-ripple").click()
    #toaster wait
    time.sleep(10)
    browser.execute_script("arguments[0].scrollIntoView()", attachButton)

#textField.send_keys(Keys.ESCAPE)
#time.sleep(3)
#scroll to update button
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