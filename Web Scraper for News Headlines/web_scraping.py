import requests
from bs4 import BeautifulSoup

def scrape_thehindu():
    response = requests.get("https://www.thehindu.com/")

    soup = BeautifulSoup(response.text,"html.parser")

    headlines = soup.find_all("h2",  class_ = "title")

    with open("headlines_thehindu.txt", "w", encoding="utf-8") as file:
        for i, line in enumerate(headlines,start=1):
            text = line.get_text(strip=True)
            if text:
                file.write(f"{i}. {text}\n")

def scrape_indiatoday():
    response = requests.get("https://www.indiatoday.in/")

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    with open("headlines_indiatoday.txt", "w", encoding="utf-8") as file:
        for i, line in enumerate(headlines, start=1):
            text = line.get_text(strip=True)
            if text:
                file.write(f"{i}. {text}\n")

def scrape_indianexpress():
    response = requests.get("https://indianexpress.com/")

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    with open("headlines_indianexpress.txt", "w", encoding="utf-8") as file:
        for i, line in enumerate(headlines, start=1):
            text = line.get_text(strip=True)
            if text:
                file.write(f"{i}. {text}\n")

scrape_thehindu()
scrape_indiatoday()
scrape_indianexpress()
