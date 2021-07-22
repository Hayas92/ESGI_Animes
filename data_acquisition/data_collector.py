#!/usr/bin/env python
import uuid
import time
import itertools
import random
def init_anime_dict():

    """
    Initializes the dictionary with the anime data.
    Return:
        init_anime_dict: dict, dictionary with the anime data.
    """

    anime_dict = {
        'anime_id': None,
        'anime_url': None,
        'anime_name': None,
        'anime_language': None,
        'anime_mean_rating': None,
        'authors': None,
        'anime_type': None,
        'anime_kind': None,
        'animation_studio': None,
        'year_of_production': None,
        'n_episodes': None,
        'status': None,
        'synopsis': None,
        'collect_date': str(time.strftime("%Y_%m_%d")),
    }

    return anime_dict
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def collect_anime_data(driver, url, anime_id):
    """
    Collects the data of the anime url.
    # Args:
        driver: selenium driver
        url: str, url of a product.
    # Return:
        anime_dict: dict, dictionary with anime's data.
    """

    anime_dict = init_anime_dict()

    anime_information = driver.find_element_by_class_name('entry-content').text
    episodes_dict = []
    # Anime's url

    try:
        anime_dict['anime_id'] = anime_id
    except:
        pass

    try:
        anime_dict['anime_url'] = url
    except:
        pass

    # Anime's name
    try:
        anime_dict['anime_name'] = driver.find_element_by_class_name('entry-title').text.strip()
    except:
        pass

    # Anime's language
    try:
        if anime_dict['anime_url'].find('vf')> 0:
            anime_dict['anime_language'] = "VF"
        else:
            anime_dict['anime_language'] = "VOSTFR"
    except:
        pass

    # Anime's mean rating
    try:
        anime_dict["anime_mean_rating"] = driver.find_element_by_class_name('post-ratings').find_element_by_tag_name('img').get_attribute('onmouseout').split(';')[-2].replace('ratings_off(','').split(',')[0].strip()
    except:
        pass

    # Authors
    try:
        try:
            anime_dict['authors'] = anime_information.split('Auteur:')[1].split('\n')[0].strip()
        except:
            anime_dict['authors'] = anime_information.split('Auteurs:')[1].split('\n')[0].strip()
    except:
        pass

    # Anime's type
    try:
        anime_dict["anime_type"] = anime_information.split('Type:')[1].split('\n')[0].strip()
    except:
        pass

    # Anime's kind
    try:
        anime_dict['anime_kind'] = anime_information.split('Genre:')[1].split('\n')[0].strip()
    except:
        pass

    # Animation studio
    try:
        anime_dict['animation_studio'] = anime_information.split('Studio d’animation:')[1].split('\n')[0].strip()
    except:
        pass

    # Year of production
    try:
        anime_dict['year_of_production'] = anime_information.split('Année de production:')[1].split('\n')[0].strip()
    except:
        pass

    # Number of episodes
    try:
        anime_dict['n_episodes'] = anime_information.split('Durée:')[1].split('\n')[0].split("épisode")[0].strip()
    except:
        pass

    # Status
    try:
        anime_dict['status'] = anime_information.split('Statut:')[1].split('\n')[0].strip()
    except:
        pass

    # Synopsis
    try:
        anime_dict['synopsis'] = driver.find_element_by_class_name('entry-content').find_element_by_tag_name('h5').get_attribute('textContent').replace('Synopsis:','').strip()
    except:
        pass

    # Episodes
    try:
        for episode_list in driver.find_element_by_class_name('entry-content').find_elements_by_tag_name('p'):
            episodes = episode_list.find_elements_by_tag_name('a')
            episodes_dict += ([{'episode_id': str(uuid.uuid1()) ,
                                'anime_url': anime_dict['anime_url'],
                                'episode_name': episode.get_attribute('textContent').strip(),
                                'episode_url': episode.get_attribute('href')}
                                for episode in episodes if episode.get_attribute('textContent').strip() != ""])
    except:
        pass

    return anime_dict, episodes_dict
