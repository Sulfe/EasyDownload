from numpy import integer
from regex import R
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

def googleColling(optionPhoto):
    searchName = optionPhoto[0]
    searchEngine = optionPhoto[1]
    searchDriver = optionPhoto[2]
    searchPath = optionPhoto[3]
    searchNum = optionPhoto[4]
    
    # Option to not show chrome/크롬을 띄우지 않는 옵션 설정
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(str(searchDriver),options=options) ##바꾸기 자신의 경로로##
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(str(searchName))
    elem.send_keys(Keys.RETURN)

    
    outpath = str(searchPath) + '/'   ##바꾸기 자신의 경로로##

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(10)
            imgUrl = driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            outfile = str(count) + ".jpg"
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, outpath + outfile)
            count = count + 1
            if count == (integer(searchNum)+1):
                break
            
        except:
            pass

    driver.close();