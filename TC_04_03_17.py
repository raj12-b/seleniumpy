from base import *
import time

dc_login()
store = 7 #WSRetail store(a store with less/no configurations set)
skuname = 'qwey3v2' #hard code a sku from the general catalog for the given store(to use 'dc_searchandmove' function)
dc_searchandmove(store, skuname)
dc_validatepage(7)
# search start
browser.find_element_by_xpath(
    "//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/button[2]").click()  # click search button
browser.find_element_by_xpath(
    "//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/div[2]/form/input").send_keys(
    skuname)
# search end
browser.implicitly_wait(10)
# refresh button
browser.find_element_by_css_selector(
    "#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
time.sleep(3)
# validate sku and check the checkbox
print("for loop start")
for n in range(1, 6):
    print(browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(n)+"]/td[2]/div/span[2]/a").get_attribute("text"))
    if skuname == (browser.find_element_by_xpath("//*[@id='pendingValidationGrid']/tbody/tr["+str(n)+"]/td[2]/div/span[2]/a").get_attribute("text")):
        print("first loop")
        time.sleep(4)
        browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child("+str(n)+") > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
        # user defined validation
        browser.find_element_by_xpath("//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
        browser.implicitly_wait(2)
        browser.find_element_by_css_selector(
            "body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(2)").click()
        break
#toaster wait
time.sleep(8)
dc_logout()
print("exit")