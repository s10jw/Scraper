import requests
from time import sleep
from bs4 import BeautifulSoup
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium_stealth import stealth
from chromedriver_py import binary_path
import hashlib
from useragents import AgentHandler


class ShadowGovernment:
    def __init__(self):
        self.AgentHandler = AgentHandler()
        return
    
    
    def get(self, url):
        """
        This method is presented a url string and safely returns the html content from that url as BS4 object.
        * params: url (string)
        * returns: html (string)
        """
        # ? What the hell is a reverse/forward DNS lookup
        # Set up Chrome Options
        chrome_options = webdriver.ChromeOptions()

        # Run in headless mode for automated tasks without a visible browser window
        chrome_options.add_argument("--headless")

        # Maximize the Chrome window upon startup for an optimized viewport
        chrome_options.add_argument("start-maximized")

        # Disable Chrome extensions to ensure a clean automation environment
        chrome_options.add_argument("--disable-extensions")

        # Disable sandbox mode, which can be necessary in certain environments
        chrome_options.add_argument('--no-sandbox')

        # Disable the use of the /dev/shm shared memory space, addressing potential memory-related issues
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Addresses strange third party cookie logging issue
        chrome_options.add_argument('log-level=3')

        # Set a custom user agent to simulate different browsers or devices for enhanced stealth during automation
        agent = self.AgentHandler.get_agent()
        chrome_options.add_argument('user-agent=' + agent)

        # Set up desired capabilities
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True  # Accept insecure certificates (optional)

        # Path to ChromeDriver
        service = Service(binary_path)

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Hide Selenium Attributes
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        # Open the target URL
        driver.get(url)

        # Scroll down to the bottom to load more content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the page to load and JavaScript to execute
        driver.implicitly_wait(10)

        # Extract the page source
        page_source = driver.page_source

        # Close the browser
        driver.quit()

        # Render HTML
        #html = BeautifulSoup(page_source)

        # Format HTML
        #html = html.prettify()

        return page_source


    def test_header(self):
        """
        This method retrieves current request headers from the website below and returns them to the user for inspection.
        * params: None
        * returns: None
        """
        url = 'https://httpbin.org/headers'
        html = self.get(url)
        print(html)
        return







