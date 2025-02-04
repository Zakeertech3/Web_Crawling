# streamlit_app.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import main  # Used to trigger the pipeline
import logging

# Set the page configuration as the first Streamlit command!
st.set_page_config(
    page_title="E-commerce Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO)

# --- Custom CSS for Unique Styling ---
st.markdown(
    """
    <style>
    /* Custom header style */
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
        padding-bottom: 10px;
    }
    /* Custom subheader style */
    .subheader {
        font-size: 1.25rem;
        color: #333333;
    }
    /* Sidebar custom background */
    .css-1d391kg {  
        background-image: linear-gradient(#2E8B57, #3CB371);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header & Title ---
st.markdown('<div class="header-title">🛍️ E-commerce Price Monitoring Dashboard</div>', unsafe_allow_html=True)
st.markdown("Welcome to the **E-commerce Price Monitoring Dashboard**! Use the sidebar controls to run the data pipeline and explore the latest product data. 🚀")

# --- Session State Initialization ---
if "pipeline_run" not in st.session_state:
    st.session_state.pipeline_run = False

# --- Sidebar Controls ---
st.sidebar.header("🚀 Pipeline Control")
if st.sidebar.button("Run Data Pipeline"):
    st.info("Pipeline is running, please wait...")
    main.run_pipeline()  # Execute the pipeline
    st.session_state.pipeline_run = True
    st.success("Pipeline executed successfully! 🎉")

# Do not show data explorer until the pipeline has been run.
if st.session_state.pipeline_run:
    st.sidebar.header("📊 Data Explorer")
    table_option = st.sidebar.selectbox("Choose a table to display", ["fakestore", "dummyjson"])
else:
    table_option = None

# --- Main Content ---
if not st.session_state.pipeline_run:
    st.warning("Please run the data pipeline using the sidebar control to view the data.")
else:
    # Connect to the SQLite database.
    engine = create_engine("sqlite:///products.db")
    try:
        df = pd.read_sql_table(table_option, con=engine)
        st.subheader(f"Data from **{table_option.capitalize()}**")
        # Create tabs for a unique layout.
        tab1, tab2 = st.tabs(["Table View", "Visualization"])
        with tab1:
            st.dataframe(df)
        with tab2:
            if "price" in df.columns:
                st.subheader("💰 Price Distribution")
                st.bar_chart(df["price"])
            else:
                st.info("No price data available for visualization.")
    except Exception as e:
        st.error(f"Error loading table '{table_option}': {e}")

# --- Footer ---
st.markdown("---")
st.markdown("👋 Made by Zakeer")