import scrapy
from scrapy.http import Request

#scrapy crawl yellow -o yellow-auto.json -t jsonlines 
class YellowSpider(scrapy.Spider):

    handle_httpstatus_list = [302]

    name = "yellow"
    start_urls = [
        'https://whitepages.co.nz/white-all/toys/new-zealand/1/',
    ]


    def parse(self, response):
        # Target the main list that does not have ads.
        for yellow in response.xpath("//div[@class='itemTitle']//a[@data-ga-id='Listing_Name_Link']"):
            yield {
                'text': yellow.css("::text").extract_first()
            }

        # Target the 'next' page link.
        next_page = response.xpath("//a[@title='Go to next page']/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)