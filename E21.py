from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,features="html.parser")
for headers in soup.find_all('h2'):
    with open('NY_Headers.txt', 'a') as open_file:
        open_file.write(headers.text)
