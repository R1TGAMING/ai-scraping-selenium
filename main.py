from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
#you can use --headless for environment
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("download.default_directory=C:/home/runner/Ai-Scraping") # change it to your directory downloading

try :
#the driver change it to your driver
 driver = webdriver.Chrome(options=options)

#get the base url 
 driver.get('https://v24.www-ytmp4.com')


#find the search box and enter the search query
 element = driver.find_element(By.XPATH, '//input[@id="input"]')

 element.send_keys('https://youtu.be/dQw4w9WgXcQ?si=u2VkmDzC-oXxU_yy') #change the link

 driver.find_element(By.XPATH, '//input[@id="submit"]').click()


#search for the video and get the API url
 url = driver.find_element(By.XPATH, "//iframe[@id='buttonApi']").get_attribute('src')

 driver.get(str(url))
 time.sleep(2)

#find the download button and then click it
 videoButton =  driver.find_element(By.XPATH, '//button[contains(text(), "Video")]')
 videoButton.click()
 time.sleep(2)

 downloadButton =  driver.find_element(By.XPATH, '//tr[4]//a[contains(text(), " Download")]') # you can change tag tr for resolution
 downloadButton.click()
 time.sleep(25)

 downloadButton2 = driver.find_element(By.XPATH, '//span[contains(text(), "Download")]')
 downloadButton2.click()
 time.sleep(5)

#close the browser
 driver.quit()
  
except Exception as e :
  print(e)