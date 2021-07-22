# -*- coding: utf-8 -*- #


import os
import json
import time


PATH_ANIME_LIST_AGGREGATED = os.path.join(os.curdir, 'anime_list_aggregated')
PATH_ANIME_URLS_TO_COLLECT = os.path.join(os.curdir, 'anime_urls_to_collect')

COLLECT_DATE = '2021_07_16'


def filter_urls(urls_dicts):
    """
    Filters the urls to collect.

    # Args:
        urls_dicts: list, list of anime urls dictionaries

    # Returns:
        anime_urls_to_collect: list, animes urls to collect
    """

    # Extract the urls from the dictionaries
    urls = [url['anime_url'] for url in urls_dicts]

    # Apply the collected key
    urls_to_collect = [{'url': url, 'collected': 'no'} for url in urls]

    return urls_to_collect

def main():

    # Load the new aggregated urls
    with open(os.path.join(PATH_ANIME_LIST_AGGREGATED, str(COLLECT_DATE) + '_anime_list_aggregated.json'), encoding='utf8') as file_to_open:
        urls_dicts = json.load(file_to_open)

    # Filter the urls
    urls_to_collect = filter_urls(urls_dicts)

    # Save reviews urls
    with open(os.path.join(PATH_ANIME_URLS_TO_COLLECT, str(time.strftime("%Y_%m_%d")) + '_anime_urls_to_collect.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(urls_to_collect, file_to_dump, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
