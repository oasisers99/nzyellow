import scrapy

class LoginSpider(scrapy.Spider):
	name = 'yellow'
	start_urls = ['https://yellow.co.nz/new-zealand/toys?what=toys']

	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			#formdata={'csrfmiddlewaretoken': 'drc9UB7jawKykwdImWRZmX6Ru1U4SwvC','g-recaptcha-response': '03AEHxwuwUXi5dnZJQwwQ4ZH6J1UDVxw7xYdQrBg0l3OxsHgDRAPKjMUC0r_z1HrSylbKlLYU9mmJ8xFZHYTBNqovKwDkAvvlXyAid8D6vhRGpArD405TNUM6YP6ZbjQpRU6Emg0aw6R2ufm_OYYnc_kqkLjnEJFCHLAKsSIZS6c9-GqGDehTy36hdfCVL9HeeI4kdHNDGUun5pGjeeItAsEcrJNZTrb_vRRpgRE-B8IeeUpgpaSvNN1LDg0UM6AeuIfRRu0PlaOQ2NDH5yXnPSbwsYX6p7cx5YtzcEo2UYV48_XtEX71Kvg5bDaDs1E_5HhNN_XOpZMrc'},
			formdata={'name':'csrfmiddlewaretoken','value':'drc9UB7jawKykwdImWRZmX6Ru1U4SwvC'},
            callback=self.after_auth
		)


	def after_auth(self, response):
		for yellow in response.xpath("//div[@class='itemTitle']//a[@data-ga-id='Listing_Name_Link']"):
			yield {
			'text': yellow.css("::text").extract_first()
			}

		next_page = response.xpath("//a[@title='Go to next page']/@href").extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)

