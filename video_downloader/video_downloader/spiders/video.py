# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['lynda.com/search?q=python']
    start_urls = ['http://lynda.com/search?q=python/']

    def parse(self, response):
        chunk_size = 256
        download_url = "https://files3.lynda.com/secure/courses/699337/VBR_MP4h264_main_SD/699337_00_01_WX30_welcome.mp4?V4Faq8CHz_eQQJ73xNDNghmOUw60nCczxhqgDYUz0He_omKluMnS2wX3G2zHxx24ZgrPuIZ-5xkhAZKXLJEjeW3H7sIatiCkvd9HGxLC4DaVxBR3nos6JvThFczuEbifirmNXA1f-5WI5RxC4tCt3WwfEBbvoMQSE5S2H3AqrUWkaPz99qgzL6bbvgI&c3.ri=3775116901097783853"
        r = requests.get(download_url, stream=True)
        with open("lynda.mp4", 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
        # yield Request(callback=self.parse)
