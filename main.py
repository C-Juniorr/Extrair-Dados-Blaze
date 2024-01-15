from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from datetime import datetime, timedelta, date

url = "https://blaze.com/pt/games/double"

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def pegarsinais():
    blackk = 0
    redd = 0
    # timeout
    wait = WebDriverWait(driver, 20)

    driver.get(url)

    wait.until(presence_of_element_located((By.ID, "roulette-recent")))

    results = driver.find_elements(By.CSS_SELECTOR, "div#roulette-recent div.entry")#find_elements_by_css_selector('#roulette .sm-box .number')
    for quote in results:
        quoteArr = quote.text.split('\n')
    while True:    
            try:
                data = [my_elem.text for my_elem in driver.find_elements(By.CSS_SELECTOR, "div#roulette-recent div.entry")][:8]
            except:
                data = [my_elem.text for my_elem in driver.find_elements(By.CSS_SELECTOR, "div#roulette-recent div.entry")][:8]
            #método convertElements, converte elementos da lista em elementos declarados
            def convertElements( oldlist, convert_dict ):
                newlist = []
                for e in oldlist:
                    if e in convert_dict:
                        newlist.append(convert_dict[e])
                    else:
                        newlist.append(e)
                return newlist
                        
                    #fim do método
            try:
                data = [my_elem.text for my_elem in driver.find_elements(By.CSS_SELECTOR, "div#roulette-recent div.entry")][:8]
            except:
                data = [my_elem.text for my_elem in driver.find_elements(By.CSS_SELECTOR, "div#roulette-recent div.entry")][:8]
            colors = convertElements(data, {'':"white",'1':"red",'2':"red",'3':"red",'4':"red",'5':"red",'6':"red",'7':"red",'8':"black",'9':"black",'10':"black",'11':"black",'12':"black",'13':"black",'14':"black"})
            print(data[0:4])
            print(colors[0:4])
            time.sleep(5)

pegarsinais()
