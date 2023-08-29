from typing import Iterator

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.http import Request, Response

from pep_parse.items import PepParseItem
from pep_parse.spiders.pep import PepSpider


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseSpiderMiddleware':
        """This method is used by Scrapy to create spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self,
                             response: Response,
                             spider: PepSpider) -> None:
        """Called for response into the spider through the spider middleware.

        Should return None or raise an exception.
        """
        return None

    def process_spider_output(self,
                              response: Response,
                              result: Iterator[PepParseItem],
                              spider: PepSpider) -> Iterator[PepParseItem]:
        """Called with the results returned from the Spider.

        Must return an iterable of Request, or item objects.
        """
        for i in result:
            yield i

    def process_spider_exception(self,
                                 response: Response,
                                 exception: Exception,
                                 spider: PepSpider) -> None:
        """Called when a spider or process_spider_input() raises an exception.

        Should return either None or an iterable of Request or item objects.
        """
        pass

    def process_start_requests(self,
                               start_requests: Iterator[Request],
                               spider: PepSpider) -> Iterator[Request]:
        """Called with the start requests of the spider.

        Works similarly to the process_spider_output() method,
        except that it doesn’t have a response associated.
        Must return only requests (not items).
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider: PepSpider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseDownloaderMiddleware':
        """This method is used by Scrapy to create your spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider: PepSpider) -> None:
        """Called for requests that go through the downloader middleware.

        Must either:
        - return None: continue processing this request
        - or return a Response object
        - or return a Request object
        - or raise IgnoreRequest: process_exception() methods of
          installed downloader middleware will be called
        """
        return None

    def process_response(self,
                         request: Request,
                         response: Response,
                         spider: PepSpider) -> Response:
        """Called with the response returned from the downloader.

        Must either;
        - return a Response object
        - return a Request object
        - or raise IgnoreRequest
        """
        return response

    def process_exception(self,
                          request: Request,
                          exception: Exception,
                          spider: PepSpider) -> None:
        """Called when download handler or process_request() raises exception.

        Must either:
        - return None: continue processing this exception
        - return a Response object: stops process_exception() chain
        - return a Request object: stops process_exception() chain
        """
        pass

    def spider_opened(self, spider: PepSpider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
