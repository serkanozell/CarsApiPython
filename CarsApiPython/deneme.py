import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from flask import Flask,jsonify
from flask import make_response
from flask import request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)

@app.route('/cars/list', methods=['GET'])
def takeAllMetots():


    PATH = "C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://cars.com/for-sale/searchresults.action")
   

    def chooseYearMin(minYear) : 
    
        Select(driver.find_element(By.ID,"year_year_min_select")).select_by_value(str(minYear))
        return

    def chooseYearMax(maxYear) :
        Select(driver.find_element(By.ID,"year_year_max_select")).select_by_value(str(maxYear))
        return

    def selectBothYearRange(year) :
        chooseYearMin(year)
        chooseYearMax(year)
        return
    def setTransmission(trans):
        driver.find_element(By.ID, "trigger_transmissions").click()
        time.sleep(4)
        transmission = driver.find_element(by=By.ID,value="panel_transmissions")
        time.sleep(4)
        transmissionList = transmission.find_elements(by=By.CLASS_NAME,value="sds-checkbox")
        time.sleep(4)
        for t in range(len(transmissionList)):
            value = transmissionList[t].find_element(by=By.CLASS_NAME,value="sds-input")
            value = value.get_attribute('value')
            if value == trans.lower():
                label = transmissionList[t].find_element(by=By.CLASS_NAME,value="sds-label")
                time.sleep(4)
                label.click()
                time.sleep(4)

        return

    def chooseBrand(brandName):
        brandList = Select(driver.find_element(By.ID,"make_select")).select_by_value(str(brandName))
        time.sleep(4)
        return
    def setColor(colorName) : 
        driver.find_element(By.ID,"trigger_exterior_colors").click()
        time.sleep(5)
        color = driver.find_element(by=By.XPATH,value ="//*[@id=\"panel_exterior_colors\"]")
        time.sleep(5)
        colorList = color.find_elements(by=By.CLASS_NAME,value="sds-checkbox")
        time.sleep(5)
        for c in range(len(colorList)):
            value = colorList[c].find_element(by=By.CLASS_NAME,value="sds-input")
            value = value.get_attribute('value')
            if value == colorName.lower():
                label = colorList[c].find_element(by=By.CLASS_NAME,value="sds-label")
                time.sleep(4)
                label.click()
                time.sleep(4)

        return

    info = dict()
    info["cars"] = []
    def getCarDetails():
        car = dict()
        advert = driver.find_element_by_xpath("/html/body/section/div[5]/section/header/div[1]/h1").text
        price = driver.find_element_by_xpath("/html/body/section/div[5]/section/header/div[2]/span[1]").text
        detail = driver.find_element_by_class_name("fancy-description-list")
        advertDetail=driver.find_element_by_xpath("/html/body/section/div[5]/section/header/div[1]/h1").text
        carDetail = detail.text.split('\n') 
        advertDetail2 = advertDetail.split(' ')
        car["advert"] = advert
        car["brand"] = advertDetail2[1]
        car["carColor"] = carDetail[1]
        car["transmission"] = carDetail[11]
        car["price"] = price
        car["year"]=advertDetail2[0]
        info["cars"].append(car)
        return info

    def collectCars():

        driver.find_element(by=By.CLASS_NAME,value="vehicle-card-link").click()
        time.sleep(4)
        carList = {}
        carList[0] = getCarDetails()
        for i in range(2) : 
            try:
                driver.find_element(By.CLASS_NAME,"srp-carousel-next-link").click() 
            except :
                return carList
            carList[i + 1] = getCarDetails()
            time.sleep(4)
       
        return carList
    trans = request.args.get('trans')
    if trans != None:
        setTransmission(trans)
    year = request.args.get('year')
    if year != None:
        selectBothYearRange(year)
    brand = request.args.get('brand')
    if brand != None:
        chooseBrand(brand)
    color = request.args.get('color')
    if color != None:
        setColor(color)   
    collectCars()
    #carList = collectCars()
    time.sleep(2)
    return info

if __name__ == '__main__':
    app.run(debug=True)




#app = Flask(__name__)

#@app.route('/cars/list',methods=['GET'])
#def SetPageNumberToFifty():
#      drp = (browser.find_element(By.ID,"pagination-dropdown"))
#      drp.select_by_index(3)
#      time.sleep(5)
#      return

#def listCars():
#    browser.get("https://cars.com/for-sale/searchresults.action")

#    def getCarFeatures() :

#        carFeatures = {}

#        headers = browser.find_elements(By.TAG_NAME,"dt")
#        features = browser.find_elements(By.TAG_NAME,"dd")

#    for x in range(0,11):
#        carFeatures[headers[x].text] = features[x].text

#    return carFeatures

#    def goingatherdetails():

#        browser.find_element(By.CLASS_NAME,"vehicle-card-link").click()
#        time.sleep(10)
#        cars = {}
#        cars[0] = getCarFeatures()

#        for x in range(2):
#            cars[x + 1] = getCarFeatures()
#            time.sleep(10)
#            browser.find_element(By.XPATH,"/html/body/section/div[4]/section[2]/div/div[2]/a").click()
#            time.sleep(10)

#    return cars
    
#    cars = goingatherdetails()
#    time.sleep(10)
#    browser.close()

#    return jsonify({'cars' : cars})

#if __name__ == '__main__':
#    app.run(debug=True)


#browser = webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
#browser.get("https://cars.com/for-sale/searchresults.action")
#time.sleep(10)

    #colorName = colorName.lower()

    #chooseColorType = driver.find_element_by_xpath(Colors[colorName]).click()
    #return
#beige =
#driver.find_element(By.XPATH,"//*[@id='panel_exterior_colors']/div[1]/label").click()
#chooseColor =
#Select(driver.find_elements(By.CLASS_NAME,"sds-checkbox")).select_by_value(black)
#time.sleep(10)
    #def getCarFeatures() :

    #    carFeatures = {}

    #    headers = driver.find_elements(By.TAG_NAME,"dt")
    #    features = driver.find_elements(By.TAG_NAME,"dd")


    #    for x in range(0,11):
    #        carFeatures[headers[x].text] = features[x].text


    #    return carFeatures

        #return jsonify({'cars': info})
    #driver.quit()
    
    #setTransmission()
    #time.sleep(2)
    #selectBothYearRange()
    #time.sleep(2)
    #setColor()
    #time.sleep(4)
    #chooseBrand("bmw")
    #time.sleep(4)
    #searchpage =
    #Select(driver.find_element(By.ID,"pagination-dropdown")).select_by_index(3)
    #time.sleep(4)
    #collectCars()

            #type =
        #driver.find_element(By.XPATH,"//*[@id='panel_transmissions']/div[2]/label").click()

            #url = "https://www.cars.com/for-sale/searchresults.action"