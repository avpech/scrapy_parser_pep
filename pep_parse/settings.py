import os

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DOMAIN = 'peps.python.org'
BASE_DIR = os.getcwd()
RESULT_FOLDER = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
OUTPUT_FORMAT = 'csv'
CSV_ENCODING = 'utf-8'
CSV_DIALECT = 'unix'

FEEDS = {
    f'{RESULT_FOLDER}/pep_%(time)s.{OUTPUT_FORMAT}': {
        'format': OUTPUT_FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
