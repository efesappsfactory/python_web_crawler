from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class EPNCrawler(CrawlSpider):
    name = 'epn'
    allowed_domains = ['www.epn.edu.ec']
    start_urls = ['https://www.epn.edu.ec/']
    rules = (Rule(LinkExtractor()),)