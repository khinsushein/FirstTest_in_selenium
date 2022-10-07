#First Contact is displayed inthe search results and the movie The Shawshank Redemption is no longer visible
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import selenium.webdriver as webdriver
driver = webdriver.Chrome('./chromedriver.exe')
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import org.openqa.selenium.WebElement
import Xpath
from selenium.common.exceptions import NoSuchElementException

def test_basic_search(browser):
  # Set up some test case data
  URL = 'https://top-movies-qhyuvdwmzt.now.sh'
  PHRASE2 = 'Star Trek:'
  bodyText = self.driver.find_element_by_tag_name('PHRASE2').text

  # Navigate to the The Shawshank Redemption home page
  browser.get(URL)

  # Find the search input element
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE2 + Keys.RETURN)

  # Search "Star Trek: First Contact"on the current page
  driver.implicitly_wait(20)


#identify element
l= driver.find_elements_by_css_selector("The Shawshank Redemption")
#get list size with len
s = len(l)
# check condition, if list size > 0, element exists
if(s>0):
   m= l.text 
print("Element exist -" + m)
if(s<0):
  print("Element does not exist")
driver.close()

