from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("download.default_directory=C:/Ai-Scraping")

driver = webdriver.Chrome(options=options)


driver.get('https://v24.www-ytmp4.com')


element = driver.find_element(By.XPATH, '//input[@id="input"]')

element.send_keys('https://youtu.be/dQw4w9WgXcQ?si=u2VkmDzC-oXxU_yy')


driver.find_element(By.XPATH, '//input[@id="submit"]').click()



url = driver.find_element(By.XPATH, "//iframe[@id='buttonApi']").get_attribute('src')

driver.get(str(url))

time.sleep(2)
videoButton = driver.find_element(By.XPATH, '//button[contains(text(), "Video")]')

videoButton.click()

time.sleep(2)

downloadButton = driver.find_element(By.XPATH, '//tr[2]//a[contains(text(), " Download")]')

downloadButton.click()

time.sleep(15)

downloadButton2 = driver.find_element(By.XPATH, '//span[contains(text(), "Download")]')


downloadButton2.click()
time.sleep(5)
print(driver.current_url)
time.sleep(15)


