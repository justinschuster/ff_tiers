# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from rankings.models import Ranking

import scrapy


class ScraperItem(DjangoItem):
    django_model = Ranking
