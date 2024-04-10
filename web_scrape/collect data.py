import requests
from datetime import datetime
import time
import csv

ticker = input("Enter the ticker symbol:")
from_date = input("Enter the start date in y/m/d format:")
to_date = input("Enter the end date in y/m/d format:")

from_date = datetime.strptime(from_date, '%Y/%m/%d')
to_date = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_date.timetuple()))
to_epoch = int(time.mktime(to_date.timetuple()))

url = f"https://finance.yahoo.com/quote/{ticker}/history?period1={from_epoch}&period2={to_epoch}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers)
print(content)

with open('data.csv', 'wb')as file:
    file.write(content)