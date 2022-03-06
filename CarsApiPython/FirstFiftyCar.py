import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


def getCarFeatures() :

    carFeatures = {}

    headers = browser.find_elements(By.TAG_NAME,"dt")
    features = browser.find_elements(By.TAG_NAME,"dd")

    for x in range(0,11):
        carFeatures[headers[x].text] = features[x].text

    return carFeatures

def SetPagetNumberToFifty(pageNumber):
      Select(browser.find_element(By.ID,"pagination-dropdown")).select_by_value(str(pageNumber))    
      return


browser = webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
browser.get("https://www.cars.com/shopping/results/")
time.sleep(10)
SetPagetNumberToFifty(5)




#def chooseBrand(brandName) :
#    Brands = {
#        "acura":"//*[@id='make_select']"
#        }
        
   
#    brandName = brandName.lower()
#    Select(browser.find_element(By.XPATH,"//*[@id='make_select']")).select_by_value(str(brandName))
#    return

    #brandName = brandName.lower()

    #click_Button = browser.find_element_by_xpath("//*[@id='make_select']")

    #click_Button.click()

    #time.sleep(5)

    #click_Button = browser.find_element_by_xpath(Brands[brandName])

    #click_Button.click()

    #return

#def chooseCar(carUrl) :
#    Cars = {
#        "first":" //*[@id='a993e5f9-4b37-4a77-8c34-1aff3b464415']"       
#        }

#    click_Button = browser.find_element_by_class_name("vehicle-card")

#    click_Button.click()

#    time.sleep(10)

#    click_Button = browser.find_element_by_id(2)

#    cliclick_Button.click()

#    return

#browser = webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
#browser.get("https://www.cars.com/shopping/results/")
#time.sleep(10)

#chooseBrand("Acura")

#time.sleep(10)

#chooseCar(2)

#time.sleep(10)