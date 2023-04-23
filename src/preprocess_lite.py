import pandas as pd

class ProcessData:
    def __init__(self):
        pass

    def clean_dataframe(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocesses the data collected from the website

        Args:
            data (pd.DataFrame): The data scraped from the website

        Returns:
            clean_df (pd.DataFrame): Preprocessed data
            
        """
        data["title"] = data["title"].str.strip()
        data["author"] = data["author"].str.strip()
        data["format"] = data["format"].str.split().str[0]
        data["image"] = data["image"].str.split().str[0]
        data["date_published"] = pd.to_datetime(data["date_published"], format='%d %b %Y', errors='ignore')  
        data["ISBN"] = data["ISBN"].str.strip()
        data["rating"] = data["rating"].str.strip()
        data["price"] = data["price"].replace(regex=True, to_replace=r'[^0-9.\-]', value=r'')
        data.rename(columns={'price': 'price (gbp)'})
        return data
