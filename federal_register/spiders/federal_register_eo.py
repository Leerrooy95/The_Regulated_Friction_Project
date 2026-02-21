"""Spider to scrape Presidential Documents from the Federal Register.

Target: https://www.federalregister.gov/presidential-documents
Data source: Federal Register public API (no key required)
Extracts: Title, Date, Document_Number, URL, Subtype for each document.
Document types: Executive Orders, Proclamations, and Notices.

Filters to the last 7 days of publications.
"""

import json
from datetime import datetime, timedelta

import scrapy

from federal_register.items import ExecutiveOrderItem


class FederalRegisterEOSpider(scrapy.Spider):
    """Scrape Executive Orders, Proclamations, and Notices from the Federal Register (last 7 days)."""

    name = "federal_register_eo"
    allowed_domains = ["federalregister.gov", "www.federalregister.gov"]

    def start_requests(self):
        # Calculate date range: last 7 days
        end_date = datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        
        # Build API URL with date filter
        api_url = (
            "https://www.federalregister.gov/api/v1/documents.json"
            "?conditions[presidential_document_type][]=executive_order"
            "&conditions[presidential_document_type][]=proclamation"
            "&conditions[presidential_document_type][]=notice"
            "&conditions[type][]=PRESDOCU"
            f"&conditions[publication_date][gte]={start_date}"
            f"&conditions[publication_date][lte]={end_date}"
            "&fields[]=title"
            "&fields[]=publication_date"
            "&fields[]=document_number"
            "&fields[]=html_url"
            "&fields[]=subtype"
            "&per_page=1000"
            "&order=newest"
        )
        
        yield scrapy.Request(url=api_url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for doc in data.get("results", []):
            item = ExecutiveOrderItem()
            item["Title"] = doc.get("title")
            item["Date"] = doc.get("publication_date")
            item["Document_Number"] = doc.get("document_number")
            item["URL"] = doc.get("html_url")
            item["Subtype"] = doc.get("subtype")
            yield item

        # Follow pagination if results exceed per_page
        next_page = data.get("next_page_url")
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
