import requests
import pandas as pd
from bs4 import BeautifulSoup

def html_table_to_dataframe(url):
  #url = "https://www.irdai.gov.in/ADMINCMS/cms/NormalData_Layout.aspx?page=PageNo765&mid=31.2"
  response = requests.get(url)
  html_text = response.text[:]
  soup = BeautifulSoup(html_text, 'html.parser')
  h_table = soup.find_all('table', {"class": "MsoNormalTable"})[0]
  df = pd.DataFrame(index=range(0,1), columns=['A'])
  column_names = []
  row_mk = 0
  for row in h_table.find_all('tr'):
    column_mk = 0
    if len(row.find_all('th')) > 0:
      for t_head in row.find_all('th'):
        print(t_head.find_all('span')[0].get_text())
    else:
      if len(column_names) == 0:
        for t_td in row.find_all('td'):
          column_names.append(t_td.find_all('span')[0].get_text())
        columns_label = column_names if len(column_names) > 0 else range(0,len(column_names))
        df = pd.DataFrame(columns = columns_label, index= range(0,len(h_table.find_all('tr'))-1))
      else:
        for t_td in row.find_all('td'):
          df.iat[row_mk, column_mk] = t_td.find_all('span')[0].get_text()
          column_mk += 1
        row_mk += 1

  return df
  #df.to_csv('sample.csv', index=False, encoding='utf-8')

print(html_table_to_dataframe("https://www.irdai.gov.in/ADMINCMS/cms/NormalData_Layout.aspx?page=PageNo765&mid=31.2"))
