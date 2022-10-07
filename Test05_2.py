#Take any movie you like and make sure the Released on, popularity, vote average and votecount fields have the expected values

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep


def browser():
  # Initialize ChromeDriver
  driver = Chrome()

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()


def test_basic_search(browser):
  # Set up some test case data
  URL = 'https://top-movies-qhyuvdwmzt.now.sh'
  PHRASE4 = 'The Godfather'

  # Navigate to the The Shawshank Redemption home page
  browser.get(URL)

  # Find the search input element
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE4 + Keys.RETURN)

  # Verify that results appear on the results page (in an new tap) 
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0

  # Verify that at least one search result contains the search phrase
  xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE4}')]"
  phrase4_results = browser.find_elements_by_xpath(xpath)
  assert len(phrase4_results) > 0

  # Verify that the search phrase is the same
  search_input = browser.find_element_by_id('search_form_input')
  assert search_input.get_attribute('value') == PHRASE4
  #Wait implicitly for elements to be ready before attempting interactions
  sleep(10)
  #Checking teh Released date visually 
  LearnMore = driver.find_element(By.CSS_SELECTOR, "LEARN MORE")
  sleep(10)
  print ('LEARN MORE:', LearnMore.text)
 
  
  



