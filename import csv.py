import csv
import requests

url = 'https://hbiostat.org/data/repo/titanic3.csv'
response = requests.get(url)        

with open('out.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))