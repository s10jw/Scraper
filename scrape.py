import requests
from bs4 import BeautifulSoup
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ShadowGovernment:
    def __init__(self):
        self.SCRAPEOPS_API_KEY = '57d5f60f-fbbe-49c3-8e54-c9d41b7a6475'
        return
    
    
    def get_headers_list(self):
        response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + self.SCRAPEOPS_API_KEY)
        json_response = response.json()
        return json_response.get('result', [])

    def get_header(self, header_list):
        random_index = randint(0, len(header_list) - 1)
        return header_list[random_index]

shadow = ShadowGovernment()
header_list = shadow.get_headers_list()
print(header_list[2]['user-agent'])

# result = requests.get('https://primer.ai/about-primer/careers/#openRoles', headers=header_list[0])
# print(result.text)

# URL = "https://realpython.github.io/fake-jobs/"

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
# r = requests.get('http://httpbin.org/headers', headers=header)
# print(r.text)
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="ResultsContainer")

# job_elements = results.find_all("div", class_="card-content")

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up desired capabilities
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True  # Accept insecure certificates (optional)

# Set the user-agent string
user_agent = header_list[2]['user-agent'] 
capabilities['goog:chromeOptions'] = {'args': ['--user-agent=' + user_agent]}

# Path to ChromeDriver
service = Service('/path/to/chromedriver')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the target URL
driver.get('https://primer.ai/about-primer/careers/#openRoles')

# Wait for the page to load and JavaScript to execute
driver.implicitly_wait(10)

# Extract the page source
html = driver.page_source

print(html)

# Close the browser
driver.quit()
