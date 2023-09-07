import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

# Set page layout to wide
st.set_page_config(layout="wide")

# Title with business context and emojis
st.title("📊 Data Cleanliness Verification 🧹")

# Introduction explaining the app's purpose
st.markdown("""
This Streamlit App allows you to import data and clean it using the mitosheet library. The app is preconfigured with a set of data checks and prompts you to fix specific issues in the data.

It ensures that your data has the following properties:
- The first column is the issue date, and it's of type datetime.
- The issue date column is a datetime column.
- There are no null values in the issue date column.
- The Notes column is not included in the dataframe.
- The term column is an integer.

**Why is this app useful?**
This app could be used in the first step of a data engineering pipeline. It allows data engineers to help data analysts ensure their data conforms to a specific schema before they continue their analysis.

In this app, only if the user has fixed all of the issues in their data will they be able to export the data to a CSV file. You could update this app to export the data to a database instead.

**Mito Streamlit Package**
Learn more about the Mito Streamlit package [here](https://mitosheet.mitotec.io/docs/streamlit/) or follow the [getting started guide](https://mitosheet.mitotec.io/docs/streamlit/getting-started/).

**Run Locally**
1. Create a virtual environment:
   ```python3 -m venv venv```
2. Activate the virtual environment:
   - macOS/Linux:
     ```source venv/bin/activate```
   - Windows:
     ```venv\Scripts\activate```
3. Install the required python packages:
   ```pip install -r requirements.txt```
4. Start the Streamlit app:
   ```streamlit run main.py```
""")

# Display Mitosheet for data cleaning
st.write("💼 Data Cleaning Spreadsheet:")
dfs, _ = spreadsheet()

# Check if data is imported
if len(dfs) == 0:
    st.info("Please import your data file to begin. Click **📥 Import** > **Import Files** and select your file.")

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

# Link to the deployed app
st.markdown("[View the deployed app here](https://tiffanythaonguyen-streamlit-example-streamlit-app-pia2qx.streamlit.app/)")
