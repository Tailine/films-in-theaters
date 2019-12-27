from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.cinemark.com.br/salvador/cinemas')

if req.status_code == 200:
  page_content = req.content
  soup = BeautifulSoup(page_content, 'html.parser')
  films_title = soup.select(".tabs-content .active .theater .theater-header h3")
  for film_title in films_title:
    print(film_title.text)