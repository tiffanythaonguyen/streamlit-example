import streamlit as st
import re  # Importing the regular expression library

# Function to identify numerical values in the text
def identify_numerical_values(doc):
    # Identify $100,000 format
    dollar_values = re.findall(r'\$\d{1,3}(?:,\d{3})*', doc)
    # Identify % format
    percent_values = re.findall(r'\d{1,3}%', doc)
    # Identify "by 'year'" format
    by_year_values = re.findall(r'by \d{4}', doc)
    
    return dollar_values, percent_values, by_year_values

# Main function
def main():
    st.title("Business Analysis")
    
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

        # Your existing code for keyword extraction can go here

if __name__ == "__main__":
    main()
