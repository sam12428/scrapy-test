import scrapy
from scrapy.http import Request

class FtpSpider(scrapy.Spider):
    name = "ftptest"
    allowed_domains = ["ftp.speed.hinet.net"]

    handle_httpstatus_list = [404]

    def start_requests(self):
        yield Request('ftp.speed.hinet.net',
                      meta={'ftp_user': 'ftp', 'ftp_password': 'ftp'})

    def parse(self, response):
        print response.body