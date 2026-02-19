"""Spider to scrape Executive Orders from the Federal Register.

Target: https://www.federalregister.gov/presidential-documents
Data source: Federal Register public API (no key required)
Extracts: Title, Date, Document_Number, URL for each Executive Order.
"""

import json

import scrapy

from federal_register.items import ExecutiveOrderItem


class FederalRegisterEOSpider(scrapy.Spider):
    """Scrape Executive Orders from the Federal Register daily list."""

    name = "federal_register_eo"
    allowed_domains = ["federalregister.gov", "www.federalregister.gov"]

    # The Federal Register provides a public JSON API for document access.
    # This is the recommended programmatic interface for the presidential
    # documents page at https://www.federalregister.gov/presidential-documents
    API_BASE = (
        "https://www.federalregister.gov/api/v1/documents.json"
        "?conditions[presidential_document_type]=executive_order"
        "&conditions[type][]=PRESDOCU"
        "&fields[]=title"
        "&fields[]=publication_date"
        "&fields[]=document_number"
        "&fields[]=html_url"
        "&per_page=20"
        "&order=newest"
    )

    def start_requests(self):
        yield scrapy.Request(url=self.API_BASE, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for doc in data.get("results", []):
            item = ExecutiveOrderItem()
            item["Title"] = doc.get("title")
            item["Date"] = doc.get("publication_date")
            item["Document_Number"] = doc.get("document_number")
            item["URL"] = doc.get("html_url")
            yield item

        # Follow pagination
        next_page = data.get("next_page_url")
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
