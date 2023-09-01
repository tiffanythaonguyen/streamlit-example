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

# Main function for the "What" page
def what_page():
    st.title("What")
    
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

# Second page function for the "Why" page
def why_page():
    st.title("Why")
    st.write("This is the 'Why' page in the app.")

# Third page function for the "How" page
def how_page():
    st.title("How")
    st.write("This is the 'How' page in the app.")

# App navigation
app_pages = {
    "What": what_page,
    "Why": why_page,
    "How": how_page,
}

selected_page = st.sidebar.radio("Select a page", list(app_pages.keys()))
app_pages[selected_page]()

if __name__ == "__main__":
    what_page()  # Start with the "What" page by default
