from django.db import models


class Anime(models.Model):
	id = models.AutoField(primary_key=True)
	anime_url = models.URLField('Url', blank=True)
	anime_name = models.CharField('Nom',max_length=300)
	anime_language = models.CharField('Langue', max_length=15)
	anime_mean_rating = models.CharField('Note', max_length=25)
	authors = models.CharField('Auteurs', max_length=300)
	anime_type = models.CharField('Type', max_length=300)
	anime_kind = models.CharField('Genre', max_length=300)
	animation_studio = models.CharField("Studio d'animation", max_length=300)
	year_of_production = models.CharField('Année de production', max_length=300)
	n_episodes = models.CharField("Nombre d'épisodes", max_length=300)
	status = models.CharField('Statut', max_length=300)
	synopsis = models.TextField('Synopsis', blank=True)
	collect_date = models.CharField('Date de collecte', max_length=300)

	def __str__(self):
		return self.anime_name


class Episode(models.Model):
	id = models.AutoField(primary_key=True)
	anime_url = models.URLField("Url de l'animé", blank=True)
	episode_name = models.CharField('Nom', max_length=120)
	episode_url = models.URLField("Url de l'épisode", blank=True)

	def __str__(self):
		return self.episode_name
