from pytrends.request import TrendReq
import time

def index_with_dates(keywords, start_date, end_date):
     """
     keywords: list of keywords => ['AAPL']
     start_date: a date as type string => '2018-01-01'
     end_date: a date as type string => '2018-01-01'
     when time interval is under than 8 months it returns on a daily basis
     when time interval is under than 6 years it returns on a weekly basis
     when time interval more than 6 years it returns on a yearly basis
     # cat='' Financial Markets: 1163
     """
     try:
          pytrends = TrendReq(hl='en-US', tz=360, requests_args={'verify':False})
          timeframe = start_date + " " + end_date
          pytrends.build_payload(kw_list=keywords, timeframe=timeframe, geo='', gprop='')
          results = pytrends.interest_over_time()
          time.sleep(6)
          return results
     except Exception as e:
          print(e)
          print(f'error has occured for {keywords}, {start_date} to {end_date}')


