from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from src.movie_recommendation_system.components.data_ingestion import DataIngestion
from src.movie_recommendation_system.components.data_transformation import DataTransformation
from src.movie_recommendation_system.components.model_trainer import ModelTrainer





class Training_Pipeline():
    def __init__(self):
        self.data_ingestion=DataIngestion()
        self.data_transformation=DataTransformation()
        self.model_trainer=ModelTrainer()
    
    def run_pipeline(self):
        logging.info('Running Training Pipeline')
        data_path =self.data_ingestion.initiate_data_ingestion()
        print(data_path)
        data_set=self.data_transformation.initiate_data_transformation(data_path)
        self.model_trainer.initiate_model_trainer(data_set)
        
        
if __name__ == "__main__":
    obj = Training_Pipeline()
    obj.run_pipeline()