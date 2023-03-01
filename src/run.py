from scraper import Scraper
from preprocess import ProcessData

scraper = Scraper("thriller", 10)
df= scraper.scrape_data()
s= ProcessData() 
clean_df= s.clean_dataframe(df)
scraper.create_csv(clean_df, "bookjs")
