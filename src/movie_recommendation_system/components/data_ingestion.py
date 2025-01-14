from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
import os
import sys
from pathlib import Path

@dataclass
class DataIngestionConfig():
    raw_data_path = Path('artifacts/raw_data.csv')
    

class DataIngestion():
    
    def __init__(self):
        self.config = DataIngestionConfig()
        
        
    def initiate_data_ingestion(self):
        
        try:
            logging.info("Data Ingestion is Initiated")
        
            os.makedirs(os.path.dirname(self.config.raw_data_path),exist_ok=True)
            
            movies = pd.read_csv('notebooks/data/tmdb_5000_movies.csv')
            credit = pd.read_csv('notebooks/data/tmdb_5000_credits.csv')
            
            movies=movies.merge(credit,on='title')
            # logging.info(movies.head().to_string())
            
            movies.to_csv(self.config.raw_data_path)
            
            logging.info("Data Ingestion Is Completed")
            
            return self.config.raw_data_path       
        except Exception as e:
            logging.error(f'Error occurred in data ingestion due to {e}')
            raise CustomException(e,sys)