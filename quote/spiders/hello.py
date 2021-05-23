import scrapy
from scrapy import Selector
from ..items import QuoteItem

class myproject(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ["hercules.in"]
    start_urls = [
        'https://hercules.in/hercules-mtb/'
    ]
    def parse(self, response):
        items = QuoteItem()
        sel = Selector(response)
        title = sel.xpath("//div[@data-transition='esg-zoomfront']/a[@target='_self']/text()").extract()
        image = sel.xpath("//div[@class='esg-entry-media esg-transition']/img/@data-lazysrc").extract()

        items['title'] = [title, image]

        yield items
