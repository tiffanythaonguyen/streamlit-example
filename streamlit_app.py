import streamlit as st
import pandas as pd
import PyPDF2
from io import BytesIO

def extract_content_from_file(file):
    """
    Extracts content from various file types and returns them.
    """
    if '.csv' in file.name:
        df = pd.read_csv(file)
        return df

    elif '.xlsx' in file.name:
        df = pd.read_excel(file, engine='openpyxl')
        return df

    elif '.pdf' in file.name:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        return text

    return None

def main():
    st.title("FinanceEconTool")
    st.subheader("Upload your class files for data collection and processing.")

    # Class Selection
    class_option = st.selectbox(
        "Which class does this file pertain to?",
        ["Math for Finance and Analytics with R", "Analytics for Finance", "Database Management Systems - SQL", 
         "Data Science with Python", "Econometrics"]
    )
    
    uploaded_files = st.file_uploader("Upload Files", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=True)

    if uploaded_files:
        if st.button("Process Files"):
            for file in uploaded_files:
                st.subheader(f"Content from {file.name}")
                content = extract_content_from_file(file)
                
                if isinstance(content, pd.DataFrame):
                    st.write(content.head())  # Display the top rows of the dataframe

                elif isinstance(content, str):
                    st.text_area("PDF Content", content, height=300)

                else:
                    st.write("Unsupported file format or empty content.")

                # If you want to see basic statistics from CSV or Excel files
                if isinstance(content, pd.DataFrame):
                    st.subheader(f"Data Statistics for {file.name}")
                    st.write(content.describe())

if __name__ == '__main__':
    main()
