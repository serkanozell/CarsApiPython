import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
#driver =
#webdriver.Chrome(executable_path=r'C\Users\serkan\Desktop\chromedriver_win32')

#browser.get("https://www.cars.com/")

#--------------------------------------------------------------------------------------------

#def chooseColor(colorName) :

#    Colors = {"beige":"//*[@id='panel_exterior_colors']/div[1]/label",
#              "black":"//*[@id='panel_exterior_colors']/div[2]/label",
#              "blue":"//*[@id='panel_exterior_colors']/div[3]/label",
#              "brown":"//*[@id='panel_exterior_colors']/div[4]/label",
#              "gold":"//*[@id='panel_exterior_colors']/div[5]/label",
#              "gray":"//*[@id='panel_exterior_colors']/div[6]/label",
#              "green":"//*[@id='panel_exterior_colors']/div[7]/label",
#              "orange":"//*[@id='panel_exterior_colors']/div[8]/label",
#              "purple":"//*[@id='panel_exterior_colors']/div[9]/label",
#              "red":"//*[@id='panel_exterior_colors']/div[10]/label",
#              "silver":"//*[@id='panel_exterior_colors']/div[11]/label",
#              "white":"//*[@id='panel_exterior_colors']/div[12]/label",
#              "yellow":"//*[@id='panel_exterior_colors']/div[12]/label"}

#    colorName = colorName.lower()

#    click_Button =
#    browser.find_element_by_xpath("//*[@id='trigger_exterior_colors']")
#    #click_Button = browser.find_element(By.XPATH,
#    #"//[@id='trigger_exterior_colors']")

#    click_Button.click()

#    time.sleep(5)

#    click_Button = browser.find_element_by_xpath(Colors[colorName])

#    click_Button.click()

#    return

#--------------------------------------------------------------------------------------------

#def chooseBrand(brandName) :
#    Brands = {
#        "audi":"//*[@id='make_select']"
#        }

#    brandName = brandName.lower()

#    click_Button = browser.find_element_by_xpath("//*[@id='make_select']")

#    click_Button.click()

#    time.sleep(5)

#    click_Button = browser.find_element_by_xpath(Brands[brandName])

#    click_Button.click()

#    return
#-----------------------------------------------------------------------------------------------

#def chooseTransmission(transmissionName) : 
#    Transmissions = {
#        "automatic":"//*[@id='panel_transmissions']/div[2]/label"
#        }

#    transmissionName = transmissionName.lower()

#    click_Button = browser.find_element_by_xpath("//*[@id='trigger_transmissions']")

#    click_Button.click()

#    time.sleep(10)

#    click_Button = browser.find_element_by_xpath("//*[@id='panel_transmissions']")

#    click_Button.click()

#    click_Button = browser.find_element_by_xpath(Transmissions[transmissionName])

#    click_Button.click()

#    return
#-------------------------------------------------------------------------------------------


#def chooseYearMin(minYear) : 
    
#    Select(browser.find_element(By.ID,"year_year_min_select")).select_by_value(str(minYear))
#    return

#def chooseYearMax(maxYear) :
#    Select(browser.find_element(By.ID,"year_year_max_select")).select_by_value(str(maxYear))
#    return

#def selectBothYearRange(yearMin,yearMax) :
#    if yearMax>=yearMin:
#        chooseYearMin(yearMin)
#        chooseYearMax(yearMax)
#    return

#--------------------------------------------------------------------------------
    #MinYear = {"minyear":"//*[@id='year_year_min_select']"}
    ##MaxYear = {"maxyear":"//*[@id='year_year_max_select']"}
    
    #click_Button = browser.find_element_by_xpath("//*[@id='year_year_min_select']")

    #click_Button.click()

    #time.sleep(10)

    ##click_Button = browser.find_element_by_xpath("//*[@id='year_year_max_select']")

    ##click_Button.click()

    #click_Button = browser.find_element_by_xpath(MinYear[minYear])

    #clicclick_Button.click()

    #click_Button = browser.find_element_by_xpath(MaxYear[maxYear])

    #click_Button.click()

    #return
#------------------------------------------------------------------------------------------------

#def getCarFeatures() :

#    carFeatures = {}

#    headers = browser.find_elements(By.TAG_NAME,"dt")
#    features = browser.find_elements(By.TAG_NAME,"dd")

#    for x in range(0,11):
#        carFeatures[headers[x].text] = features[x].text

#    return carFeatures

#def SetPagetNumberToFifty(pageNumber):
#      Select(browser.find_element(By.ID,"pagination-dropdown")).select_by_value(str(pageNumber))
#      return

#browser = webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
#browser.get("https://www.cars.com/shopping/results/")
#time.sleep(10)
#SetPagetNumberToFifty(50)
#time.sleep(10)

#chooseYearMin(2020)
#time.sleep(10)
#chooseYearMax(2021)
#time.sleep(10)
#chooseTransmission("Automatic")
#chooseYearRange(2019)
#chooseBrand("Audi")
#chooseColor("Blue")

