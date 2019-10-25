import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://slo-tech.com/delo',
    ]

    def parse(self, response):

        for job in response.xpath('//div[@id="page_content"]/div[@id="content"]/table[@class="forums"]/tbody/tr'):
        
            yield {
                'title': job.xpath('td[@class="name"]/h3/a/text()').get(),
                'department': job.xpath('td[@class="name"]/div/span[@class="oddelek"]/a/text()').get(),
                'poster': job.xpath('td[@class="company"]/a/text()').get(),
                'url': job.xpath('td[@class="name"]/h3/a/@href').get(),
            }

      



        