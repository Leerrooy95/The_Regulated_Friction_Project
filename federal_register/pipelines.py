# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FederalRegisterPipeline:
    """Default pipeline for processing Executive Order items."""

    def process_item(self, item, _spider):
        return item
