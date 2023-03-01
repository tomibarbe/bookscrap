import requests
import time
import math
from datetime import datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

class ScraperError(Exception):
    pass


class Scraper:

    """
    Webscraping program for gathering data on different genres from the Book Depository website
    """

    def __init__(self, keyword: str, number_of_items: int, availability: str, sortBy: str, format: str) -> None:
        """
        Initialises the object instance
        Args:
           keyword (str): The genre of book to scrape
           number_of_items (int): Number of pages to scrape
           availability (str): "1" for in-stock, "2" for pre-order, nothing for both
           sortBy (str): "popularity", ...others
           format (str): "1" for paperback, ...others (see on webpage), nothing for everything

        Returns:
            None
        """

        self.__headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
        self.keyword = keyword
        self.availability = availability
        self.sortBy = sortBy
        self.format = format
        self.number_of_items = number_of_items
       
    def get_url(self) -> list:
        """
        Fetches the urls of the pages to be scraped

        Returns:
            urls (list): Urls of the pages to be scraped
            
        """
        base_url= f"https://www.bookdepository.com/search?searchTerm={self.keyword}&format={self.format}&availability={self.availability}&searchSortBy={self.sortBy}"
        url_separator= "&page="
        pages= math.ceil(self.number_of_items)
        urls= []
        for page_num in range(1, pages + 1):
                page_num= str(page_num)
                if page_num == '0' or page_num == '1':
                    url = base_url
                else:
                    url = base_url + url_separator + page_num
                urls.append(url)
        return urls

    def request_page(self, url: str) -> requests.Response:
        """
        Makes a request to the webpage to be scraped
        Args:
            url (str): Url of the page to be scraped

        Returns:
            page (requests.Response): Object containing the server's response to the HTTP request    
                
        """ 
        page= requests.get(url, self.__headers)
        if page.status_code != 200:
            print("Error processing request")
        return page

    def create_soup(self, page: requests.Response):
        """
        Parses the html
        Args:
            page (requests.Response): Object containing the server's response to the HTTP request 

        Returns:
            soup: bs4.BeautifulSoup object
            
        """
        soup= BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_book_title(self, soup) -> str:
        """
        Extracts the title of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            title (str): title of the book
            
        """
        title = None
        try:
            title= soup.find('meta', {'itemprop': "name"})['content']  
        except ScraperError:
            raise ScraperError
        finally:
            return title
        
    def get_book_image(self, soup) -> str:
        """
        Extracts the title of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            title (str): title of the book
            
        """
        title = None
        try:
            title= soup.find('img')['src']
        except ScraperError:
            raise ScraperError
        except KeyError:
            title = soup.find('img')['data-lazy']
        finally:
            return title
        
    def get_book_author(self, soup) -> str:
        """
        Extracts the author of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            price (float): Price of the book
            
        """
        author = None
        try:
            author = soup.find('span', {'itemprop': "name"}).text
        except ScraperError:
            raise ScraperError     
        finally:
            return author

    def get_book_format(self, soup) -> str:
        """
        Extracts the format of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            format (str): Edition of the book
            
        """
        format = None
        try:
            format= soup.find('p', {'class': "format"}).text  
        except ScraperError:
            raise ScraperError     
        finally:
            return format

    def get_publication_date(self, soup)-> str:
        """
        Extracts the publication date of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            date_published (str): publication date of the book
            
        """
        date_published = None
        try:
            date_published = soup.find('p', {'class': "published"}).text
        except ScraperError:
            raise ScraperError     
        finally:
            return date_published
            
    def get_book_ISBN(self, soup) -> str: 
        """
        Extracts the ISBN of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            ISBN (str): ISBN of the book
            
        """
        isbn = None
        try:
            isbn = soup.find("meta", {"itemprop": "isbn"})['content']     
        except ScraperError:
            raise ScraperError     
        finally:
            return isbn

    def get_book_rating(self, soup) -> str:
        """
        Extracts the rating of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            rating (str): rating of the book
            
        """
        rating = None
        try:
            rating= str(len(soup.find_all('span', {'class': "star full-star"}))) + '/5'
        except ScraperError:
            raise ScraperError
        
        finally:
            return rating

    def get_book_price(self, soup) -> str:
        """
        Extracts the price of the book from the parsed BeautifulSoup object

        Args:
            soup (bs4.BeautifulSoup object): parsed html of the item page

        Returns:
            price (str): Price of the book
            
        """
        price = None
        try:
            price = soup.find('span', {'class': "sale-price"}).text
        except ScraperError:
            raise ScraperError     
        finally:
            return price
           
    def create_dataframe(self, data_list: list, columns:list) -> pd.DataFrame:
        """
        Creates a dataframe from a list

        Args:
            data_list (list): list of values
            columns (list): column labels to use for the resulting dataframe

        Returns:
            data (pd.DataFrame): a dataframe of the list of values 
        """
        data= pd.DataFrame(data_list, columns= columns)
        return data


    def create_csv(self, data: pd.DataFrame, file_title: str) -> None:
        """
        Converts a dataframe to a csv

        Args:
            data (pd.DataFrame): the dataframe to be converted to csv
            file_title (str): title of the output file

        Returns:
            None   
        """
        data.to_csv(f'{file_title}.csv', index= False)

    def scrape_data_lite (self) -> pd.DataFrame:
        """
        Scrapes the Book Depository website and returns a dataframe of the specific genre.

        Returns:
            data: A dataframe of all the books scraped
        """
        data_list= [] 
        urls= self.get_url()
        for url in urls:
            page= self.request_page(url)
            soup= self.create_soup(page)
            books= soup.find_all('div', {'class': "book-item"})
            num_book= 0
            for book in books:
                title= self.get_book_title(book)
                author= self.get_book_author(book)
                format= self.get_book_format(book)
                image= self.get_book_image(book)
                date_published= self.get_publication_date(book)
                isbn= self.get_book_ISBN(book)
                rating= self.get_book_rating(book)
                price= self.get_book_price(book) 
                data_list.append([self.keyword, title, author, format, image,
                                    date_published, isbn,
                                    rating, price
                                    ])
                num_book+= 1
                print (f'{num_book} book(s) has been scraped and appended')
        data= self.create_dataframe(data_list, columns= ["genre", "title", "author", "format", "image",
                                "date_published", "ISBN",
                                "rating", "price"
                                ])
        return data
