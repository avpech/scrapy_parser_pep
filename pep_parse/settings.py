import os

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = os.getcwd()
RESULT_FOLDER = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
ENCODING = 'utf-8'
CSV_DIALECT = 'unix'

FEEDS = {
    f'{RESULT_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
