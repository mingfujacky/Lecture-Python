import requests
from bs4 import BeautifulSoup
import re

def get_bitcoin_price():
    url = "https://www.coinmarketcap.com/currencies/bitcoin"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the price element using a regex pattern
    price_element = soup.find('span', class_="sc-65e7f566-0 esyGGG base-text")

    if not price_element:
        raise Exception("Price element not found on the page")
    
    # Extract the text and clean it up
    price_text = price_element.get_text(strip=True)
    
    # Use regex to extract the numeric value from the text
    price_match = re.search(r'[\d,]+(?:\.\d+)?', price_text)
    
    if not price_match:
        raise Exception("Price not found in the text")
    
    return price_match.group(0)

if __name__ == "__main__":
    price = get_bitcoin_price()
    print(f"Latest Bitcoin price: {price}")