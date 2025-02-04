# scrapers.py
import requests
import logging

# Configure logger for this module.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataScraper:
    """
    Class responsible for fetching data from external APIs.
    """

    @staticmethod
    def fetch_fakestore_data():
        """
        Fetch product data from FakeStoreAPI.
        Returns:
            data (list): JSON data containing products, or None if an error occurs.
        """
        url = "https://fakestoreapi.com/products"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            logger.info("✅ Fetched FakeStoreAPI data successfully.")
            return data
        except Exception as e:
            logger.error(f"❌ Error fetching FakeStoreAPI data: {e}")
            return None

    @staticmethod
    def fetch_dummyjson_data():
        """
        Fetch product data from DummyJSON.
        Returns:
            data (dict): JSON data containing products, or None if an error occurs.
        """
        url = "https://dummyjson.com/products"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            logger.info("✅ Fetched DummyJSON data successfully.")
            return data
        except Exception as e:
            logger.error(f"❌ Error fetching DummyJSON data: {e}")
            return None

    @staticmethod
    def fetch_all():
        """
        Fetch data from all configured APIs.
        Returns:
            dict: A dictionary with keys 'fakestore' and 'dummyjson'.
        """
        return {
            "fakestore": DataScraper.fetch_fakestore_data(),
            "dummyjson": DataScraper.fetch_dummyjson_data()
        }
