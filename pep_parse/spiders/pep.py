from typing import Iterator

import scrapy
from scrapy.http import Request, Response

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [f'https://{DOMAIN}/']

    def parse(self, response: Response) -> Iterator[Request]:
        """Сбор ссылок на страницы документов PEP."""
        links = response.css('#numerical-index a[href^="pep-"]')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response: Response) -> Iterator[PepParseItem]:
        """Сбор информации со страниц с документами PEP."""
        number = int(
            response.css('header > ul > li:nth-child(3)::text')
            .get().replace('PEP', '').strip()
        )
        name = response.css('h1.page-title::text').get().strip()
        status = response.css(
            'dt:contains("Status") + dd ::text').get().strip()
        yield PepParseItem(number=number, name=name, status=status)
