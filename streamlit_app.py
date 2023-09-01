import streamlit as st
import re  # Importing the regular expression library

# Function to identify numerical values, months, and years in the text
def identify_numerical_values(doc):
    # Identify $100,000 format
    dollar_values = re.findall(r'\$\d{1,3}(?:,\d{3})*', doc)
    # Identify % format
    percent_values = re.findall(r'\d{1,3}%', doc)
    # Identify general numerical values
    general_numerical_values = re.findall(r'\b\d+\b', doc)
    # Identify months
    months = re.findall(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\b', doc, re.IGNORECASE)
    # Identify years
    years = re.findall(r'\b\d{4}\b', doc)
    
    return dollar_values, percent_values, general_numerical_values, months, years

# Main function
def main():
    st.title("Business Analysis")
    
    st.markdown("## 📌 Paste Document")
    
    # Text area for document input
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    # Button to trigger analysis
    if st.button("Analyze Text"):
        
        # Identify numerical values, months, and years
        dollar_values, percent_values, general_numerical_values, months, years = identify_numerical_values(doc)
        
        # Display identified values
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified general numerical values: {general_numerical_values}")
        st.write(f"Identified months: {months}")
        st.write(f"Identified years: {years}")

        # Your existing code for keyword extraction can go here

if __name__ == "__main__":
    main()
