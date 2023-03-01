import pytest
from src.scraper import Scraper

def test_get_correct_number_of_urls():
    scraper = Scraper("romance", 40)
    url_list = ['https://www.bookdepository.com/search?searchTerm=romance', 'https://www.bookdepository.com/search?searchTerm=romance&page=2']
    assert scraper.get_url() == url_list

def test_request_page():
    scraper = Scraper("romance", 2)
    page= scraper.request_page("https://www.bookdepository.com/search?searchTerm=romance")
    assert page.status_code == 200

def test_scrapes_correct_number_of_books():
    scraper = Scraper("romance", 10)
    df= scraper.scrape_data()
    assert len(df) == 10

def test_scrapes_and_converts_to_csv():
    scraper = Scraper("romance", 3)
    df= scraper.scrape_data()
    assert scraper.create_csv(df, "books") is None
