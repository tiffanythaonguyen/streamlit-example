import streamlit as st
import re  # Importing the regular expression library
import contextlib
import traceback
import textwrap

# Function to add vertical space
def add_vertical_space(num_lines: int = 1):
    """Add vertical space to your Streamlit app."""
    for _ in range(num_lines):
        st.write("")

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

     # Add vertical space
    add_n_lines = st.slider("Add n vertical lines below this", 1, 20, 5)
    add_vertical_space(add_n_lines)
    st.write("Dataframe")

    # Echo expander function for simple DataFrame example
    with echo_expander(code_location="below", label="Simple Dataframe example"):
        import pandas as pd
        df = pd.DataFrame(
            [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]],
            columns=("A", "B", "C", "D", "E"),
        )
        st.dataframe(df)

if __name__ == "__main__":
    main()
