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
    Location = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Date = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Event_Name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Fighter_Name1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Takedowns1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Submission_Attempts1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Passes1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Weight_Class1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Method1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Round1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Time1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Result1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Height1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Weight1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Reach1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Stance1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    DOB1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes_Per_Min1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    TD_Avg1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Fighter_Name2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Takedowns2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Submission_Attempts2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Passes2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Weight_Class2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Method2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Round2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Time2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Result2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

    Height2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Weight2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Reach2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Stance2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    DOB2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Strikes_Per_Min2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    TD_Avg2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())


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
