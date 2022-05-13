from string import printable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request as request
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.pap.pl/')


cookies = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]/div/div/div/div/div/div[1]')
cookies.click()

time.sleep(1)

driver.maximize_window() 
en_language = driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/ul[2]/li[3]/a')
en_language.click()

business = driver.find_element(by=By.XPATH, value='//*[@id="block-mainnavigationen"]/ul/li[3]/a')
business.click()

titles = []

content = driver.find_elements(By.CLASS_NAME, value='title')
print(content)
print('--------------------------------')
for i in content:
    titles.append(i.find_element(by=By.XPATH, value=".//*").get_attribute('text'))


print(titles)

images = driver.find_elements(by=By.TAG_NAME, value='img')
i=0
for img in images:
    source = img.get_attribute("src")
    request.urlretrieve(source, f"photo{i}.png")
    i+=1

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get(driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a').get_attribute(name='href'))

lastpage = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a')
print(lastpage.text)


driver.quit()