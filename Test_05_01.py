#Search for A New and verify that all the titles displayed contain the search phrase

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
from selenium.webdriver.remote.webelement import WebElement


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
  PHRASE3 = 'A New'

  # Navigate to the home page
  browser.get(URL)

  # Find the search input element
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE3 + Keys.RETURN)

  # Verify that results appear on the results page 
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0
  sleep (20)
  
  List<WebElement> listElement = driver.findElements(By.className("PHRASE3"));
      for(int i =0;i<listElement.size();i++) {
             String elementText = listElement.get(i).getText(); 
             System.out.println(elementText); 
}