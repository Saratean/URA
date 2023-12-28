from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

url = 'https://new-science.ru/category/news/page/3/'

r = requests.get(url)

bs = BS(r.content, "html.parser")


temp = bs.find_all('div', 'post-details')


dict_news = {"news": [], "links": [], "views": [], "date": []}

for i in temp:
  dict_news["news"].append(i.find('h2', 'post-title').text)
  dict_news["links"].append(i.find('h2', 'post-title').find('a').get('href'))
  dict_news["date"].append(i.find('span', 'date meta-item tie-icon').text)
  dict_news["views"].append(i.find('span', 'meta-views meta-item').text)
  
print(
    len(dict_news["news"]),
    len(dict_news["links"]),
    len(dict_news["views"]),
    len(dict_news["date"])
)

df_news = pd.DataFrame(dict_news, columns=["news", "links", "views", "date"])

df_news.to_csv("./saved_data.csv")