# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2']

    def parse(self, response):
        items = AmazontutorialItem()


        product_name = response.css('.p13n-sc-truncated::text').extract()
        product_author = response.css('.a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').css('::text').extract()
        #product_price = response.css('..p13n-sc-price , .zg-item-immersion:nth-child(14) .a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').css('::text').extract()
        #product_imagelink = response.css('img , #zg-other-container+ .zg-item-immersion .p13n-sc-price , .zg-item-immersion:nth-child(14) .a-link-child , .zg-item-immersion:nth-child(2) .p13n-sc-truncated').css('::alt(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        #items['product_price'] = product_price
        #items['product_imagelink'] = product_imagelink

        yield items