import requests
from bs4 import BeautifulSoup

# ==========================================
#          WEB SCRAPING PROJECT
# ==========================================

url = "https://quotes.toscrape.com/"

print("==========================================")
print("          WEB SCRAPING PROJECT")
print("==========================================")

try:
    # Send request to website
    response = requests.get(url, timeout=10)

    # Check whether request was successful
    if response.status_code == 200:

        print("\nWebsite connected successfully!")

        # Convert HTML into BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote blocks
        quotes = soup.find_all("div", class_="quote")

        print("\n========== SCRAPED QUOTES ==========")

        for number, quote in enumerate(quotes, start=1):

            text = quote.find(
                "span",
                class_="text"
            ).get_text(strip=True)

            author = quote.find(
                "small",
                class_="author"
            ).get_text(strip=True)

            print("\nQuote", number)
            print("Text   :", text)
            print("Author :", author)

        print("\n==========================================")
        print("Web scraping completed successfully!")
        print("==========================================")

    else:
        print("Website could not be accessed.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:

    print("\nAn error occurred while connecting to the website.")
    print("Error:", error)