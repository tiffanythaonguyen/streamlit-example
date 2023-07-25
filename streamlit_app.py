import streamlit as st
import pandas as pd
import pdfreader
from io import BytesIO
import pandera as pa
from scipy import stats

# Adjusting the primary color of the Streamlit app
st.set_page_config(
    page_title="FinanceEconTool",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
    theme={
        "primaryColor": "#FFC0CB",  # Light Pink
        "backgroundColor": "#EFEFEF",
        "secondaryBackgroundColor": "#F0F0F0",
        "textColor": "#262730",
        "font": "sans-serif",
    },
)

# Define schema for tidy dataset validation
schema = pa.DataFrameSchema({
    "Feedback": pa.Column(pa.String),
    "Hypothesis Test Question": pa.Column(pa.String),
    "Hypothesis Test Result": pa.Column(pa.String),
})

def extract_content_from_file(file):
    """
    Extracts content from various file types and returns them.
    """
    if '.csv' in file.name:
        df = pd.read_csv(file)
        return df

    elif '.pdf' in file.name:
        reader = pdfreader.SimplePDFViewer(file)
        reader.navigate(1)
        reader.render()
        text = " ".join(reader.canvas.strings)
        return text

    return None

def perform_hypothesis_test(question, text):
    # This is a placeholder hypothesis test.
    word_count = len(text.split())
    p_value = stats.binom_test(word_count, n=500, p=0.5)  # Hypothetical binomial test
    return "Accept" if p_value > 0.05 else "Reject"

def main():
    st.title("FinanceEconTool 💼📈🔬")
    st.subheader("Upload your class files for data collection and processing 📊💡📚")

    # Class Selection
    class_option = st.selectbox(
        "Which class does this file pertain to?",
        ["Math for Finance and Analytics with R", "Analytics for Finance", "Database Management Systems - SQL", 
         "Data Science with Python", "Econometrics"]
    )
    
    uploaded_files = st.file_uploader("Upload Files", type=['csv', 'pdf'], accept_multiple_files=True)

    if uploaded_files:
        if st.button("Process Files"):
            for file in uploaded_files:
                st.subheader(f"Content from {file.name}")
                content = extract_content_from_file(file)
                
                if isinstance(content, pd.DataFrame):
                    st.write(content.head())  # Display the top rows of the dataframe

                elif isinstance(content, str):
                    st.text_area("PDF Content", content, height=300)

                    # Hypothesis Testing
                    question = st.text_input("Ask a question about the document for hypothesis testing")
                    if question:
                        result = perform_hypothesis_test(question, content)
                        st.write(f"Hypothesis Test Result: {result}")

                else:
                    st.write("Unsupported file format or empty content.")

                # If you want to see basic statistics from CSV files
                if isinstance(content, pd.DataFrame):
                    st.subheader(f"Data Statistics for {file.name}")
                    st.write(content.describe())

if __name__ == '__main__':
    main()
