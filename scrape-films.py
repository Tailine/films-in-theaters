from bs4 import BeautifulSoup
import requests

separator = "===============================================================\n"
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
      file.write(f"{title}\n\nComprar ingressos: {buy_ticket_link}\n\n") 

      auditorium = data.find("span", { "class": "times-auditorium" }).text
      file.write(auditorium)

      film_times = data.select(".times-options")
      film_languages = list(map(lambda span: span.text ,data.select(".times-labels.times-labels-right li span")))
      
      for i, time in enumerate(film_times):
        time_option = ", ".join(map(lambda span: span.text , time.select("li span")))
        file.write(f'\nHorários: {time_option} \nIdiomas: {film_languages[i]}\n\n')
      file.write(separator)
    # TODO - add link
    # TODO - write results into file 
  file.close()

main()