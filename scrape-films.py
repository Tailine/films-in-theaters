from bs4 import BeautifulSoup
import requests

separator = "===============================================================\n"
req = requests.get('https://www.cinemark.com.br/salvador/cinemas')
file = open("movies.txt", "w")

def display_results(title, times):
  print("FILME: ", title, "\nHORÁRIOS: ", times, "\n")

def main():
  if req.status_code == 200:
    page_content = req.content
    soup = BeautifulSoup(page_content, 'html.parser')
    films_data = soup.select(".tabs-content .active .theater")
    for data in films_data:
      title = data.select('h3 a')[0].text # get film title
      file.write(title) 

      theater_times = data.select(".theater-times")
      for info in theater_times:
        film_times = data.select(".times-options")
        film_languages = list(map(lambda span: span.text ,data.select(".times-labels.times-labels-right li span")))
        
        for i, time in enumerate(film_times):
          time_option = ", ".join(map(lambda span: span.text , time.select("li span")))
          file_content = f'\nHorários: {time_option} \nIdiomas: {film_languages[i]}\n\n'
          file.write(file_content)
        file.write(separator)
    # TODO - add link
    # TODO - write results into file 
  file.close()

main()