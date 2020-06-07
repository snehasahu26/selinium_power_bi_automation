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
#from azure.storage.blob import BlockBlobService

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
YES=(By.ID, "idSIButton9")


browser = webdriver.Chrome('D:/selinium_automation/chromedriver.exe')
browser.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=871c010f-5e61-4fb1-83ac-98610a7e9110&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DqrOwG8YMpUNTxNxFx34G-wJohyDaR1mqwA0HHDA4HdbNG5fjrLxDh4jbzTJkIH_3aE4Nxk2upJ9szqLIZ2iLGGyRH4HeO09X9jRVwlRZI1AlY91vj2egTQCf0YIV9jPWWrB8z4ZqDk7e1-hAAMDJhw&response_mode=form_post&nonce=637160463269170685.MGM4M2JhMWQtNWM3Mi00ZDRiLTgxNmUtMjQ3ZTA0YmI1NjQzOGU5OWZkOTItNmRjNS00YThlLTg1ZjMtZmFjOWZkMDg1Mjk3&site_id=500453&redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1&post_logout_redirect_uri=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&nux=1&msafed=0&x-client-SKU=ID_NET45&x-client-ver=5.3.0.0&sso_reload=true')

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("mchilukala@geminius.onmicrosoft.com")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("Gemini@123")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(YES)).click()
time.sleep(5)

browser.get("https://app.powerbi.com/groups/me/list/reports")

browser.find_element_by_xpath('//*[@title="dataset_kpi"]').click()
time.sleep(10)


       
#browser.find_element_by_class_name('slicer-restatement').text
#browser.find_elements_by_class_name('slicer-restatement")


#### ramesh code
browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()

time.sleep(1)

for i in range(0,10):
    browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[2]/transform/div/div[3]/visual-modern/div/div/div[2]/div/i').click()
    print('dropdown clicked')
    time.sleep(2)
    #print("$('.scrollRegion').parent().animate({} )".format("{scrollTop: "+str(55*i)+'}'))
    browser.execute_script("$('.scrollRegion').parent().animate({} )".format("{scrollTop: "+str(55*i)+'}'))
    time.sleep(2)
    print('scroll-bar clicked')
    browser.execute_script("$('.visibleGroup').find('.row:nth-child(1)').find('.slicerItemContainer').click()")
    name=browser.find_element_by_class_name('slicer-restatement').text
    time.sleep(2)
    element = browser.find_element_by_class_name('visualContainerHost') # find part of the page you want image of
    location = element.location
    size = element.size
    png = browser.get_screenshot_as_png() # saves screenshot of entire page
    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines crop
    im.save(name +'.png')
    ## image to azure
    #block_blob_service = BlockBlobService(account_name='fankickuat', account_key='PNxQuzWQMCw8kijdrRHcOPtaOs2yrwkFDiXagiVZ18MKE4EDmp5f8VgQiJRVxStAZfva7tck3LLxyUdvs+NwIA==') 
    #block_blob_service.create_blob_from_path('images', name+'.png', "D:/selinium_automation/127fb3963b12b4f0b339ff0c8ee14558-9b9fb97eba993a13e10e03369834be69203573a8/"+name+".png")
    #print(block_blob_service.make_blob_url('images', name+'.png'))
    
    time.sleep(5)
    print('element clicked'+str(i))
    

