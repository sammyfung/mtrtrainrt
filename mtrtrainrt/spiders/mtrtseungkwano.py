# -*- coding: utf-8 -*-
from .mtrwestrail import MtrwestrailSpider


class MtrtseungkwanoSpider(MtrwestrailSpider):
    name = 'mtrtseungkwano'
    line_code = 'TKL'
    stations = {
        'NOP': 'North Point', 'QUB': 'Quarry Bay', 'YAT': 'Yau Tong',
        'TIK': 'Tiu Keng Leng', 'TKO': 'Tseung Kwan O', 'LHP': 'LOHAS Park',
        'HAH': 'Hang Hau', 'POA': 'Po Lam'
    }
