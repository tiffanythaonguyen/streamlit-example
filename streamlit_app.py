import streamlit as st
import re  # Importing the regular expression library

# Function to identify numerical values and the next two words or any key after each value
def identify_numerical_values(doc):
    dollar_values = re.findall(r'(\$\d{1,3}(?:,\d{3})*)(?:\s+([\w\s\W]{1,20}))?', doc)
    percent_values = re.findall(r'(\d{1,3}%)(?:\s+([\w\s\W]{1,20}))?', doc)
    whole_numbers = re.findall(r'(\b\d{1,3}(?:,\d{3})*\b)(?!%)(?:\s+([\w\s\W]{1,20}))?', doc)
    decimal_numbers = re.findall(r'(\b\d+\.\d{1,2}\b)(?:\s+([\w\s\W]{1,20}))?', doc)
    months = re.findall(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', doc)
    years = re.findall(r'\b\d{4}\b', doc)
    
    return dollar_values, percent_values, whole_numbers, decimal_numbers, months, years

# Main function
def main():
    st.title("Business Analysis")
    
    st.markdown("## 📌 Paste Document")
    
    doc = st.text_area("Paste your text below (max 500 words)", height=200)
    
    if st.button("Analyze Text"):
        dollar_values, percent_values, whole_numbers, decimal_numbers, months, years = identify_numerical_values(doc)
        
        st.write(f"Identified dollar values: {dollar_values}")
        st.write(f"Identified percent values: {percent_values}")
        st.write(f"Identified whole numbers: {whole_numbers}")
        st.write(f"Identified decimal numbers: {decimal_numbers}")
        st.write(f"Identified months: {months}")
        st.write(f"Identified years: {years}")

if __name__ == "__main__":
    main()
