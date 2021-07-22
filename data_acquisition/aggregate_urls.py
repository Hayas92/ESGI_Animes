# -*- coding: utf-8 -*- #


import os
import glob
import json
import time


PATH_ANIME_LIST_COLLECTED = os.path.join(os.curdir, 'anime_list_collected')
PATH_ANIME_LIST_AGGREGATED = os.path.join(os.curdir, 'anime_list_aggregated')


def aggregate_anime_list_urls():
    """
    Gathers all the JSON files from the 'anime_list_collected' folder and will
    aggregate them into a single file which will be saved in the 'anime_list_aggregated' folder.
    """

    aggregated_anime_list_urls = []

    try:
        # Open all the json file in the folder `PATH_ANIME_LIST_COLLECTED`
        for json_file in glob.glob(os.path.join(PATH_ANIME_LIST_COLLECTED, '*.json')):
            anime_list_collected_files = json.load(open(json_file, 'r', encoding='utf-8'))
            # Save the file with series urls in one aggregated list
            for anime_list_collected_file in anime_list_collected_files:
                aggregated_anime_list_urls.append(anime_list_collected_file)
    except:
        pass

    with open(os.path.join(PATH_ANIME_LIST_AGGREGATED, str(time.strftime("%Y_%m_%d")) + '_anime_list_aggregated.json'), 'w',encoding='utf8') as file_to_dump:
        json.dump(aggregated_anime_list_urls, file_to_dump, indent=4, ensure_ascii=False)


def main():
    aggregate_anime_list_urls()


if __name__ == "__main__":
    main()