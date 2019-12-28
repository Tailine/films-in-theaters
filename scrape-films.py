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
    print(title)
    theater_times = data.select(".theater-times")
    for info in theater_times:
      film_times = data.select(".times-options")
      for time in film_times:
        time_option = ", ".join(map(lambda span: span.text , time.select("li span")))
        film_languages = ", ".join(map(lambda span: span.text ,data.select(".times-labels.times-labels-right li span")))
        print(time_option)
        print(film_languages, "\n")
      print("===============================================================")

    # TODO - add languages
    # TODO - add link
    # TODO - write results into file 
    # display_results(title, times)