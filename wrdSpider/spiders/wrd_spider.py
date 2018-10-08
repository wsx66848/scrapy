# -*- coding: utf-8 -*-
import scrapy
import re
import urlparse
import xlrd
from wrdSpider.items import WrdSpiderItem
from scrapy.utils.response import get_base_url


class WrdSpider(scrapy.Spider):
    name = 'wrd_spider'
    start_urls = list()
    description = dict()

    def __init__(self, filename):
        super(WrdSpider, self).__init__(self.name)
        url_file = xlrd.open_workbook(filename)
        table = url_file.sheet_by_index(0)
        rows = table.nrows
        for row_num in range(0, rows):
            data = table.row_values(row_num)
            http_url = "http://%s" % data[0]
            https_url = "https://%s" % data[0]
            self.start_urls.append(http_url)
            self.start_urls.append(https_url)
            self.description[http_url] = data[1]
            self.description[https_url] = data[1]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta={'start_url': url,
                                                                 'description': self.description[url]})

    def parse(self, response):
        if type(response) is scrapy.http.Response:
            pass
        else:
            url_list = response.xpath("//a/@href").extract()
            title = response.xpath("//title/text()").extract_first()
            base_url = get_base_url(response)
            description = response.meta['description']
            if title:
                title = title.encode('utf8')
            if type(description) is unicode and description:
                description = description.encode('utf8')
            for url in url_list:
                url = urlparse.urljoin(base_url, url)
                if re.match(r'[a-zA-z]+://[^\s]*', url):
                    yield scrapy.Request(url, callback=self.parse, meta={'start_url': response.meta['start_url'],
                                                                         'description': response.meta['description']})
            yield WrdSpiderItem(title=title,
                                url=response.url,
                                root_url=response.meta['start_url'],
                                description=description,
                                host=urlparse.urlparse(response.url).netloc)




