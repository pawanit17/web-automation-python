# Version 1.0
# Author: Pavan Dittakavi
# About: This python script uses the selenium webdriver of Chrome browser ( version 80 )
#        does the following activities automatically.
#        1. Opens 'Wikipedia' page and searches for 'Pulp Fiction' article.
#        2. Then clicks on the Random Article functionality.
#        3. Then it opens up a new tab and loads 'Github' website.
#        4. It then searches for the text 'pawanit17' in the search bar.
#        5. From the results it would filter users with that id
#        6. It finally opens the home page of the user 'pawanit17', that's me :).
# License: Please feel free to use it per your need.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch the Chrome webdriver
# As of the time of writing this example, I am using Chrome Version 80.0.3987.149 (Official Build) (64-bit)
# Consequently, the chromedriver.exe too is based on the Chrome 80 version.
driver = webdriver.Chrome('./chromedriver.exe')

# Launch the Wikipedia web page via Chrome browser
driver.get("https://www.wikipedia.org/")

# We now are presented with the interface to select the language of our choice - we pick English.
# When the DOM is looked up in a browser, js-link-box-en uniquely identifies the button corresponding to English language.
english_version_wiki = driver.find_element_by_id('js-link-box-en')
english_version_wiki.click()

# We now assert for the presence of the text 'Wikipedia, the free encyclopedia' which signifies that we have loaded the main page for English language.
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//title[text()='Wikipedia, the free encyclopedia']")))

# Get the search box to type in our search strings.
search_text_field = driver.find_element_by_id('searchInput')
search_text_field.send_keys('Pulp Fiction')

# Click the 'Search' button to initiate the search.
driver.find_element_by_id('searchButton').click()

# Click the 'Random Page' button to initiate the search.
random_page_list_element = driver.find_element_by_id('n-randompage')
random_page_list_element.click()

# Now lets open a new tab in the same browser instance to open another webpage.
driver.execute_script("window.open('');")

# Open Github website.
driver.switch_to.window(driver.window_handles[1])
driver.get("https://github.com/")
time.sleep(3)

# Search for the user id 'pawanit17' as the search term - this involves typing and then an enter key press.
github_search_input = driver.find_element_by_xpath("//input[@type='text']")
github_search_input.send_keys('pawanit17')
github_search_input.send_keys(Keys.ENTER)

# This would search all commits, repos and users with the name 'pawanit17'.
# So we would filter the search results on 'users' criteria as shown below.
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//a[text()='Users']")))
github_search_results_user_category = driver.find_element_by_xpath("//a[text()='Users']")
github_search_results_user_category.click()

# Once we filter using the 'users' criterion, we would have users with the id as 'pawanit17'.
# There may be one or more - perhaps if their user id or name is a substring.
# We therefore identify that user whose id is case-sensitive whole-word 'pawanit17' and click it.
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//em[text()='pawanit17']")))
github_search_results_users = driver.find_element_by_xpath("//em[text()='pawanit17']")
github_search_results_users_hyperlink = github_search_results_users.find_element_by_xpath('..')
github_search_results_users_hyperlink.click()
time.sleep(3)

# Now close this second tab to close 'GitHub' page.
driver.close()
print("Welcome to my page on Github - https://github.com/pawanit17")

# Close the first tab containing the 'Wikipedia' page along with the chrome browser.
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()
