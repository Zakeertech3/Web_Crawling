# 🛍️ E-commerce Price Monitoring Dashboard

Welcome to the **E-commerce Price Monitoring Dashboard** – a sleek, end-to-end data pipeline solution that fetches, transforms, and displays product data from multiple e-commerce APIs in real time. 🚀

![Dashboard Preview](![Image](https://github.com/user-attachments/assets/eb6765c8-cac5-44e4-866a-e4416366b499))

## Overview

This project is designed to:
- **Extract** data from two awesome APIs:  
  - **FakeStoreAPI**  
  - **DummyJSON**
- **Transform** the data by converting nested structures (dictionaries and lists) into JSON strings for SQL compatibility.
- **Load** the data into both an **SQLite** database and **MongoDB**.
- **Display** the latest product information using a highly interactive, emoji-enhanced **Streamlit** dashboard.

Access the live dashboard here: [Live Dashboard](https://webcrawling-84mcpsiwjnpdxe8iijpth8.streamlit.app/) 🌐

## Features

- **Real-Time Data Pipeline**: Fetches and processes product data from multiple sources.
- **Robust ETL Layer**: Transforms nested data structures into SQL-friendly formats.
- **Dual Storage**: Stores data in both SQL (SQLite) and NoSQL (MongoDB) databases.
- **Interactive Dashboard**: Custom CSS, session state management, and a unique tabbed layout for a polished user experience.
- **Seamless Deployment**: Easily deployable on [Streamlit Cloud](https://streamlit.io/cloud).

## Tech Stack

- **Python** – The backbone of our project.
- **Requests** – For fetching data from APIs.
- **Pandas** – For data manipulation.
- **SQLAlchemy** – For SQL database interactions.
- **PyMongo** – For MongoDB connectivity.
- **Streamlit** – For building our interactive dashboard.
- **Logging** – For robust monitoring and debugging.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Zakeertech3/Web_Crawling.git
cd ecommerce-dashboard
