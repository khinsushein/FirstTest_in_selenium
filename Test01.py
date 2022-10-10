#open the "https://top-movies-qhyuvdwmzt.now.sh/" in Chrome
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
# open in Chrome browser
driver.get("https://top-movies-qhyuvdwmzt.now.sh/")
# Title of the page
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#close the browser
driver.close()

