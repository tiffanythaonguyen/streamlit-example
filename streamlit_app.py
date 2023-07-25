# main.py
import streamlit as st
import numpy as np
import pandas as pd
import PyPDF2
from io import BytesIO

# For econometrics
import statsmodels.api as sm
from statsmodels.sandbox.regression.gmm import IV2SLS

def get_data(data):
    # Handle data upload types
    if '.csv' in data.name:
        df = pd.read_csv(data)
    elif '.pdf' in data.name:
        # Extract text using PyPDF2
        pdf_reader = PyPDF2.PdfFileReader(data)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        st.text_area("Extracted PDF Text", text, height=300)  # Displaying extracted text for now
        return None  # Adjust this as needed
    elif '.xlsx' in data.name:
        df = pd.read_excel(data, engine='openpyxl')
    return df

def show_summary(df, analysis_type):
    # Show summary based on analysis type
    if df is not None:
        st.write(f"## {analysis_type}")

        dependent_var = st.selectbox('Choose Dependent Variable', df.columns)
        independent_vars = st.multiselect('Choose Independent Variables', df.columns, default=[col for col in df.columns if col != dependent_var])

        X = df[independent_vars]
        y = df[dependent_var]

        if analysis_type == 'OLS':
            X = sm.add_constant(X)  # adding a constant
            model = sm.OLS(y, X).fit()
            st.write(model.summary())
        # Continue for other analysis types ...

def main():
    st.title("Econometric Tools for Business Decisions")

    # Upload data section
    data_files = st.file_uploader("Upload your company data (CSV, Excel, PDF)", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=True)
    analysis_type = st.sidebar.selectbox("Choose Analysis Type", ("Home", "OLS", "Multivariable Regression", "R Application", "Machine Learning"))

    if data_files and analysis_type != "Home":
        col1, col2, col3 = st.beta_columns(3)

        with col1:
            csv_files = [file for file in data_files if '.csv' in file.name]
            for file in csv_files:
                df = get_data(file)
                st.write(f"### Summary for file: {file.name}")
                show_summary(df, analysis_type)

        with col2:
            xlsx_files = [file for file in data_files if '.xlsx' in file.name]
            for file in xlsx_files:
                df = get_data(file)
                st.write(f"### Summary for file: {file.name}")
                show_summary(df, analysis_type)

        with col3:
            pdf_files = [file for file in data_files if '.pdf' in file.name]
            for file in pdf_files:
                df = get_data(file)
                st.write(f"### Summary for file: {file.name}")
                show_summary(df, analysis_type)

    st.markdown("### Check out the full app [here](https://tiffanythaonguyen-streamlit-example-streamlit-app-pia2qx.streamlit.app/)!")

if __name__ == '__main__':
    main()
