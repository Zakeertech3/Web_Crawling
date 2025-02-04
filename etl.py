# etl.py
import pandas as pd
import json
import logging
from sqlalchemy import create_engine
from pymongo import MongoClient

# Configure logger for this module.
logger = logging.getLogger(__name__)

class DataLoader:
    """
    Class responsible for loading data into SQL and MongoDB.
    """
    def __init__(self, sql_db_url="sqlite:///products.db", mongo_url="mongodb://localhost:27017/", mongo_db_name="products_db"):
        self.engine = create_engine(sql_db_url)
        self.mongo_client = MongoClient(mongo_url)
        self.mongo_db = self.mongo_client[mongo_db_name]

    def load_to_sql(self, data, table_name):
        """
        Loads data into a SQL table.
        Args:
            data: A list of dictionaries or a dict containing a 'products' key.
            table_name (str): The target table name.
        """
        try:
            # Convert data to a DataFrame.
            if isinstance(data, dict) and "products" in data:
                df = pd.DataFrame(data["products"])
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = pd.DataFrame(data)
            
            # Convert any dictionary or list values to JSON strings.
            for col in df.columns:
                if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
                    df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x)
            
            df.to_sql(table_name, con=self.engine, if_exists="replace", index=False)
            logger.info(f"✅ Data loaded into SQL table '{table_name}'.")
        except Exception as e:
            logger.error(f"❌ Error loading data into SQL table '{table_name}': {e}")

    def load_to_mongo(self, data, collection_name):
        """
        Loads data into a MongoDB collection.
        Args:
            data: A list of dictionaries or a dict containing a 'products' key.
            collection_name (str): The target collection name.
        """
        try:
            if isinstance(data, dict) and "products" in data:
                docs = data["products"]
            elif isinstance(data, list):
                docs = data
            else:
                docs = data
            
            collection = self.mongo_db[collection_name]
            collection.delete_many({})
            collection.insert_many(docs)
            logger.info(f"✅ Data loaded into MongoDB collection '{collection_name}'.")
        except Exception as e:
            logger.error(f"❌ Error loading data into MongoDB collection '{collection_name}': {e}")