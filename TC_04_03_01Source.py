from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

browser = webdriver.Chrome()
#login
browser.get("https://dev.digicontent.io")
browser.maximize_window()
uname = browser.find_element_by_id("input_0")
pwd = browser.find_element_by_id("input_1")

uname.send_keys("")#input username inside quotes
pwd.send_keys("")#input password inside quotes
pwd.send_keys(Keys.ENTER)
browser.implicitly_wait(6)
#validate & publish tab
browser.find_element_by_id("tab-item-13").click() #validate and publish tab
browser.find_element_by_xpath("//*[@id='wrap']/div[1]/md-content/div[1]/md-input-container/md-select").click() #open store dropdown in validate&publish
browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option[4]").click() #select the 4th store
browser.implicitly_wait(6)
#Published tab
browser.find_element_by_css_selector("#publishTabs > md-tabs-wrapper > md-tabs-canvas > md-pagination-wrapper > md-tab-item:nth-child(4)").click()
#click the refresh button
browser.implicitly_wait(6)
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
#click the product name
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > span").click()
browser.implicitly_wait(6)
#backspace one letter in name
browser.find_element_by_css_selector("#validProducts > tbody > tr:nth-child(1) > td:nth-child(2) > div > form > div > input").send_keys(Keys.BACKSPACE)
#click outside
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-left._md._md-toolbar-transitions > div").click()
#checkbox
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
#copy sku of item
skuname = browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")
print(skuname)
#action menu
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > md-menu:nth-child(7) > button").click()
browser.implicitly_wait(2)
#update option
browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(1)").click()
time.sleep(8)
browser.find_element_by_css_selector("#publishTabs > md-tabs-wrapper > md-tabs-canvas > md-pagination-wrapper > md-tab-item:nth-child(1)").click()
browser.implicitly_wait(2)
#search start
browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/button[2]").click() #click search button
browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/div[2]/form/input").send_keys(skuname)
#search end
# refresh button
browser.find_element_by_css_selector("#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
browser.implicitly_wait(12)
#print(browser.find_element_by_xpath("//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/md-table-pagination/div[3]/div").get_attribute('innerHTML'))
#validate sku and check the checkbox
for n in range(1, 6):
    if skuname == (browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(n)+"]/td[2]/div/span[2]/a").get_attribute("text")):
        time.sleep(4)
        browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(n)+"]/td[1]/md-checkbox/div[1]").click()
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
        browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
        for m in range(1, 6):
            if skuname == (browser.find_element_by_css_selector("#validProductGrid > div > valid-products-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child("+str(m)+") > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")):
                print("hi")
                time.sleep(4)

                browser.find_element_by_xpath("//*[@id='validProducts']/tbody/tr["+str(m)+"]/td[1]/md-checkbox/div[1]").click()
                browser.find_element_by_xpath("//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
                browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(3)").click()
                print("published :-) "+skuname)
                break

        break

