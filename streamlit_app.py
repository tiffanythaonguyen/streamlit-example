import streamlit as st
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Function to identify numerical values in the text
def identify_numerical_values(doc):
    dollar_values = re.findall(r'\$\d+(\.\d{2})?|\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', doc)
    percent_values = re.findall(r'\d+(\.\d+)?%', doc)
    by_year_values = re.findall(r'by \d{4}', doc)
    return dollar_values, percent_values, by_year_values

# Function to identify keywords by frequency
def identify_keywords_by_frequency(doc):
    words = re.findall(r'\b\w+\b', doc.lower())
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    return Counter(filtered_words).most_common(10)

# Function to identify relationships between words
def identify_word_relationships(doc):
    words = re.findall(r'\b\w+\b', doc.lower())
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    bigram_finder = BigramCollocationFinder.from_words(filtered_words)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)
    return bigrams

# Main function
def main():
    st.title("BERT Keyword Extractor 🎈")
    
    st.markdown("## 📌 Paste Document")
    
    # Text area for document input
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    # Button to trigger analysis
    if st.button("Analyze Text"):
        
        # Identify numerical values
        dollar_values, percent_values, by_year_values = identify_numerical_values(doc)
        
        # Display identified values
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified 'by year' values: {by_year_values}")

        # Identify keywords by frequency
        keywords_by_frequency = identify_keywords_by_frequency(doc)
        st.write(f"Identified keywords by frequency: {keywords_by_frequency}")

        # Identify relationships between words
        word_relationships = identify_word_relationships(doc)
        st.write(f"Identified relationships between words: {word_relationships}")

if __name__ == "__main__":
    main()
