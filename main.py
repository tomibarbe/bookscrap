from scraper import Scraper
from preprocess import ProcessData
import pandas as pd



def main():
    genres = ["romance", "horror", "thriller", "health", "anime", "biography"]
    number_of_items = 10
    df_total= pd.DataFrame()
    for genre in genres:
        scraper = Scraper(genre, number_of_items)
        df = scraper.scrape_data()
        df_total= df_total.append(df)
    s= ProcessData() 
    clean_df= s.clean_dataframe(df_total)           
    scraper.create_csv(clean_df, "books")


if __name__ == "__main__":
    main()



