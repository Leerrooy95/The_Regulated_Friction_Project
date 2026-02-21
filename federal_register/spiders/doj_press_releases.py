"""Spider to scrape press releases from the Department of Justice.

Target: https://www.justice.gov/news
Data source: DOJ public JSON API (no key required)
Extracts: Title, Date, URL, Component, Topic, Number, UUID for each release.

Filters to the last 30 days of publications.

Note: The DOJ API sorts results in ascending date order by default and does
not support reliable descending sort.  This spider first fetches metadata to
determine the total result count, then begins iterating backwards from the
last page so the most recent press releases are encountered first.
"""

import json
import math
from datetime import datetime, timedelta

import scrapy

from federal_register.items import DOJPressReleaseItem

PAGESIZE = 50
BASE_URL = "https://www.justice.gov/api/v1/press_releases.json"


class DOJPressReleaseSpider(scrapy.Spider):
    """Scrape DOJ press releases from the justice.gov API (last 30 days)."""

    name = "doj_press_releases"
    allowed_domains = ["www.justice.gov", "justice.gov"]

    # Rolling window in days (configurable via -a days=N)
    days = 30

    def start_requests(self):
        self.cutoff = datetime.utcnow() - timedelta(days=int(self.days))
        # Fetch a single record to learn the total count
        url = f"{BASE_URL}?pagesize=1&page=0"
        yield scrapy.Request(url=url, callback=self.parse_count)

    def parse_count(self, response):
        """Read total count and start from the last page."""
        data = json.loads(response.text)
        total_count = int(
            data.get("metadata", {}).get("resultset", {}).get("count", 0)
        )
        if total_count == 0:
            return

        last_page = math.ceil(total_count / PAGESIZE) - 1
        url = f"{BASE_URL}?pagesize={PAGESIZE}&page={last_page}"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        results = data.get("results", [])

        if not results:
            return

        # Track whether any item on this page is within the date window.
        # Pages are ascending by date, so we process every item on the page
        # (some may straddle the cutoff boundary) and only stop paginating
        # backwards when no items on a page fall within the window.
        found_in_window = False

        for doc in results:
            doc_date = datetime.utcfromtimestamp(int(doc.get("date", "0")))
            if doc_date < self.cutoff:
                continue  # Skip items outside the window

            found_in_window = True

            item = DOJPressReleaseItem()
            item["Title"] = doc.get("title")
            item["Date"] = doc_date.strftime("%Y-%m-%d")
            item["URL"] = doc.get("url")
            item["UUID"] = doc.get("uuid")
            item["Number"] = doc.get("number") or ""

            # Component is always an array of dicts
            components = doc.get("component", [])
            item["Component"] = ", ".join(
                c.get("name", "") for c in components
            ) if isinstance(components, list) else ""

            # Topic is an array of dicts when populated, empty string when absent
            topics = doc.get("topic", [])
            item["Topic"] = ", ".join(
                t.get("name", "") for t in topics
            ) if isinstance(topics, list) else ""

            yield item

        # Paginate backwards to the previous page if this page had results
        # within the date window
        meta = data.get("metadata", {}).get("resultset", {})
        current_page = int(meta.get("page", 0))

        if found_in_window and current_page > 0:
            prev_page = current_page - 1
            prev_url = f"{BASE_URL}?pagesize={PAGESIZE}&page={prev_page}"
            yield scrapy.Request(url=prev_url, callback=self.parse)
