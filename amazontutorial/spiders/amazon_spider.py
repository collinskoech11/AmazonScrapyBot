# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2']

    def parse(self, response):
        items = AmazontutorialItem()


        product_name = response.css('.p13n-sc-truncated').extract()
        product_author = response.css('.a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').get()
        product_price = response.css('..p13n-sc-price , .zg-item-immersion:nth-child(14) .a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').get()
        product_imagelink = response.css('img , #zg-other-container+ .zg-item-immersion .p13n-sc-price , .zg-item-immersion:nth-child(14) .a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').get()
