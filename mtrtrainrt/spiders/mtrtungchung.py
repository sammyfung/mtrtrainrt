# -*- coding: utf-8 -*-
from .mtrwestrail import MtrwestrailSpider


class MtrtungchungSpider(MtrwestrailSpider):
    name = 'mtrtungchung'
    line_code = 'TCL'
    stations = {
        'HOK': 'Hong Kong', 'KOW': 'Kowloon', 'OLY': 'Olympic',
        'NAC': 'Nam Cheong', 'LAK': 'Lai King', 'TSY': 'Tsing Yi',
        'SUN': 'Sunny Bay', 'TUC': 'Tung Chung'
    }
