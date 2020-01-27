## Create a dataframe of MDPI journals with their ISSN

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.mdpi.com/about/journals'
r=requests.get(url)

html_doc=r.text
soup=BeautifulSoup(html_doc)

a=soup.table
table_rows = a.find_all('tr')
res = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    if row:
        res.append(row)

df = pd.DataFrame(res, columns=['Journal Name','ISSN','Launched','Current Issue','Upcoming Articles','Total Articles','RSS'])
df['Journal Name']=df['Journal Name'].str.split().str[0]
df.head()

MDPI=df.iloc[:,0:2]

MDPI.to_csv('../Analysis Data/MDPI_journals.csv')
