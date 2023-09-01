import streamlit as st
import re  # Importing the regular expression library

# Function to identify numerical values and the next two words after each value
def identify_numerical_values(doc):
    # Identify $100,000 format
    dollar_values = re.findall(r'(\$\d{1,3}(?:,\d{3})*)(?:\s+(\w+\s+\w+))?', doc)
    # Identify % format
    percent_values = re.findall(r'(\d{1,3}%)(?:\s+(\w+\s+\w+))?', doc)
    # Identify whole numbers with commas
    whole_numbers = re.findall(r'(\b\d{1,3}(?:,\d{3})*\b)(?:\s+(\w+\s+\w+))?', doc)
    # Identify decimal numbers in x.x or x.xx format
    decimal_numbers = re.findall(r'(\b\d+\.\d{1,2}\b)(?:\s+(\w+\s+\w+))?', doc)
    # Identify months
    months = re.findall(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', doc)
    # Identify years in xxxx format
    years = re.findall(r'\b\d{4}\b', doc)
    
    return dollar_values, percent_values, whole_numbers, decimal_numbers, months, years

# Main function
def main():
    st.title("Business Analysis")
    
    st.markdown("## 📌 Paste Document")
    
    # Text area for document input
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    # Button to trigger analysis
    if st.button("Analyze Text"):
        
        # Identify numerical values and the next two words after each value
        dollar_values, percent_values, whole_numbers, decimal_numbers, months, years = identify_numerical_values(doc)
        
        # Display identified values
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified whole numbers: {whole_numbers}")
        st.write(f"Identified decimal numbers: {decimal_numbers}")
        st.write(f"Identified months: {months}")
        st.write(f"Identified years: {years}")

        # Your existing code for keyword extraction can go here

if __name__ == "__main__":
    main()
