from selenium import webdriver
import time

# somethimes if using local ide you may need to do the following:
# from selenium.webdriver.chrome.service import Service
# service = Service("/users/sashagoldin/path/to/chromedriver/mayneed to downaload it first") and then add positional argument in   
#  driver = webdriver.Chrome(service = service, options=options)

def get_driver():  
# Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars") # disables the infobars
  options.add_argument("start-maximized") # start browser in maximized mode
  options.add_argument("disable-dev-shm-usage") # To avoid issues with linux
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disbale-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())