import scrapy
from scrapy.crawler import CrawlerProcess
import sys


    
if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]

class WbotSpider(scrapy.Spider):
    import datetime
    
    name = 'wbot'
    allowed_domains = ['www.bazaar.shopclues.com/']
    start_urls = ['https://bazaar.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G&fsrc=facet_network_type/']

    custom_settings = {
         'FEED_FORMAT':'csv',
         'FEED_URI': 'results.csv'
         }
    
    date1 = datetime.date.today()
    def parse(self, response):
        #Extracting the content using css selectors
        prod_name = response.css(".prod_name::text").extract()
        prod_price = response.css(".p_price::text").extract()
        prod_discount = response.css(".prd_discount::text").extract()
        prod_img_link = response.css("img::attr(data-img)").extract()
        #date = datetime.date.today()
        date_test = self.date1
    #def dte():
        #currentDateAndTime = datetime.now()
        

       
        #Give the extracted content row wise
        for item in zip(prod_name,prod_price,prod_discount,prod_img_link):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Name' : item[0],
                'Price' : item[1],
                'Discount' : item[2],
                'Link' : item[3],
                'DateExtract' : date_test
            }
            #yield or give the scraped info to scrapy
            yield scraped_info
            
process = CrawlerProcess()
process.crawl(WbotSpider)
process.start()


