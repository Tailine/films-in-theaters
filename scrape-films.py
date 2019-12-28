from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.cinemark.com.br/salvador/cinemas')

def display_results(title, times):
  print("FILME: ", title, "\nHORÁRIOS: ", times, "\n")

if req.status_code == 200:
  page_content = req.content
  soup = BeautifulSoup(page_content, 'html.parser')
  films_data = soup.select(".tabs-content .active .theater")
  for data in films_data:
    # get film title
    title = data.select('h3 a')[0].text
    # get film times
    film_times = data.select(".times-options li span")
    times = ", ".join(list(map(lambda html: html.text, film_times)))
    
    # TODO - add link
    # TODO - write results into file 
    display_results(title, times)