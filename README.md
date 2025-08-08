# Elevate-Labs-Internship-Task-3
# News Headlines Web Scraper

This Python script scrapes top news headlines from the **India Today** website using `requests` and `BeautifulSoup`. It automates the process of collecting current headlines and saves them into a `.txt` file for easy reference.

## Tools Used
- Python 3
- `requests` for fetching HTML
- `BeautifulSoup` for parsing HTML content

## Features
- Extracts 30+ headlines from India Today's homepage
- Cleans and formats each headline
- Saves output to a numbered `.txt` file

## Why India Today?
While exploring multiple news sites (India Today, The Hindu, Indian Express), India Today provided the most scraper-friendly structure with over 30 headlines in static HTML. Other sites had limited visible content due to dynamic loading or minimal homepage listings.

## How to Run
```bash
python web_scraper.py

## Learning Outcomes
- Understanding HTTP GET requests
- Parsing HTML with BeautifulSoup
- Handling exceptions and file I/O
- Evaluating site structure for scraping suitability
