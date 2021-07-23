# -*- coding: utf-8 -*- #

import json
import os
import time
import random

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from data_collector import collect_anime_data

# Import PATH
PATH_ANIME_DATA = os.path.join(os.curdir, 'anime_data')
PATH_ANIME_EPISODES_DATA = os.path.join(os.curdir,'anime_episodes_data')
PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'
#PATH_DRIVER = r'D:\Users\Tenma\Documents\chromedriver_win32\chromedriver.exe'
#PATH_DRIVER = r'D:\Ouss\projet_allocine-main\packages.exe'

# Chromedriver options
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")

COLLECT_DATE = '2021_07_21'


def main():

    # Select the url
    url = "https://gum-gum-streaming.com/d-frag-vostfr/"
    # Load the driver
    driver = webdriver.Chrome(PATH_DRIVER, options=CHROME_OPTIONS)
    anime_id = 54
    # Load the url with the driver
    driver.get(url)

    # Wait for the page to load correctly
    time.sleep(random.uniform(1,3))

    # Collect data
    anime_data, episodes_dict = collect_anime_data(driver, url,anime_id)

    # Save anime information
    print(anime_data)

    with open(os.path.join(PATH_ANIME_DATA, str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '_anime_data.json'), 'w',encoding='utf-8') as file_to_dump:
        json.dump(anime_data, file_to_dump, indent=4, ensure_ascii=False)

    # Save anime's episodes information

    print(episodes_dict)

    with open(os.path.join(PATH_ANIME_EPISODES_DATA, str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '_anime_data.json'), 'w', encoding ='utf-8') as file_to_dump:
        json.dump(episodes_dict, file_to_dump, indent=4, ensure_ascii=False)

    # Delete the cookies and quit the driver
    driver.delete_all_cookies()
    driver.quit()


if __name__ == "__main__":
    main()