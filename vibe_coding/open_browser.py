import webbrowser
import urllib.parse

def main():
    query = input("Enter your Wikipedia search query: ")
    encoded_query = urllib.parse.quote(query)
    url = f"https://en.wikipedia.org/wiki/Special:Search?search={encoded_query}"
    webbrowser.open(url)

if __name__ == "__main__":
    main()