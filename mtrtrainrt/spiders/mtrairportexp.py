# -*- coding: utf-8 -*-
from .mtrwestrail import MtrwestrailSpider


class MtrairportexpSpider(MtrwestrailSpider):
    name = 'mtrairportexp'
    line_code = 'AEL'
    stations = {
        'HOK': 'Hong Kong', 'KOW': 'Kowloon', 'TSY': 'Tsing Yi',
        'AIR': 'Airport', 'AWE': 'AsiaWorld Expo'
    }
