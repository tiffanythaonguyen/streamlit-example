import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader as pdr
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker
import plotly.graph_objs as go
from IPython.display import HTML

# Define the function to extract content from a CSV file and return it as a DataFrame
def extract_content_from_file(file):
    if '.csv' in file.name:
        df = pd.read_csv(file)
        return df
    return None

# Define the function to fetch data from FRED API
def fetch_fred_data(series, start_date, end_date):
    df = pdr.DataReader(series, 'fred', start_date, end_date)
    return df

# Define the main function for your Streamlit app
def main():
    st.title("FinanceEconTool 💼📈🔬")
    st.subheader("Upload your class files for data collection and processing 📊💡📚")

    # Initialize content with None
    content = None

    # File Uploader
    uploaded_files = st.file_uploader("Upload Files", type=['csv'], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            # If CSV file
            if '.csv' in file.name:
                data = extract_content_from_file(file)
                st.write(f"Data overview for {file.name}:")
                st.write(data.head())

                st.sidebar.header("Visualizations")
                plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot"]
                selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

                if selected_plot == "Bar plot":
                    x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
                    y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
                    st.write("Bar plot:")
                    fig, ax = plt.subplots()
                    sns.barplot(x=data[x_axis], y=data[y_axis], ax=ax)

                    # Modify the x-axis ticks
                    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=10))
                    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

                    st.pyplot(fig)

                # Add other plots here (e.g., Scatter plot, Histogram, Box plot)

                # Summary statistics DataFrame
                st.subheader("Summary Statistics")
                summary_stats_df = data.describe()
                st.write(summary_stats_df)

                # Correlation Matrix DataFrame
                st.subheader("Correlation Matrix")
                correlation_df = data.corr()
                st.write(correlation_df)

    # Fetch data from FRED API
    st.header("Forecasting using FRED API 📈")

    # Define the series codes for House_Price_Index, GDP, and Unemployment
    series_codes = ['CSUSHPISA', 'GDP', 'UNRATE']

    # Define the date range for the forecast
    start_date = '2020-01-01'
    end_date = '2023-12-31'

    for series in series_codes:
        st.subheader(f"Forecast for {series}:")

        # Fetch data from FRED API
        df = fetch_fred_data(series, start_date, end_date)

        # Display the data
        st.write(df)

        # Plot the data using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df[series], mode='lines', name=series))
        fig.update_layout(title=f"Time Series Plot for {series}", xaxis_title="Date", yaxis_title=series)
        st.plotly_chart(fig)

    # Recommendations
    st.header("Recommendations 🔍")

    # Example recommendations (you can replace this with actual recommendations based on data analysis)
    st.markdown(
        """
        Based on the data analysis, we recommend focusing on the following areas:
        - **House_Price_Index**: Analyze the trend and perform a forecast to identify potential investment opportunities in the housing market.
        - **GDP**: Monitor the GDP growth rate and plan financial strategies accordingly for business development.
        - **Unemployment**: Keep an eye on the unemployment rate and its impact on the economy to make informed decisions.

        Remember that these are just preliminary insights, and further analysis may reveal more specific areas for investigation.
        """
    )

    # Display the FRED embedded links
    st.header("FRED Embedded Links 📈")
    iframe_code = '''
    <iframe style="border: 1px solid #333333; overflow: hidden; width: 190px; height: 490px;" src="//research.stlouisfed.org/fred-glance-widget.php" height="240" width="320" frameborder="0" scrolling="no"></iframe>

    <<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=175Js&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden; width:670px; height:525px;" allowTransparency="true" loading="lazy"></iframe>>
    '''

    st.components.v1.html(iframe_code)

# Rest of the code...

# Run the app when the script is executed
if __name__ == '__main__':
    main()

