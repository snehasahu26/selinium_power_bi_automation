from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image 
from selenium.webdriver.support.ui import Select
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver.common.action_chains import ActionChains

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
YES=(By.ID, "idSIButton9")


browser = webdriver.Chrome('D:/selinium_automation/chromedriver.exe')
browser.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=871c010f-5e61-4fb1-83ac-98610a7e9110&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DqrOwG8YMpUNTxNxFx34G-wJohyDaR1mqwA0HHDA4HdbNG5fjrLxDh4jbzTJkIH_3aE4Nxk2upJ9szqLIZ2iLGGyRH4HeO09X9jRVwlRZI1AlY91vj2egTQCf0YIV9jPWWrB8z4ZqDk7e1-hAAMDJhw&response_mode=form_post&nonce=637160463269170685.MGM4M2JhMWQtNWM3Mi00ZDRiLTgxNmUtMjQ3ZTA0YmI1NjQzOGU5OWZkOTItNmRjNS00YThlLTg1ZjMtZmFjOWZkMDg1Mjk3&site_id=500453&redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1&post_logout_redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&nux=1&msafed=0&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0&sso_reload=true')

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("ssahu@gemini-us.com")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("welcome@123")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(YES)).click()
time.sleep(5)

browser.get("https://app.powerbi.com/groups/me/list/reports")

browser.find_element_by_xpath('//*[@title="dataset_kpi"]').click()
time.sleep(15)


#print(browser.find_element_by_class_name('slicer-dropdown-menu').text)

#slicer-restatement

'''
like = browser.find_elements_by_class_name('slicer-restatement')
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(len(like))
for x in range(0,len(like)):
    if like[x].is_displayed():
        print(like[x].text)
'''

        
        
#browser.find_elements_by_class_name('slicer-restatement")


#### ramesh code
browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()

time.sleep(10)


browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 55 })")
#$('.scrollRegion').parent().animate({ scrollTop: 55 })

time.sleep(10)

browser.execute_script("$('.visibleGroup').find('.row:nth-child(1)').find('.slicerItemContainer').click()")
#browser.find_elements_by_class_name('slicerItemContainer').click()

time.sleep(2)
browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 110 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(2)').find('.slicerItemContainer').click()")
time.sleep(5)
print("one got clicked")
browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 110 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(3)').find('.slicerItemContainer').click()")
time.sleep(5)
print("2 got clicked ")
browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 110 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(4)').find('.slicerItemContainer').click()")
time.sleep(5)
print("3 got clicked")
browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 110 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(5)').find('.slicerItemContainer').click()")
time.sleep(5)
print("4 got clikced ")
browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()

browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 330 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(1)').find('.slicerItemContainer').click()")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(2)').find('.slicerItemContainer').click()")
print("7th got clicked")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(3)').find('.slicerItemContainer').click()")
print("7th got clicked")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(4)').find('.slicerItemContainer').click()")
print("7th got clicked")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(5)').find('.slicerItemContainer').click()")
print("7th got clicked")

time.sleep(5)
browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
time.sleep(2)
browser.execute_script("$('.scrollRegion').parent().animate({ scrollTop: 610 })")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(1)').find('.slicerItemContainer').click()")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(2)').find('.slicerItemContainer').click()")
print("7th got clicked")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(3)').find('.slicerItemContainer').click()")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(4)').find('.slicerItemContainer').click()")
time.sleep(5)
browser.execute_script("$('.visibleGroup').find('.row:nth-child(5)').find('.slicerItemContainer').click()")


#like = browser.find_elements_by_class_name('slicerItemContainer')

#like.index().click()
### for visible element

#element = browser.find_elements_by_class_name('slicerItemContainer')
#actions = ActionChains(browser)
#actions.move_to_element(element[4]).perform()
#
#actions.move_to_element(element[4]).click()
#
#source_element = browser.find_element_by_class_name('slicerItemContainer') ### Scrollbar element
#
#dest_element = actions.move_to_element(element[4]) ### ▼ element
#
#ActionChains(browser).drag_and_drop(source_element, dest_element).perform()


#WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME , 'slicerItemContainer'))).click()




#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#print(len(like))
#for x in range(0,len(like)):
#  if like[x].is_displayed():
#      like[x].click()
#      print(like[x])
#      print("#### text #################")
#      print(like[x].text)
#      time.sleep(10)
#      #to click on the drop down 
#      browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
'''
element = browser.find_elements_by_class_name('slicerItemContainer')

actions = ActionChains(browser)
actions.move_to_element(element[4]).perform()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()

like1 = browser.find_elements_by_class_name('slicerItemContainer').click()

print(len(like1))
print(like1[4].is_displayed())
'''
#element = browser.find_elements_by_class_name('slicerItemContainer')
#
#actions = ActionChains(browser)
#actions.move_to_element(element[4]).perform()
#time.sleep(10)
#browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
##browser.find_elements_by_class_name('slicerItemContainer').click()

############
'''
for each in range(4,10):
    print("entered into for looooooooooop ")
    actions = ActionChains(browser)
    actions.move_to_element(element[each]).perform()
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
    x=browser.find_elements_by_class_name('slicerItemContainer')
    time.sleep(4)
    if x[each].is_displayed():
        print("@@@ inside inner for loop @@@@@@@@@@")
        print(x[each].text)
        x[each].click()
        time.sleep(10)
      #to click on the drop down 
        browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
'''
#actions.move_to_element(element[4]).perform()
#element = browser.find_elements_by_class_name('slicerItemContainer')
#actions = ActionChains(browser)
#actions.move_to_element(element[4]).perform()
#
#actions.move_to_element(element[4]).click()

