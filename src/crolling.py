from numpy import integer
from regex import R
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

def action(searchName,searchEngine,searchDriver,searchPath,searchNum):
    google = 'Google'
    #searchName = optionPhoto[0]
    #searchEngine = optionPhoto[1]
    #searchDriver = optionPhoto[2]
    #searchPath = optionPhoto[3]
    #searchNum = optionPhoto[4]
    if searchEngine==google:
        value = googleCrolling(searchName,searchDriver,searchPath,searchNum)
        return value
    else :
        value = naverCrolling(searchName,searchDriver,searchPath,searchNum)
        return value

def googleCrolling(searchName,searchDriver,searchPath,searchNum):
    # Option to not show chrome/크롬을 띄우지 않는 옵션 설정
    print('다운로드를 시작합니다.')
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(str(searchDriver),options=options) ##바꾸기 자신의 경로로##
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(str(searchName))
    elem.send_keys(Keys.RETURN)
    outpath = str(searchPath)+'/'   ##바꾸기 자신의 경로로##
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
            time.sleep(5)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            outfile =str(count)+'.jpg'
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, outpath + outfile)
            count = count + 1
            if count == (int(searchNum)+1):
                break
            
        except:
            pass

    driver.close();
    return '다운로드 종료'



def naverCrolling(searchName,searchDriver,searchPath,searchNum):
    print('다운로드를 시작합니다.')
    # Option to not show chrome/크롬을 띄우지 않는 옵션 설정
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(str(searchDriver),options=options) ##바꾸기 자신의 경로로##
    driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
    elem = driver.find_element_by_name("query")
    elem.send_keys(str(searchName))
    elem.send_keys(Keys.RETURN)

    
    outpath = str(searchPath)+'/'   ##바꾸기 자신의 경로로##

    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector('._image._listImage')
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(5)
            imgUrl = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            outfile = str(count) + ".jpg"
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, outpath + outfile)
            count = count + 1
            if count == (int(searchNum)+1):
                break
            
        except:
            pass

    driver.close();
    return '다운로드 종료'