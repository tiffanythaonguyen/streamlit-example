import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Mito Spreadsheet Automation for Financial Data")

    # Initialize an empty DataFrame
    empty_df = pd.DataFrame()

    # Display empty DataFrame as a table in Streamlit
    st.write("Empty Spreadsheet:")
    st.write(empty_df)

    # Upload CSV or Excel file
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Read and display the uploaded data
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')

            st.write("Uploaded Spreadsheet:")
            st.write(df)

            # Perform basic statistical summaries using NumPy
            if st.button("Show Basic Statistics"):
                st.write("Mean of each column:")
                st.write(np.mean(df))

                st.write("Standard Deviation of each column:")
                st.write(np.std(df))

                st.write("Correlation Matrix:")
                st.write(np.corrcoef(df.values, rowvar=False))

        except Exception as e:
            st.write("There was an error loading the file.")
            st.write(e)

if __name__ == "__main__":
    main()
