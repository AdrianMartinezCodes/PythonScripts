import requests
from bs4 import BeautifulSoup


url1 = "https://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html"
url2 = "https://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749_2.html?sid=ST2010082902923"
r = requests.get(url1)
s = requests.get(url2)
r_html = r.text
s_html = s.text


soup1 = BeautifulSoup(r_html,'html.parser')
soup2 = BeautifulSoup(s_html,'html.parser')

for paper in soup1.find_all('p'):
    print(paper.text,"\n")
for paper in soup2.find_all('p'):
    print(paper.text,"\n")
