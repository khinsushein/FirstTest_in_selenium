# Search for A New and verify that all the titles displayed contain the search phrase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
from time import sleep
import org.openqa.selenium.WebElement
import Xpath
from selenium.common.exceptions import NoSuchElementException


def test_basic_search(browser):
  # Set up some test case data
  URL = 'https://top-movies-qhyuvdwmzt.now.sh'
  PHRASE3 = 'God the Father'
  bodyText = self.driver.find_element_by_tag_name('PHRASE3').text

  # Navigate to the 'God the Father'page
  browser.get(URL)

  # Find the search input element
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE3 + Keys.RETURN)

  # Search "God the Father"on the current page
  driver.implicitly_wait(20)


#identify element
l= driver.find_elements_by_css_selector("God the Father")
#get list size with len
s = len(l)
# check condition, if list size > 0, element exists
if(s>0):
   m= l.text 
print("Element exist -" + m)
if(s<0):
  print("Element does not exist")
driver.close()

