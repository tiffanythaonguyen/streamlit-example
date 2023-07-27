import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go
import statsmodels.api as sm
from linearmodels import PanelOLS

# Fetch data from FRED API
def fetch_fred_data(series, start_date, end_date):
    df = pdr.DataReader(series, 'fred', start_date, end_date)
    return df

# Basic statistical analysis
def analyze_data(df):
    st.write(f"Total Columns: {df.shape[1]}")
    st.write(f"Total Rows: {df.shape[0]}")
    st.write(f"Index: {df.index}")
    for column in df.columns:
        st.write(f"Unique values in {column}: {df[column].nunique()}")

    # Regression (assuming last column as dependent variable)
    X = df.iloc[:, :-1]
    X = sm.add_constant(X)
    y = df.iloc[:, -1]
    model = sm.OLS(y, X).fit()
    st.write(model.summary())

# Panel data analysis
def panel_data_analysis(df):
    # Assuming 'id' and 'time' columns for entities and time respectively
    dependent = df.iloc[:, -1]
    exog = sm.add_constant(df.iloc[:, :-2])
    panel_data = df.set_index(['id', 'time'])
    mod = PanelOLS(dependent, exog, entity_effects=True)
    res = mod.fit(cov_type='clustered', cluster_entity=True)
    st.write(res)

# File Upload and Analysis
def file_upload_analysis():
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())
        analyze_data(data)

        # Check for panel data analysis feasibility
        if 'id' in data.columns and 'time' in data.columns:
            panel_data_analysis(data)

# Government Data Analysis (from uploaded file)
def gov_data_analysis():
    st.title("Government Data Analysis")
    
    # Define the series codes for Treasury Rate, Housing Supply, and GDP
    series_codes = ['GS10', 'HOUST', 'GDP']

    # Define the date range for the forecast
    start_date = '2020-01-01'
    end_date = '2023-12-31'

    for series in series_codes:
        st.subheader(f"Data for {series}:")

        # Fetch data from FRED API
        df = fetch_fred_data(series, start_date, end_date)

        # Display the data
        st.write(df)

        # Plot the data using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df[series], mode='lines', name=series))
        fig.update_layout(title=f"Time Series Plot for {series}", xaxis_title="Date", yaxis_title=series)
        st.plotly_chart(fig)

    st.write("For more detailed data, please visit the following FRED links:")
    st.markdown("[Treasury Rate (GS10)](https://fred.stlouisfed.org/series/GS10)")
    st.markdown("[Housing Supply (HOUST)](https://fred.stlouisfed.org/series/HOUST)")
    st.markdown("[GDP](https://fred.stlouisfed.org/series/GDP)")

# ... [the rest of your functions: home, fred_data_analysis, future_of_finance, python_finance]

# Main App
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", 
                                  "Government Data Analysis", 
                                  "FRED Data Analysis", 
                                  "Future of Finance: 2030", 
                                  "Python and Finance",
                                  "File Upload and Analysis"])

if page == "Home":
    home()
elif page == "Government Data Analysis":
    gov_data_analysis()
elif page == "FRED Data Analysis":
    fred_data_analysis()
elif page == "Future of Finance: 2030":
    future_of_finance()
elif page == "Python and Finance":
    python_finance()
elif page == "File Upload and Analysis":
    file_upload_analysis()


