import streamlit as st
import pandas as pd
import numpy as np
import PyPDF2
from io import BytesIO

def main():
    st.title("FinanceEconTool")
    st.subheader("Upload your class files for analysis and insights!")

    # Class Selection
    class_option = st.selectbox(
        "Which class does this file pertain to?",
        ["Math for Finance and Analytics with R", "Analytics for Finance", "Database Management Systems - SQL", 
         "Data Science with Python", "Econometrics"]
    )
    
    uploaded_files = st.file_uploader("Upload Files", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=True)

    if uploaded_files:
        if st.button("Analyze"):
            for file in uploaded_files:
                st.subheader(f"Analysis for {file.name}")

                if '.csv' in file.name:
                    df = pd.read_csv(file)
                    st.write(df.head())

                elif '.xlsx' in file.name:
                    df = pd.read_excel(file, engine='openpyxl')
                    st.write(df.head())

                elif '.pdf' in file.name:
                    pdf_reader = PyPDF2.PdfFileReader(file)
                    text = ""
                    for page_num in range(pdf_reader.numPages):
                        text += pdf_reader.getPage(page_num).extractText()
                    st.text_area("PDF Content", text, height=300)

                # You can customize the analysis based on the class selected
                st.write(f"Data Statistics for {file.name}")
                st.write(df.describe())

                # Generate insights or recommendations based on analyses
                st.subheader("Recommendations and Skills Insights")
                if class_option == "Math for Finance and Analytics with R":
                    st.write("1. Master the integration of complex financial equations.")
                    st.write("2. Use R for deeper data analysis and visualizations.")
                    st.write("**Key Hard Skills**: Quantitative Finance, Empirical Finance Research")
                    
                elif class_option == "Analytics for Finance":
                    st.write("1. Grasp time-series analysis for financial forecasting.")
                    st.write("2. Delve into optimization techniques.")
                    st.write("**Key Hard Skills**: Optimization Modeling, Forecasting")
                    
                elif class_option == "Database Management Systems - SQL":
                    st.write("1. Master SQL queries for complex data retrieval.")
                    st.write("2. Understand the architecture of relational databases.")
                    st.write("**Key Hard Skills**: Database Optimization, Data Structuring")
                    
                elif class_option == "Data Science with Python":
                    st.write("1. Understand ML models for financial prediction.")
                    st.write("2. Master pandas for data manipulation.")
                    st.write("**Key Hard Skills**: Panel Data Analysis, Data Visualization")
                    
                elif class_option == "Econometrics":
                    st.write("1. Dive into multiple regression models.")
                    st.write("2. Understand causality and potential pitfalls.")
                    st.write("**Key Hard Skills**: Empirical Finance Research, Forecasting")

if __name__ == '__main__':
    main()
