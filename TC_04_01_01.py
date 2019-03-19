from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

browser = webdriver.Chrome()
#login
browser.get("https://dev.digicontent.io")
browser.maximize_window()
uname = browser.find_element_by_id("input_0")
pwd = browser.find_element_by_id("input_1")

uname.send_keys("")#enter username inside quotes
pwd.send_keys("")#enter password inside quotes
pwd.send_keys(Keys.ENTER)
browser.implicitly_wait(6)

#move an item from general catalog
browser.find_element_by_id("tab-item-12").click()
store = randint(1, 5)
browser.implicitly_wait(6)
browser.find_element_by_xpath("//*[@id='fileUploadSection-content']/div/div[2]/md-input-container").click() #open store dropdown
browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option["+str(store)+"]").click() #select a store
browser.implicitly_wait(6)
#SKU(move is not complete)
skurand = randint(1, 5)
browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(skurand)+"]/td[1]/md-checkbox/div[1]").click()
print(browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(skurand)+"]/td[3]/div/span[2]/a").get_attribute("text"))
skuname = (browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(skurand)+"]/td[3]/div/span[2]/a").get_attribute("text"))
#SKU complete
browser.find_element_by_xpath("//*[@id='fileUploadSection-content']/div/div[1]/button").click()
browser.implicitly_wait(2)
browser.find_element_by_xpath("//*[@id='dialogContent_customAlert']/div/div/md-dialog-actions/button[2]").click()
#move complete

time.sleep(10)

#validate & publish tab
browser.find_element_by_id("tab-item-13").click() #validate and publish tab
browser.find_element_by_xpath("//*[@id='wrap']/div[1]/md-content/div[1]/md-input-container/md-select").click() #open store dropdown in validate&publish
browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option["+str(store)+"]").click() #select the same store
browser.implicitly_wait(6)
#skuname = 'amcreated-img2'
#search start
browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/button[2]").click() #click search button
browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/div[2]/form/input").send_keys(skuname)
#search end
browser.implicitly_wait(2)
#refresh button
browser.find_element_by_css_selector("#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
#print(browser.find_element_by_xpath("//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/md-table-pagination/div[3]/div").get_attribute('innerHTML'))
#validate sku and check the checkbox - without for loop
if skuname == (browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr/td[2]/div/span[2]/a").get_attribute("text")):
    browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr[1]/td[1]/md-checkbox/div[1]").click()
    #user defined validation
    browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
    browser.implicitly_wait(6)
    browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(2)").click()
    browser.find_element_by_xpath("//*[@id='publishTabs']/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[2]").click()
    browser.implicitly_wait(6)
    browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button.md-icon-button.md-button.md-ink-ripple.cust-search.md-button").click()
    browser.implicitly_wait(6)
    browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > div.md-default.grid-toolbar.grid-search-div.font-16px.display-flex > form > input").send_keys(skuname)
    #refresh button
    #print("refresh")
    browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
    if skuname == (browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")):
        print("hi")
        browser.find_element_by_xpath("//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/md-table-container/table/thead[1]/tr/th[1]/md-checkbox/div[1]").click()
        browser.find_element_by_xpath("//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
        browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(3)").click()
        print("published :-) "+skuname)



