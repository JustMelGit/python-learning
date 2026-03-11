# from selenium import webdriver
DRIVER_PATH = r'C:\Users\Justice\Downloads\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.nintendo.com/")
print(driver.page_source)
driver.quit()
