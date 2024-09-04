from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.foxsports.com/tennis/atp/rankings')
soup = BeautifulSoup(page.text, 'html')
table = soup.find('div', class_='table-wrapper')
table
titles = table.find_all('tr')[0]
column_titles_updated = []

for title in titles:
    column_titles_updated.append(title.text.strip())
    
print(column_titles_updated)
titles = table.find_all('tr')[0]
column_titles_updated = []

for title in titles:
    column_titles_updated.append(title.text.strip())
    
print(column_titles_updated)

table_data = soup.find_all('tr')[1:]

for row in table_data:
    row_data = row.find_all('td')
    
    indiv_row_data = [data.text.strip() for data in row_data[1:]]
    print(indiv_row_data)

df = pd.DataFrame(columns=column_titles_updated)

for row in table_data:
    row_data = row.find_all('td')
    
    indiv_row_data = [data.text.strip() for data in row_data[1:]]
    
    length = len(df)
    df.loc[length] = indiv_row_data

df.to_csv('tennis-rankings.csv')