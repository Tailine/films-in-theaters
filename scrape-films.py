from bs4 import BeautifulSoup
import requests

separator = "======================================================================\n"
req = requests.get('https://www.cinemark.com.br/salvador/cinemas')
file = open("movies.txt", "w")

def main():
  if req.status_code == 200:
    page_content = req.content
    soup = BeautifulSoup(page_content, 'html.parser')
    films_data = soup.select(".tabs-content .active .theater")
    for data in films_data:
      title = data.select('h3 a')[0].text # get film title
      buy_ticket_link = (data.select('.actions .btn.btn-primary.btn-buy.reversed')[0]).get('href')
      file.write(f"\n{title}\n\nComprar ingressos: {buy_ticket_link}\n\n") 

      theater_times = data.find("ul", { "class": "theater-times" })
      theater_times = theater_times.findChildren("li", recursive = False)
      
      for film_data in theater_times:
        auditorium = list(map(lambda span: span.text , film_data.select(".times-auditorium")))
        
        film_languages = list(map(lambda span: span.text, film_data.select(".times-labels.times-labels-right li span")))

        film_times = film_data.select(".times-options")
      
        for i, time in enumerate(film_times):
          time_option = ", ".join(map(lambda span: span.text , time.select("li span")))
          file.write(f'{auditorium[i]}\nHorários: {time_option} \nIdiomas: {", ".join(film_languages)}\n\n')
      file.write(separator)

  file.close()

main()