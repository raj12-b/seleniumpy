from selenium import webdriver
import time
browser = webdriver.Chrome()


def dc_login():

    from selenium.webdriver.common.keys import Keys
    # login
    global browser
    browser.get("https://dev.digicontent.io")
    browser.maximize_window()
    uname = browser.find_element_by_id("input_0")
    pwd = browser.find_element_by_id("input_1")

    uname.send_keys("")  # enter username inside quotes
    pwd.send_keys("")  # enter password inside quotes
    pwd.send_keys(Keys.ENTER)
    browser.implicitly_wait(6)

def dc_validatepage(n): #go to validate page and select the store(nth store sent as argument)
    # validate & publish page
    global browser
    browser.find_element_by_id("tab-item-13").click()  # validate and publish tab
    browser.find_element_by_xpath("//*[@id='wrap']/div[1]/md-content/div[1]/md-input-container/md-select").click()  # open store dropdown in validate&publish
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option["+str(n)+"]").click()  # select the nth store
    browser.implicitly_wait(10)

def dc_publishedtab():
    # validate & publish tab
    global browser
    #browser.find_element_by_id("tab-item-13").click()  # validate and publish tab
    #browser.find_element_by_xpath("//*[@id='wrap']/div[1]/md-content/div[1]/md-input-container/md-select").click()  # open store dropdown in validate&publish
    #browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option[4]").click()  # select the 4th store(rstore)
    #browser.implicitly_wait(10)
    # Published tab
    browser.find_element_by_css_selector("#publishTabs > md-tabs-wrapper > md-tabs-canvas > md-pagination-wrapper > md-tab-item:nth-child(4)").click()
    time.sleep(2)

def dc_pendingvalidationtab():
    global browser
    # validate & publish tab
    #browser.find_element_by_id("tab-item-13").click()  # validate and publish tab
    #browser.find_element_by_xpath("//*[@id='wrap']/div[1]/md-content/div[1]/md-input-container/md-select").click()  # open store dropdown in validate&publish
    #browser.find_element_by_xpath("/html/body/div[3]/md-select-menu/md-content/md-option[4]").click()  # select the 4th store(rstore)
    #browser.implicitly_wait(10)
    # pending validation tab
    browser.find_element_by_css_selector("#publishTabs > md-tabs-wrapper > md-tabs-canvas > md-pagination-wrapper > md-tab-item:nth-child(1)").click()
    browser.implicitly_wait(6)

