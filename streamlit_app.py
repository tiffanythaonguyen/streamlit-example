import streamlit as st
import re
from pandas import DataFrame
from keybert import KeyBERT
import seaborn as sns

# Function to identify numerical values in the text
def identify_numerical_values(doc):
    dollar_values = re.findall(r'\$\d+(\.\d{2})?|\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', doc)
    percent_values = re.findall(r'\d+(\.\d+)?%', doc)
    by_year_values = re.findall(r'by \d{4}', doc)
    general_numerical_values = re.findall(r'\d+(\.\d+)?|\d{1,3}(?:,\d{3})*(?:\.\d+)?', doc)
    return dollar_values, percent_values, by_year_values, general_numerical_values

# Function to identify abbreviations and capitalized words
def identify_abbreviations_and_caps(doc):
    abbreviations = re.findall(r'\b[A-Z]{2,}\b', doc)
    capitalized_words = re.findall(r'\b[A-Z][a-z]+\b', doc)
    return abbreviations, capitalized_words

# Main function
def main():
    st.title("Keyword Extractor 🎈")
    
    st.markdown("## 📌 Paste Document")
    
    # Text area for document input
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    # Button to trigger analysis
    if st.button("Analyze Text"):
        
        # Identify numerical values
        dollar_values, percent_values, by_year_values, general_numerical_values = identify_numerical_values(doc)
        
        # Display identified values
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified 'by year' values: {by_year_values}")
        st.write(f"Identified general numerical values: {general_numerical_values}")

        # Identify abbreviations and capitalized words
        abbreviations, capitalized_words = identify_abbreviations_and_caps(doc)
        
        # Display identified abbreviations and capitalized words
        st.write(f"Identified abbreviations: {abbreviations}")
        st.write(f"Identified capitalized words: {capitalized_words}")

        # Initialize KeyBERT model
        kw_model = KeyBERT("distilbert-base-nli-mean-tokens")
        
        # Extract keywords
        keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None, top_n=10, diversity=0.5)
        
        # Display keywords
        df = DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"]).sort_values(by="Relevancy", ascending=False).reset_index(drop=True)
        df.index += 1
        st.table(df)

if __name__ == "__main__":
    main()
