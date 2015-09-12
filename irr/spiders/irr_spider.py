# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from irr.items import IRRTitle

class IRRSpider(CrawlSpider):
    name = "irr"
    allowed_domains = ["irr.ru"]
    start_urls = [
        "http://www.irr.ru/real-estate/commercial/search/currency=RUR/sourcefrom=0/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial/search/currency=RUR/sourcefrom=1/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial-sale/search/currency=RUR/sourcefrom=0/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial-sale/search/currency=RUR/sourcefrom=1/date_create=yesterday/page_len60/"
    ]
    rules = [
        Rule(LinkExtractor(
            allow=['/real-estate/.*/page\\d/$']),
            callback='parse_item',
            follow=True)
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        titles = response.xpath('//div[@class="productName js-productListingProductName"]/text()')
        with open('lol.txt', 'a') as f:
            for i in response.xpath('//div[@class="productName js-productListingProductName"]/text()').extract():
                f.write(i.encode('utf-8'))
        items = []
        for title in titles:
           item = IRRTitle()
           item['title'] = title.extract()
           items.append(item)
        return 