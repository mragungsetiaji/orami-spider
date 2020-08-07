import scrapy

class SpiderSpider(scrapy.Spider):

    name = 'spider'
    allowed_domains = ['www.orami.co.id']
    disallowed_urls = ['http://www.orami.co.id/login']
    start_urls = [
        'http://www.orami.co.id/ap/takoyakids/',
    ]

    def parse(self, response):
        links = response.css('[class="wrap-list-product"] a::attr(href)').extract()
        links = list(set(links))
        for url in links:
            if url not in self.disallowed_urls:
                yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):

        title = response.xpath('//*[@id="product-brand-option"]/h1/text()').extract()[0].strip()
        price = response.xpath('//*[@id="product-price-option"]/div/div/text()').extract()[0].strip()
        seller = response.xpath('//*[@id="product-brand-option"]/p/span[2]/text()').extract()[0].strip() 
        highlight = response.xpath('//*[@id="highlight"]//text()').extract()

        highlight = '. '.join(highlight).strip().replace(",", " ").replace("\n", " ")

        scraped_info = {
            'url': response.url,
            'title' : title,
            'price' : price,
            'seller': seller,
            'highlight': highlight
        }

        yield scraped_info
