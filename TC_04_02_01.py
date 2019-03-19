from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
browser.find_element_by_xpath("//*[@id='publishedProductGrid']/div/catalog-published-product-grid/md-content/md-card/md-table-container/table/tbody/tr[1]/td[2]/div/span").click()
browser.implicitly_wait(6)
#backspace one letter in name
browser.find_element_by_css_selector("#validProducts > tbody > tr:nth-child(1) > td:nth-child(2) > div > form > div > input").send_keys(Keys.BACKSPACE)
#click outside
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-left._md._md-toolbar-transitions > div").click()
#checkbox
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
#action menu
browser.find_element_by_css_selector("#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > md-menu:nth-child(7) > button").click()
browser.implicitly_wait(2)
#update option
browser.find_element_by_css_selector("body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(1)").click()
