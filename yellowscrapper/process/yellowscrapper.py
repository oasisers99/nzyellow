import scrapy
from scrapy.http import Request

#scrapy crawl yellow -o yellow-auto.json -t jsonlines 
class YellowSpider(scrapy.Spider):

    #handle_httpstatus_list = [301]

    name = "yellow"
    start_urls = [
        'https://whitepages.co.nz/white-all/toys/new-zealand/1/',
    ]

    handle_httpstatus_list = [301,302]

    request_with_cookies = Request(url="https://whitepages.co.nz/white-all/toys/new-zealand/1/",
                               headers=[{
                                    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                    #'Accept-Encoding':'gzip, deflate, sdch, br',
                                    #'Accept-Language':'en-US,en;q=0.8',
                                    #'Cache-Control':'max-age=0',
                                    #'Connection':'keep-alive',
                                    'cookie':'wpSrc=direct / none; __insp_wid=848114167; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93aGl0ZXBhZ2VzLmNvLm56L3ljYXB0Y2hhP25leHQ9JTJGd2hpdGUtYWxsJTJGbWFzc2FnZSUyRm5ldy16ZWFsYW5kJTJGMTAlMkY%3D; __insp_targlpt=V2hpdGUgUGFnZXPCriAtIE5aIEJ1c2luZXNzICYgUmVzaWRlbnRpYWwgRGlyZWN0b3J5; __insp_norec_sess=true; __gads=ID=8bf409308ee926ae:T=1498716749:S=ALNI_MYnKIztAtp6KJebLQ0eeWwI_O5Dww; csrftoken=c2IQbpJNV3KCwO1Hz345BkxA2kXPCc8s; Oxygenid=47bjfp1x2f3ln7ybtd4ycsfbv4m0nxq6; _ga=GA1.3.997398821.1498716646; _gid=GA1.3.1021244401.1498716646; __utma=211115850.997398821.1498716646.1498716646.1498716646.1; __utmc=211115850; __utmz=211115850.1498716646.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __insp_slim=1498716758458; location_info="{\"doubleclick_latest_zone_id\": 3907}"; searchuuid=aee9746c-5c91-11e7-ace6-0242c0a8d503',
                                    #'Host':'whitepages.co.nz',
                                    'referer':'https://whitepages.co.nz/',
                                    #'Upgrade-Insecure-Requests':'1',
                                    #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                                    }],
                                )

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