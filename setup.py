import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from wrdSpider.spiders.wrd_spider import WrdSpider
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())

domains = ['domain1.xlsx',
           'domain2.xlsx',
           'domain3.xlsx',
           'domain4.xlsx',
           'domain5.xlsx',
           'domain6.xlsx',
           'domain7.xlsx',
           'domain8.xlsx',
           'domain9.xlsx',
           'domain10.xlsx',
           'domain11.xlsx',
           'domain12.xlsx',
           'domain13.xlsx',
           'domain14.xlsx',
           'domain15.xlsx',
           'domain16.xlsx',
           'domain17.xlsx',
           'domain18.xlsx',
           'domain19.xlsx',
           'domain20.xlsx']

@defer.inlineCallbacks
def crawl():
    for domain in domains:
        yield runner.crawl(WrdSpider, filename=domain)
    reactor.stop()

crawl()
reactor.run()
