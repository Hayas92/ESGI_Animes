#!/usr/bin/env python


import os
import glob
import json
import time


PATH_ANIMES_DATA = os.path.join(os.curdir, 'animes_data')
PATH_ANIMES_EPISODES_DATA = os.path.join(os.curdir,'animes_episodes_data')

PATH_MERGED_ANIMES_DATA = os.path.join(os.curdir, 'merged_animes_data')
PATH_MERGED_ANIMES_EPISODES_DATA = os.path.join(os.curdir, 'merged_animes_episodes_data')

COLLECT_DATE = '2021_07_21'


def aggregate_files():
    """
    Aggregates the collected animes data files.
    """

    # Merge anime data files
    anime_data_files = []
    try:
        for product_file in glob.glob(os.path.join(PATH_ANIMES_DATA, '*.json')):
            anime_data_files.append(json.load(open(product_file, 'r',encoding='utf8')))
    except:
        pass

    with open(os.path.join(PATH_MERGED_ANIMES_DATA, DATE_COLLECT + '_animes_data_aggregated' + '.json'), 'w',encoding='utf-8') as file_to_dump:
        json.dump(anime_data_files, file_to_dump, indent=2, ensure_ascii=False)

    # Merge anime episodes data files
    anime_episodes_data_files = []
    try:
        for product_file in glob.glob(os.path.join(PATH_ANIMES_EPISODES_DATA, '*.json')):
            anime_episodes_data_files.append(json.load(open(product_file, 'r', encoding='utf8')))
    except:
        pass

    # Convert nested list to flat list
    flatList = [item for elem in anime_episodes_data_files for item in elem]

    with open(os.path.join(PATH_MERGED_ANIMES_EPISODES_DATA, DATE_COLLECT + '_animes_episodes_data_aggregated' + '.json'), 'w',
              encoding='utf-8') as file_to_dump:
        json.dump(flatList, file_to_dump, indent=2, ensure_ascii=False)


def main():
    aggregate_files()


if __name__ == "__main__":
    main()
