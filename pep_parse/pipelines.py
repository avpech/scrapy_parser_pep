import csv
import datetime as dt
import os
from collections import defaultdict

from pep_parse.items import PepParseItem
from pep_parse.settings import (BASE_DIR, CSV_DIALECT, CSV_ENCODING,
                                DATETIME_FORMAT, OUTPUT_FORMAT, RESULT_FOLDER)
from pep_parse.spiders.pep import PepSpider


class PepParsePipeline:
    """Создание сводки по статусам PEP."""

    def open_spider(self, spider: PepSpider) -> None:
        """Создание счетчика количества документов по статусу."""
        self.counter = defaultdict(int)

    def process_item(self,
                     item: PepParseItem,
                     spider: PepSpider) -> PepParseItem:
        """Увеличение счетчика для полученного документа."""
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider: PepSpider) -> None:
        """Вывод сводки по статусам PEP в csv-файл."""
        results_dir = os.path.join(BASE_DIR, RESULT_FOLDER)
        os.makedirs(results_dir, exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.{OUTPUT_FORMAT}'
        file_path = os.path.join(results_dir, file_name)
        with open(file_path, 'w', encoding=CSV_ENCODING) as file:
            writer = csv.writer(file, dialect=CSV_DIALECT)
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(sorted(self.counter.items()))
            writer.writerow(('Total', sum(self.counter.values())))
