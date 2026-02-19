# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExecutiveOrderItem(scrapy.Item):
    """Item representing a Federal Register Executive Order."""
    Title = scrapy.Field()
    Date = scrapy.Field()
    Document_Number = scrapy.Field()
    URL = scrapy.Field()
