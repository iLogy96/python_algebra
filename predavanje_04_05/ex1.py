import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/index.html?"

naslov_selector = ".product_pod h3 a"
rating_selector = ".star-rating"
price_selector = ".price_color"

page = BeautifulSoup(requests.get(URL).content, "html.parser")

naslovi = page.select(naslov_selector)
ocjene = page.select(rating_selector)
cijene = page.select(price_selector)
# spremimo podatke u tekstualnu datoteku
with open("./predavanje_04_05/books.csv", "w") as file:

    for cijena, naslov, ocjena in zip(cijene, naslovi, ocjene):
        out = f"{naslov.text},{cijena.text},{ocjena['class'][1]}\n"
        file.write(out)

print()
