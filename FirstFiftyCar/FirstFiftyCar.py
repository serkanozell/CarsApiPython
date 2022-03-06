import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import pprint
from flask import Flask,jsonify
from flask import make_response

#url =
#"https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=1&perPage=20&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006"
#url =
#"https://www.cars.com/vehicledetail/4ac00116-5912-4b9c-a2e8-59073cad7bc1/"
url = "https://www.cars.com/for-sale/searchresults.action"
browser = webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
def parse_json(url):
    with requests.get(url) as res:
        if res.status_code == 200:
            info = dict()
            info["cars"] = []
            browser.get(url)
            drp = Select(browser.find_element(by=By.ID,value="pagination-dropdown"))
            drp.select_by_index(3)
            time.sleep(10)
            lists = browser.find_elements(by=By.CSS_SELECTOR,value=".vehicle-card")
            for a in range(5):
                car = dict()
                if a==0:
                    browser.find_element(by=By.CLASS_NAME,value="vehicle-card-link").click()
                    title=browser.find_element(by=By.XPATH,value="/html/body/section/div[5]/section/header/div[1]/h1").text
                    car["title"]=title

                    price=browser.find_element(by=By.XPATH,value="/html/body/section/div[5]/section/header/div[2]/span").text
                    car["price"]=price

                    titles = title.strip().split(' ')
                    car["brand"] = titles[1]

                    car["modelYear"] = titles[0]              

                    imgDiv=browser.find_element(by=By.ID,value="swipe-index-0")
                    car["img"]=imgDiv.get_attribute('src')

                    basics=browser.find_element(by=By.CLASS_NAME,value="fancy-description-list")
                    carColor=basics.text.split('\n')
                    car["color"]=carColor[1]
                    info["cars"].append(car)

                else:
                    browser.find_element(by=By.CLASS_NAME,value="srp-carousel-next-link").click()
                    title=browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[1]/h1").text
                    car["title"]=title

                    price=browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[2]/span").text
                    car["price"]=price

                    titles = title.strip().split(' ')
                    car["brand"]=titles[1]

                    car["modelYear"]=titles[0]
                    imgDiv=browser.find_element(by=By.ID,value="swipe-index-0")
                    car["img"]=imgDiv.get_attribute('src')

                    basics=browser.find_element(by=By.CLASS_NAME,value="fancy-description-list")
                    carAttributes=basics.text.split('\n')
                    car["color"]=carAttributes[1]
                    car["transmission"]=carAttributes[11]
                    info["cars"].append(car)


    return info

#browser =
#webdriver.Chrome("C:\\Users\\serkan\\Desktop\\chromedriver_win32\\chromedriver.exe")
#url = browser.get("https://www.cars.com/shopping/results/")
cars = parse_json(url)
pprint.pprint(cars)



                #payment_section = row.find("div", { "class": "payment-section" })
                #price = payment_section.find("span", { "class": "listing-rowprice" })
                #car["price"] = price.text.strip() if price else None

                #msrp = payment_section.find("span", { "class": "listing-rowmsrp" })
                #car["msrp"] = msrp.text.strip() if msrp else None

                #car["meta"] = dict()
                #meta = row.find("ul", { "class": "listing-rowmeta" }).find_all("li")
                #for meta_item in meta:
                #    meta_f = meta_item.find("strong")
                #    meta_f = meta_f.text.strip() if meta_f else None
                #    if meta_f:
                #        meta_v = meta_item.text.replace(meta_f, "").strip()
                #        car["meta"][meta_f] = meta_v

                #info["cars"].append(car)