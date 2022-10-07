#open the "https://top-movies-qhyuvdwmzt.now.sh/"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver.exe')
 
driver.get("https://top-movies-qhyuvdwmzt.now.sh/")
main_window = browser.current_window_handle
print(driver.title)


