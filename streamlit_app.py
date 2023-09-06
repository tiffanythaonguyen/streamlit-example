import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

# Set page layout to wide
st.set_page_config(layout="wide")

# Title with business context and emojis
st.title("📊 Financial Data Cleaning and Analysis 📈")

# Introduction explaining the app's purpose
st.markdown("""
This app empowers you to clean and analyze financial data efficiently. It performs data quality checks and guides you through the cleaning process using Mitosheet.

To use the app:
1. Click **📥 Import** > **Import Files** and select your financial data file (CSV or Excel).
2. Configure the import settings.
3. Utilize Mitosheet to clean and transform the data based on the prompts.
4. 📥 Download the cleaned data for further analysis.

This app's goal is to go beyond the "what" and explore the "why" of financial data in real-time.
""")

# List of data quality checks and prompts
CHECKS_AND_PROMPTS = [
    (
        lambda df: df.columns[0] != 'issue date',
        'Rename the first column to "issue date".',
        'Double-click on the column name to edit it.'
    ),
    (
        lambda df: df["issue date"].dtype != "datetime64[ns]",
        'Change the data type of "issue date" to datetime.',
        'Click the Filter icon, and select "datetime" from the dtype dropdown.'
    ),
    (
        lambda df: df["issue date"].isnull().sum() > 0,
        'Remove null values from the "issue date" column.',
        'Use the filter icon in the column header and select "Is Not Empty".'
    ),
    (
        lambda df: "Notes" in df.columns,
        'Delete the "Notes" column (last column).',
        'Select the column header and press Delete.'
    ),
    (
        lambda df: df["term"].dtype != "int64",
        'Extract the number of months from the "term" column.',
        'Double-click on a cell in the column and write the formula `=INT(LEFT(term, 3))`.'
    ),
]

# Function to run data checks and display prompts
def run_data_checks_and_display_prompts(df):
    for check, error_message, help_text in CHECKS_AND_PROMPTS:
        if check(df):
            st.error(error_message + " " + help_text)
            return False
    return True

# Display Mitosheet for data cleaning
st.write("💼 Financial Data Cleaning Spreadsheet:")
dfs, _ = spreadsheet()

# Check if data is imported
if len(dfs) == 0:
    st.info("Please import your financial data file to begin. Click **📥 Import** > **Import Files** and select your file.")

# Run data checks and prompts
else:
    df = list(dfs.values())[0]
    checks_passed = run_data_checks_and_display_prompts(df)

    if checks_passed:
        st.success("✅ All checks passed! The data is clean and ready for download.")
        
        # Function to convert DataFrame to CSV
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')
        
        # Download button for cleaned data
        cleaned_data_csv = convert_df_to_csv(df)
        st.download_button("📥 Download Cleaned Data", cleaned_data_csv, "cleaned_data.csv", "text/csv")
