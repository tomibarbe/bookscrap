from scraper_lite2 import Scraper
from preprocess_lite import ProcessData

scraper = Scraper("thriller", 1, "1", "popularity", "1")
df= scraper.scrape_data_lite()
s= ProcessData() 
clean_df= s.clean_dataframe(df)
scraper.create_csv(clean_df, "bwb_books_lite")
