from flask import Flask, render_template, url_for,\
    request, redirect

import sqlite3
from contextlib import closing

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from database_setup import Base, Title

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# <sqlalchemy code>

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# </sqlalchemy code>


# <scrapy>

class IRRSpider(CrawlSpider):
    name = "irr"
    allowed_domains = ["irr.ru"]
    start_urls = [
        "http://www.irr.ru/real-estate/commercial/search/currency=RUR/sourcefrom=0/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial/search/currency=RUR/sourcefrom=1/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial-sale/search/currency=RUR/sourcefrom=0/date_create=yesterday/page_len60/",
        "http://www.irr.ru/real-estate/commercial-sale/search/currency=RUR/sourcefrom=1/date_create=yesterday/page_len60/"
    ]
    rules = [
        Rule(LinkExtractor(
            allow=['/real-estate/.*/page\\d/$']),
            callback='parse_item',
            follow=True)
    ]
    # function to make spider not to stop on first url
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
    	# populating sqlite sdb with parsed items:
        for title in response.xpath('//div[@class="productName js-productListingProductName"]/text()').extract():
        	newTitle = Title(name=title)
        	session.add(newTitle)
        	session.commit()
        return 

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# </scrapy>

# <flask app>
DATABASE = 'test.db'

app = Flask(__name__)
app.config.from_object(__name__)

# ==== functions for creating and operating sqlite db ====


def connect_db():
	"""Connecting to db"""
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
# ==== functions for creating and operating sqlite db ====

# ==== flask functions ====
@app.route('/', methods=['GET','POST'])
def index():
	if request.method == "POST":
		# run spider
		process.crawl(IRRSpider)
		process.start()
		return redirect(url_for('titles'))
	else:
		return render_template('index.html')

@app.route('/titles', methods=['GET','POST'])
def titles():
	# retrive all titles from sqlite usting sqlalchemy
	titles = session.query(Title).all()
	return render_template('titles.html',titles=titles)

if __name__ == '__main__': 
    app.run(debug=True)
# </flask app>