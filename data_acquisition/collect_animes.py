# -*- coding: utf-8 -*- #
import os
import time
import json
import random

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from data_collector import collect_anime_data


# Import PATH
PATH_ANIMES_DATA = os.path.join(os.curdir, 'animes_data')
PATH_ANIMES_EPISODES_DATA = os.path.join(os.curdir,'animes_episodes_data')
PATH_ANIME_URLS_TO_COLLECT = os.path.join(os.curdir, 'anime_urls_to_collect')
PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'
#PATH_DRIVER = r'D:\Users\Tenma\Documents\chromedriver_win32\chromedriver.exe'
#PATH_DRIVER = r'D:\Ouss\projet_allocine-main\packages.exe'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")

COLLECT_DATE = '2021_07_21'


def main():
    anime_urls_to_collect = json.load(open(os.path.join(PATH_ANIME_URLS_TO_COLLECT, COLLECT_DATE + '_anime_urls_to_collect.json'), 'r'))

    for anime_id, anime_url in enumerate(anime_urls_to_collect):

        # Select the url under specific conditions
        if anime_url['collected'] == 'no':

            # Load the driver for every new page
            driver = webdriver.Chrome(PATH_DRIVER, options=CHROME_OPTIONS)

            print('[LOG] Current url:', anime_url['url'])
            print('[LOG] Datetime:', time.strftime("%Y_%m_%d_%H_%M_%S"))

            try:
                # Load the url with the driver
                driver.get(anime_url['url'])

                # Wait for the page to load correctly
                time.sleep(random.uniform(1, 3))

                # Collect and save the anime data
                anime_data, episodes_dict = collect_anime_data(driver, anime_url['url'],anime_id)

                # Change the status of the current url and save it.
                # The current anime url has a name (therefore data has been collected).
                if anime_data["anime_name"]:

                    with open(os.path.join(PATH_ANIMES_DATA, COLLECT_DATE + '_anime_data_' + str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '.json'), 'w', encoding='utf-8') as file_to_dump:
                        json.dump(anime_data, file_to_dump, indent=2, ensure_ascii=False)
                    with open(os.path.join(PATH_ANIMES_EPISODES_DATA,str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '_anime_data.json'), 'w',encoding='utf-8') as file_to_dump:
                        json.dump(episodes_dict, file_to_dump, indent=4, ensure_ascii=False)
                    # The url is set as 'yes'.
                    anime_url['collected'] = 'yes'
                    print("[LOG] All the anime's data have been collected for the current url")

                    with open(os.path.join(PATH_ANIME_URLS_TO_COLLECT, COLLECT_DATE + '_anime_urls_to_collect.json'),'w') as file_to_dump:
                        json.dump(anime_urls_to_collect, file_to_dump, indent=2, ensure_ascii=False)

                else:
                    # If the page data didn't load
                    # The collect for the current url has raised some errors.
                    # The url is set as 'issue'.
                    anime_url['collected'] = 'issue'
                    print('[LOG] Issue with the current url. Saved as url with issues.')

                    with open(os.path.join(PATH_ANIME_URLS_TO_COLLECT, COLLECT_DATE + '_anime_urls_to_collect.json'),'w') as file_to_dump:
                        json.dump(anime_urls_to_collect, file_to_dump, indent=2, ensure_ascii=False)

            except:
                # The collect for the current url has raised some errors.
                # The url is set as 'issue'.
                anime_url['collected'] = 'issue'
                print('[LOG] Issue with the current url. Saved as url with issues.')

                with open(os.path.join(PATH_ANIME_URLS_TO_COLLECT, COLLECT_DATE + '_anime_urls_to_collect.json'),'w') as file_to_dump:
                    json.dump(anime_urls_to_collect, file_to_dump, indent=2, ensure_ascii=False)

            # Delete the cookies and quit the driver
            driver.delete_all_cookies()
            driver.quit()


if __name__ == "__main__":
    main()