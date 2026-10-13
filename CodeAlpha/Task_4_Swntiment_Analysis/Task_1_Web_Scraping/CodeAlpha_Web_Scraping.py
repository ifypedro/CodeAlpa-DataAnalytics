import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


# Store scraped book records
books_data = []


# Scrape 50 catalogue pages
for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to access page {page}")
        continue

    soup = BS(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        relative_url = book.h3.a["href"]

        product_url = (
            "https://books.toscrape.com/catalogue/"
            + relative_url
        )

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": product_url
        })

    print(f"Page {page} scraped successfully.")


# Create DataFrame
books_data_multipage_df = pd.DataFrame(books_data)


# ======= CLEANING THE DATA =========

# Clean the price column - remove both £ and Â characters
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].str.replace("£", "", regex=False)
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].str.replace("Â", "", regex=False)  # Remove the problematic Unicode character
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].astype(float)

# Checking the price datatype
books_data_multipage_df["Price"].dtype


books_data_multipage_df["Price"] = books_data_multipage_df["Price"].astype(float)


# Check dataset information
print("\nDataset Shape:")
print(books_data_multipage_df.shape)

print("\nMissing Values:")
print(books_data_multipage_df.isnull().sum())

print("\nDuplicate Rows:")
print(books_data_multipage_df.duplicated().sum())


# Save dataset
books_data_multipage_df.to_csv("books_dataset.csv", index=False)


print("\nScraping completed successfully!")
print(f"Total books scraped: {len(books_data_multipage_df)}")
print("Dataset saved as books_dataset.csv")