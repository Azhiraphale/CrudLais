import scrapy
 
class BootstrapTableSpider(scrapy.Spider):
    name = "example"
 
    def start_requests(self):
        urls = [
            'http://cnes2.datasus.gov.br/Mod_Profissional.asp?VCo_Unidade=2408102653982',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//*[@id="example"]//tbody/tr'):
            yield {
                'first' : row.xpath('td[0]//text()').extract_first(),
                'last': row.xpath('td[3]//text()').extract_first(),
                'handle' : row.xpath('td[6]//text()').extract_first(),
            }
