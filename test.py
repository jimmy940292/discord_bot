from opgg.v2.opgg import OPGG
from opgg.v2.params import Region
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse

def main():
    # opgg = OPGG()
    # results = opgg.search("FW NL#2015", Region.TW)
    # [print(result) for result in results]
    
    id = 'FW NL#2015'
    id = id.replace('#', '-')
    id = urllib.parse.quote(id)
    
    options = Options()
    options.headless = True
    # Disable images for faster loading
    prefs = {"profile.managed_default_content_settings.images": 2,"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument('--headless')
    # options.headless = True
    
    url = f"https://www.op.gg/summoners/tw/{id}"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    driver.quit()
    
    try:
        stats = soup.find(class_='css-1egz98l').find(class_='stats').find(class_='win-lose')
        print(stats.text)
    except:
        print('')

    


if __name__ == "__main__":
    main()