def dc_findandpublish(skuname): #find a product using SKU in pendingvalidation tab and publish the product
    import time
    # search start
    browser.find_element_by_xpath(
        "//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/button[2]").click()  # click search button
    browser.find_element_by_xpath(
        "//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/div[2]/form/input").send_keys(
        skuname)
    # search end
    time.sleep(3)
    # refresh button
    browser.find_element_by_css_selector(
        "#validProductsGrid > div > pending-validation-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
    time.sleep(3)
    # validate sku and check the checkbox
    print("for loop start")
    for n in range(1, 6):
        print(browser.find_element_by_xpath(
            "//*[@id='pendingValidationGrid']/tbody/tr[" + str(n) + "]/td[2]/div/span[2]/a").get_attribute("text"))
        if skuname == (browser.find_element_by_xpath(
                "//*[@id='pendingValidationGrid']/tbody/tr[" + str(n) + "]/td[2]/div/span[2]/a").get_attribute("text")):
            print("first loop")
            time.sleep(4)
            browser.find_element_by_css_selector("#pendingValidationGrid > tbody > tr:nth-child(" + str(
                n) + ") > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
            # user defined validation
            browser.find_element_by_xpath(
                "//*[@id='validProductsGrid']/div/pending-validation-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
            browser.implicitly_wait(2)
            browser.find_element_by_css_selector(
                "body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(2)").click()
            browser.find_element_by_xpath(
                "//*[@id='publishTabs']/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[2]").click()
            browser.implicitly_wait(2)
            browser.find_element_by_css_selector(
                "#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button.md-icon-button.md-button.md-ink-ripple.cust-search.md-button").click()
            browser.implicitly_wait(2)
            browser.find_element_by_css_selector(
                "#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > div.md-default.grid-toolbar.grid-search-div.font-16px.display-flex > form > input").send_keys(
                skuname)
            print("second for loop start")
            time.sleep(3)
            # refresh button
            browser.find_element_by_css_selector(
                "#validProductGrid > div > valid-products-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
            time.sleep(3)
            for m in range(1, 6):
                print(browser.find_element_by_css_selector(
                    "#validProductGrid > div > valid-products-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(" + str(
                        m) + ") > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text"))
                if skuname == (browser.find_element_by_css_selector(
                        "#validProductGrid > div > valid-products-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(" + str(
                                m) + ") > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute("text")):
                    print("hi")
                    browser.implicitly_wait(2)
                    browser.find_element_by_css_selector(
                        "#validProductGrid > div > valid-products-grid > md-content > md-card > md-table-container > table > tbody > tr > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
                    browser.find_element_by_xpath(
                        "//*[@id='validProductGrid']/div/valid-products-grid/md-content/md-card/div[1]/md-toolbar[2]/div/md-menu[2]/button").click()
                    browser.find_element_by_css_selector(
                        "body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(3)").click()
                    print("published :-) " + skuname)
                    break
            break

def dc_update(): #click the checkbox of first entry and select update in published tab
    # click outside
    browser.find_element_by_css_selector(
        "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.width-50.pull-left._md._md-toolbar-transitions > div").click()
    # checkbox
    checkbox = browser.find_element_by_css_selector(
        "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple")
    # scroll until checkbox visible
    browser.execute_script("arguments[0].scrollIntoView();", checkbox)
    checkbox.click()
    # copy sku of item
    skuname = browser.find_element_by_css_selector(
        "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > md-table-container > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute(
        "text")
    print(skuname)
    # action menu
    browser.find_element_by_css_selector(
        "#publishedProductGrid > div > catalog-published-product-grid > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > md-menu:nth-child(7) > button").click()
    browser.implicitly_wait(2)
    # update option
    browser.find_element_by_css_selector(
        "body > div._md.md-open-menu-container.md-whiteframe-z2.md-active.md-clickable > md-menu-content > md-menu-item:nth-child(1)").click()
    # toaster wait
    time.sleep(6)
    return skuname

def dc_searchandmove(store, skuname):   # move an item from general catalog
    browser.find_element_by_id("tab-item-12").click()
    browser.implicitly_wait(6)
    browser.find_element_by_xpath(
        "//*[@id='fileUploadSection-content']/div/div[2]/md-input-container").click()  # open store dropdown
    time.sleep(1)
    browser.find_element_by_xpath(
        "/html/body/div[3]/md-select-menu/md-content/md-option[" + str(store) + "]").click()  # select a store
    time.sleep(8)
    # search start
    browser.find_element_by_css_selector(
        "#uploadGrid > md-content > div.flex-100 > div > generalcatalog-grid-directive > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button.md-icon-button.md-button.md-ink-ripple.cust-search.md-button").click()  # click search button
    browser.find_element_by_css_selector(
        "#uploadGrid > md-content > div.flex-100 > div > generalcatalog-grid-directive > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > div.md-default.grid-toolbar.grid-search-div.font-16px.display-flex.width-27 > form > input").send_keys(
        skuname)
    # search end
    time.sleep(12)

    while True:  # do while equivalent
        # refresh button
        browser.find_element_by_css_selector(
            "#uploadGrid > md-content > div.flex-100 > div > generalcatalog-grid-directive > md-content > md-card > div.layout-row > md-toolbar.md-table-toolbar.md-default.grid-toolbar.pull-right._md._md-toolbar-transitions > div > button:nth-child(2)").click()
        print("in loop")
        time.sleep(5)
        print("end time")
        if (skuname == (browser.find_element_by_css_selector(
                "#pendingValidationGrid > tbody > tr > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute(
                "text"))):
            break

    # click checkbox
    print("checkbox")
    browser.find_element_by_css_selector(
        "#pendingValidationGrid > tbody > tr:nth-child(1) > td.md-cell.md-checkbox-cell > md-checkbox > div.md-container.md-ink-ripple").click()
    # if condition for double-check
    if (skuname == (browser.find_element_by_css_selector(
            "#pendingValidationGrid > tbody > tr > td:nth-child(3) > div > span:nth-child(2) > a").get_attribute(
        "text"))):
        # click 'Move Products' button
        browser.find_element_by_xpath("//*[@id='fileUploadSection-content']/div/div[1]/button").click()
        browser.implicitly_wait(2)
        # confirm move products
        browser.find_element_by_xpath(
            "//*[@id='dialogContent_customAlert']/div/div/md-dialog-actions/button[2]").click()
        # toaster wait
        time.sleep(8)
    # move complete