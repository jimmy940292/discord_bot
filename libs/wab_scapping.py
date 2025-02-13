from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse


# find class in response
# def processData()

# Get data from OPGG
def getDataFromOpgg(id: str) -> str:

    # Convert space and '#'
    id = id.replace('#', '-')
    id = urllib.parse.quote(id)
    
    options = Options()
    options.headless = True
    
    # Disable images for faster loading
    prefs = {"profile.managed_default_content_settings.images": 2,"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs", prefs)
    
    url = f"https://www.op.gg/summoners/tw/{id}"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    driver.quit()
    
    try:
        stats = soup.find(class_='css-1egz98l').find(class_='stats').find(class_='win-lose')
        # print(stats.text)
        return stats.text
    except:
        return ''
    
    
    
    

