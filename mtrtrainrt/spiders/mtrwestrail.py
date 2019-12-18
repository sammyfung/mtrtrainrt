# -*- coding: utf-8 -*-
import scrapy, json, re
from mtrtrainrt.items import MtrtrainrtItem


class MtrwestrailSpider(scrapy.Spider):
    name = 'mtrwestrail'
    allowed_domains = ['rt.data.gov.hk']
    line_code = 'WRL'
    stations = {
        'HUH': 'Hung Hom', 'ETS': 'East Tsim Sha Tsui', 'AUS': 'Austin',
        'NAC': 'Nam Cheong', 'MEF': 'Mei Foo', 'TWW': 'Tsuen Wan West',
        'KSR': 'Kam Sheung Road', 'YUL': 'Yuen Long', 'LOP': 'Long Ping',
        'TIS': 'Tin Shui Wai', 'SIH': 'Siu Hong', 'TUM': 'Tuen Mun'
    }
    url_prefix = 'https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php'
    start_urls = [ url_prefix ]

    def parse(self, response):
        for code, name in self.stations.items():
            yield scrapy.Request('%s?line=%s&sta=%s' % (self.url_prefix, self.line_code, code), self.parse_station)

    def parse_station(self, response):
        data = json.loads(response.body_as_unicode())
        code = re.sub('.*sta=', '', response.request.url)
        code = re.sub('&.*', '', code)
        station = self.stations[code]
        for dir in ('UP', 'DOWN'):
            try:
                for i in data['data']['%s-%s' % (self.line_code, code)][dir]:
                    item = MtrtrainrtItem()
                    item['station'] = station
                    item['code'] = code
                    item['line'] = self.line_code
                    item['dir'] = dir
                    item['time'] = i['time']
                    item['dest_code'] = i['dest']
                    item['dest'] = self.stations[item['dest_code']]
                    item['platform'] = i['plat']
                    item['last_update'] = data['curr_time']
                    item['is_delay'] = False if data['isdelay'] == 'N' else True
                    yield(item)
            except KeyError:
                pass
