from selenium import webdriver

# This is an example #1 of web automation using selenium where we open youtube.com and search through the search bar

# creates a new instance of the chromedriver(which needs to be installed separately and moved to path folder)
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")

# the xpath of the HTML element of the search bar on youtube is passed as a argument
search_bar = driver.find_element_by_xpath('//*[@id="search"]')
# search_bar object allows us to type in the youtube search bar through send_keys(<what you want to search>)
search_bar.send_keys("Formula 1")

# the xpath of the HTML element of the search button on youtube is passed as a argument
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
