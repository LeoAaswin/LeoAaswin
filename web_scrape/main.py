import requests
from datetime import datetime
import csv

ticker = input("Enter the ticker symbol:")
from_date = input("Enter the start date in yyyy-mm-dd format:")
to_date = input("Enter the end date in yyyy-mm-dd format:")

from_epoch = int(datetime.strptime(from_date, '%Y-%m-%d').timestamp())
to_epoch = int(datetime.strptime(to_date, '%Y-%m-%d').timestamp())

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
    content = response.text
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

# Save data to CSV file
with open('data.csv', 'w', newline='') as csvfile:
    csvfile.write(content)
