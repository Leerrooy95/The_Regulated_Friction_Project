# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExecutiveOrderItem(scrapy.Item):
    """Item representing a Federal Register Presidential Document."""
    Title = scrapy.Field()
    Date = scrapy.Field()
    Document_Number = scrapy.Field()
    URL = scrapy.Field()
    Subtype = scrapy.Field()
    Capital_Leverage_Keywords = scrapy.Field()  # Track B keywords matched (Section 122, etc.)


class DOJPressReleaseItem(scrapy.Item):
    """Item representing a DOJ press release."""
    Title = scrapy.Field()
    Date = scrapy.Field()
    URL = scrapy.Field()
    UUID = scrapy.Field()
    Number = scrapy.Field()
    Component = scrapy.Field()
    Topic = scrapy.Field()
    Capital_Leverage_Keywords = scrapy.Field()  # Track B keywords matched (Section 122, etc.)
