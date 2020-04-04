# Web Automation with Python
This project is about automating munda web related tasks using Python selenium driver. I orignally used Python for my office work where I used it to open a web page, search for the input user and kill his session with the web server. This really worked out well and so thought that I would also do it for another usecase to serve as an example.

## Introduction 
In this case, I used Python for opening up Chrome and then visiting wikipedia web page. I then search for the article 'Pulp Fiction' and then click on the 'Random Page' generator link. Then I open a new tab and I open GitHub and search my id 'pawanit17' and eventually visit my profile page. Once done, I close the opened two tabs and then close the browser.

### Selenium & the WebDriver
Selenium is a project for supporting the automation of web browsers to do specific programmer defined tasks. Selenium WebDriver is an interface which can take instructions to run on corresponding browsers. For more information, please do visit the official website here: https://www.selenium.dev/documentation/en/

The webdrivers are found in the form of an executable on the internet. For example: https://chromedriver.chromium.org/downloads lists the Chrome webdrivers for the different versions.

### Python integration for Selenium WebDriver
Python has bindings for Selenium WebDriver. So using Python we can write some instructions which are to be performed by the driver.
https://pypi.org/project/selenium/

## Project set up
- Download Python from https://www.python.org/downloads/
- Download Pycharm Community Edition from https://www.jetbrains.com/pycharm/download/
- Install Selenium package for Python using the below command
   ```bash
   pip install selenium
   ```
- Download the Python webdriver for Chrome from https://chromedriver.chromium.org/downloads
- Download Pyinstaller using teh below command
   ```bash
   pip install PyInstaller
   ```
 
## Automating an activity on a website
The following steps are the main action sequences for realizing an automation with Python

### Loading the webdriver and opening the Chrome Application
   ```bash
driver = webdriver.Chrome('./chromedriver.exe') # I had the exe on the same location as the python script.
   ```

### Opening the Wikipedia web page
   ```bash
driver.get("https://www.wikipedia.org/")
   ```
   
### Language seletion on the Wikipedia page
   ```bash
english_version_wiki = driver.find_element_by_id('js-link-box-en')
english_version_wiki.click()
   ```
   
### Web Page Load Wait
   ```bash
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//title[text()='Wikipedia, the free encyclopedia']")))
   ```
   
### Enter Search Criterion & Searching
   ```bash
search_text_field = driver.find_element_by_id('searchInput')
search_text_field.send_keys('Pulp Fiction')
driver.find_element_by_id('searchButton').click()
   ```
   
### Opening a new tab in Chrome & switching focus to it
   ```bash
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://github.com/")
   ```
   
### Closing second tab & the main tab - close of Chrome application itself.
   ```bash
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
   ```
   
## Tip
- The key to successful automation involves looking up the HTML DOM and understanding how to recognise the elements like Search Boxes and Buttons.
  - Debugger is your friend.
- Sometimes the script would not be able to detect elements although you know they exist. This could most likely be because the HTML DOM is still loading and is not finised yet. In this case, use WebDriverWait to your advantage as described above.
- Chrome Driver in my experience was the easiest to set up and confiure. Simply do a Help->About Chrome to understand the version and download the corresponding driver version.
- Internet explore is the trickiet of them all. Most of the developers are getting this error almost consistently
*Enable Protected Mode must be set to the same value (enabled or disabled) for all zones.*
  - There are a wide variety of solutions available for this like configuring the flags like *ignoreProtectedModeSettings*, configuring *DesiredCapabilities* etc. But for my prototype that I did for my company, I just ensured that the *Internet Options -> Security -> Enable Protection Mode* checkbox to be aligned the same way for the different Zones ( Internet, Local Intranet, Trusted Sites, Restricted Sites ) etc.
- Finally, the IE webdrivers can be found here: https://www.selenium.dev/downloads/ and if you notice that the key typein onto the text fields is slow, try switching from 32 bit drivers to 64 bit drivers or vice-versa.
  - In my case, I had to swap the 64 bit driver with the 32 bit driver.

