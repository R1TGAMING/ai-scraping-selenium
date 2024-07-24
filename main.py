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

driver = webdriver.Chrome(options=options)


driver.get('https://v24.www-ytmp4.com')


element = driver.find_element(By.XPATH, '//input[@id="input"]')

element.send_keys('https://youtu.be/dQw4w9WgXcQ?si=u2VkmDzC-oXxU_yy')


submit = driver.find_element(By.XPATH, '//input[@id="submit"]').click()

driver.execute_script("window.scrollTo(0, 400);")

time.sleep(5)

url = driver.find_element(By.XPATH, "//iframe[@id='buttonApi']").get_attribute('src')

driver.get(url)

time.sleep(5)