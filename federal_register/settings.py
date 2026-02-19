# Scrapy settings for federal_register project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "federal_register"

SPIDER_MODULES = ["federal_register.spiders"]
NEWSPIDER_MODULE = "federal_register.spiders"

# Crawl responsibly by identifying yourself (and obeying robots.txt)
ROBOTSTXT_OBEY = True

# Polite crawling delay (seconds)
DOWNLOAD_DELAY = 1

# Override the default request headers
DEFAULT_REQUEST_HEADERS = {
    "Accept": "application/json",
    "Accept-Language": "en",
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "federal_register.pipelines.FederalRegisterPipeline": 300,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
