from base import *

dc_login()
browser.implicitly_wait(20)
#Inventory&Price page
browser.find_element_by_css_selector("#tab-item-15").click()
time.sleep(5)
#upload inventory button
#enter the upload file location
browser.find_element_by_css_selector("#fileInput").send_keys("C:/Users/WINDOWS/Documents/Automation/Inventory/TC_08_01_07.csv")
#toastr message
msg = browser.find_element_by_class_name("toast-message").get_attribute("innerHTML")
#comparing actual and expected error messages
if msg == 'Please upload valid file format (Excel/XML)':
    print("Correct warning message is displayed")
else:
    print("msg is ", msg)
#toaster wait
time.sleep(8)
print("exit")