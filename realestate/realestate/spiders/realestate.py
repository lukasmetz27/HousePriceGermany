import scrapy

class Realestate(scrapy.Spider):
    name = 'real'
    allowed_domains = ['immonet.de']
    start_urls = ['https://www.immonet.de/wohnung-mieten/hamburg.html']

    def parse(self, response):
        for apartment in response.xpath('//div[@class="col-xs-12 search-list-entry"]'):
            yield {
                'title': apartment.xpath('.//h3/a/text()').get(),
                'address': apartment.xpath('.//div[contains(@class, "address-block")]/text()').get(),
                'price': apartment.xpath('.//div[contains(@class, "price-block")]/text()').get(),
            }