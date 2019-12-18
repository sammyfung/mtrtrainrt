# Real-time MTR train information in Hong Kong


Author: Sammy Fung


Scrape the arrival time information for up to the next five trains of the Airport Express, Tung Chung Line, West Rail Line and Tseung Kwan O Line. 


This project is also good for data archive with build-in csv / json output provided by Scrapy. 


Data Source: https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data


## Installation


# pip -r requirements.txt


## Scraping

Airport Express: scrapy crawl mtrairportexp -t csv -o test.csv --logfile=test.log


Tung Chung Line: scrapy crawl mtrtungchung -t csv -o test.csv --logfile=test.log


West Rail Line: scrapy crawl mtrwestrail -t csv -o test.csv --logfile=test.log


Tseung Kwan O Line: scrapy crawl mtrtseungkwano -t csv -o test.csv --logfile=test.log


