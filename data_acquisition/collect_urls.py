#!/usr/bin/env python


import json
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Import PATH
PATH_ANIME_LIST = os.path.join(os.curdir, 'anime_list_collected')
PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'
#PATH_DRIVER = r'D:\Users\Tenma\Documents\chromedriver_win32\chromedriver.exe'
#PATH_DRIVER = r'D:\Ouss\projet_allocine-main\packages.exe'

# Chromedriver options
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")


def init_url_dict():
    """
    Initializes the dictionary with the information of an anime (name and url)
    Return:
       url_dict: dict, dictionary with the anime data.
    """
    url_dict = {
        'id_product': None,
        'anime_name': None,
        'anime_url': None,
        'anime_language': None,
        'collect_date': str(time.strftime("%Y_%m_%d")),
    }

    return url_dict


def collect_url_dict(driver,url):
    """
    Collects all the animes on the anime list page.

    # Args:
        driver: selenium driver.
        url: str, url of the anime list page.

    # Return:
        urls_dicts: list, list of dictionaries with anime's data.
    """

    urls_dicts = []

    # Load all the animes on the page
    animes = driver.find_element_by_class_name('entry-content').find_elements_by_tag_name('h2')

    # For each anime we save a dictionary
    for id_anime, anime in enumerate(animes):

        url_dict = init_url_dict()

        # Anime's id
        try:
            url_dict['id_product'] = id_anime + 1
        except:
            pass

        # Anime's name
        try:
            url_dict['anime_name'] = anime.find_element_by_tag_name('a').get_attribute('textContent').strip()
        except:
            pass

        # Anime's url
        try:
            url_dict['anime_url'] = anime.find_element_by_tag_name('a').get_attribute('href')
        except:
            pass

        # Anime's language
        try:
            if url.find('vf') >0:
                url_dict['anime_language'] = "VF"
            else:
                url_dict['anime_language'] = "VOSTFR"
        except:
            pass

        urls_dicts.append(url_dict)

    return urls_dicts


def main():
    # Urls on which the anime list is located
    urls = ["https://gum-gum-streaming.com/vostfr/##",
            "https://gum-gum-streaming.com/vf/##"]

    for url in urls:
        print('[LOG] Current url =', url)

        # Load the driver for the url
        driver = webdriver.Chrome(PATH_DRIVER, options=CHROME_OPTIONS)
        driver.get(url)

        # Wait for the page to load correctly
        time.sleep(random.uniform(1, 3))

        # Collect the anime list and save it in a json file
        try:
            urls_dicts = collect_url_dict(driver,url)
            with open(os.path.join(PATH_ANIME_LIST, str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '_anime_list_collected.json'),
                    'w', encoding='utf-8') as file_to_dump:
                json.dump(urls_dicts, file_to_dump, indent=4, ensure_ascii=False)

            print('[LOG] All the urls have been saved for the current url.')
        except:
            print('[LOG] There is an issue with the current url. The urls have not been saved.')

        # Delete the cookies and quit the driver
        driver.delete_all_cookies()
        driver.quit()


if __name__ == "__main__":
    main()
