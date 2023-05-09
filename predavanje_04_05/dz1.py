import requests
from bs4 import BeautifulSoup

URLs = [
    "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html",
    "http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html",
]

title_selector = ".product_pod h3 a"
price_selector = ".product_price .price_color"

book_list = []

# Loop through all the URLs
for url in URLs:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the book titles and prices on the page
    titles = soup.select(title_selector)
    prices = soup.select(price_selector)

    # Store each book's title and price in a dictionary and add it to the book list
    for title, price in zip(titles, prices):
        book_list.append({"title": title.text, "price": float(price.text[1:])})

# Find the most and least expensive books
most_expensive = max(book_list, key=lambda x: x["price"])
least_expensive = min(book_list, key=lambda x: x["price"])

# Write out the results in books.csv
with open("./predavanje_04_05/books.csv", "w") as file:
    out = (
        f"The most expensive book is {most_expensive['title']} and it costs {most_expensive['price']:.2f}.\n"
        f"The least expensive book is {least_expensive['title']} and it costs {least_expensive['price']:.2f}.\n"
    )
    file.write(out)

