# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
#

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_whitespace(value):
    return value.strip()


class UfcStats(scrapy.Item):
    Fighter_Name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Takedowns = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Submission_Attempts = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Passes = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Weight_Class = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Method = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Round = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Time = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Result = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Location = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Date = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Event_Name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    
    Height = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Weight = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Reach = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Stance = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    DOB = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes_Per_Min = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    TD_Avg = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())


class JokeItem(scrapy.Item):
    joke_text = scrapy.Field(input_processor=MapCompose(remove_tags, remove_whitespace), output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(remove_tags, remove_whitespace), output_processor=TakeFirst())


class SephoraItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    popularity = scrapy.Field()
