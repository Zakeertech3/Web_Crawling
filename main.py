# main.py
import logging
from scrapers import DataScraper
from etl import DataLoader

# Configure logger.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    """
    Execute the complete data pipeline:
      1. Extract: Fetch data from FakeStoreAPI and DummyJSON.
      2. Transform: (Implicit via ETL conversion of nested structures.)
      3. Load: Insert the data into both SQLite and MongoDB.
    """
    logger.info("🚀 Starting data pipeline execution...")

    # --- Extract Phase ---
    logger.info("🔄 Fetching data from APIs...")
    data_fakestore = DataScraper.fetch_fakestore_data()
    data_dummyjson = DataScraper.fetch_dummyjson_data()

    # --- Load Phase ---
    loader = DataLoader()
    
    if data_fakestore:
        logger.info("🔄 Loading FakeStoreAPI data into databases...")
        loader.load_to_sql(data_fakestore, "fakestore")
        loader.load_to_mongo(data_fakestore, "fakestore")
    else:
        logger.warning("⚠️ No FakeStoreAPI data to load.")

    if data_dummyjson:
        logger.info("🔄 Loading DummyJSON data into databases...")
        loader.load_to_sql(data_dummyjson, "dummyjson")
        loader.load_to_mongo(data_dummyjson, "dummyjson")
    else:
        logger.warning("⚠️ No DummyJSON data to load.")

    logger.info("🎉 Data pipeline execution complete.")

if __name__ == "__main__":
    run_pipeline()
