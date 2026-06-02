import pandas as pd
from pathlib import Path

class Silver:
    def __init__(self):
        self.bronze_path = Path('data/bronze_data.csv')
        
    def clean_data(self):
        if self.bronze_path.exists():
            df = pd.read_csv(self.bronze_path)
            # Perform cleaning operations (e.g., drop duplicates, handle missing values)
            df.drop_duplicates(inplace=True)
            df.ffill(inplace=True)
            df['order_date'] = pd.to_datetime(df['order_date'])
            df.columns = df.columns.str.capitalize().str.replace(' ', '_')
            df['Unit_price'] = df['Unit_price'].astype(float)
            df['Quantity'] = df['Quantity'].astype(int)
            df['Total_amount'] = df['Total_amount'].astype(float)
            return df
        else:
            print("Bronze data not found.")
            return None

