import streamlit as st
import pandas as pd
import numpy as np
import mitosheet  # Import mitosheet library

def main():
    st.title("Financial Data Spreadsheet Automation")

    # Initialize an empty DataFrame
    empty_df = pd.DataFrame()

    # Display empty DataFrame as a table in Streamlit
    st.write("Welcome to the Financial Data Spreadsheet Automation App!")
    st.write("This app is designed to bridge the gap between profound human questions and quantitative research in the financial domain.")
    st.write("From philosophers pondering the nature of value to data engineers optimizing algorithms, from CFOs making strategic decisions to investors managing portfolios, this app provides a continuum of tools.")
    st.write("It empowers users to explore, analyze, and derive insights from financial data.")
    st.write("Use it to bring quantitative research to life, whether you're an academic researcher or a CEO shaping investment strategies.")

    st.write("Empty Spreadsheet:")
    
    # Create an empty spreadsheet using mitosheet
    empty_df = mitosheet.sheet(data=empty_df, key="empty_sheet")
    
    # Display the empty spreadsheet
    st.dataframe(empty_df)

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
            
            # Display the uploaded data using mitosheet
            df = mitosheet.sheet(data=df, key="uploaded_sheet")
            st.dataframe(df)

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
