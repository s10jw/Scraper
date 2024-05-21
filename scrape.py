import requests
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
        #url = 'https://httpbin.org/headers'
        driver.get(url)

        # Wait for the page to load and JavaScript to execute
        driver.implicitly_wait(10)

        # Extract the page source
        html = driver.page_source

        # Close the browser
        driver.quit()

        return html


# Run stuff
shadow = ShadowGovernment()

print(headers==headers2)



