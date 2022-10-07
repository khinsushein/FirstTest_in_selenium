#Retrieve the url of the image and open it in another tab then close the tab.


from selenium.webdriver import Chrome
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


def test_basic_duckduckgo_search(browser):
  # Set up some test case data
  URL = 'https://top-movies-qhyuvdwmzt.now.sh'
  PHRASE2 = 'The Godfather Part II'

  # Navigate to the The Shawshank Redemption home page
  browser.get(URL)

  # Find the search input element
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE2 + Keys.RETURN)

  # Verify that results appear on the results page (in an new tap) 
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0
  sleep (20)
  # Close current tab and return to the original page
  driver.navigate().to("url")

  
  
  



