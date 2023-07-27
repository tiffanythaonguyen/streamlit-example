import streamlit as st
import pandas_datareader as pdr
import plotly.graph_objects as go

# Define the function to fetch data from FRED API
def fetch_fred_data(series, start_date, end_date):
    df = pdr.DataReader(series, 'fred', start_date, end_date)
    return df

# Home Page
def home():
    st.title("Welcome to pyfiquant")
    st.write(
    "This app showcases the significance of data-driven decision-making, "
    "my coursework from my graduate program, and my interest in finance and Python."
    )

# World Economic Forum Insights
def wef_insights():
    st.title("World Economic Forum Insights")
    st.write(
    "Dive deeper into the financial landscape, innovations, and insights provided by the World Economic Forum."
    )
    st.markdown("[WEF Intelligence on Financial and Monetary Systems](https://intelligence.weforum.org/topics/a1Gb0000000LHOUEA4)")
    st.markdown("[Streamlit App Showcase](https://tiffanythaonguyen-streamlit-example-streamlit-app-pia2qx.streamlit.app/)")

# FRED Data Analysis
def fred_data_analysis():
    st.header("FRED Data Analysis 📈")
    series = st.selectbox("Choose a data series:", ['CSUSHPISA', 'GDP', 'UNRATE'])
    start_date = st.date_input("Start Date", '2020-01-01')
    end_date = st.date_input("End Date", '2023-12-31')
    
    if st.button("Fetch Data"):
        df = fetch_fred_data(series, start_date, end_date)
        st.write(f"Data for {series} from {start_date} to {end_date}:")
        st.write(df)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df[series], mode='lines', name=series))
        fig.update_layout(title=f"Time Series Plot for {series}", xaxis_title="Date", yaxis_title=series)
        st.plotly_chart(fig)

# Future of Finance Insights
def future_of_finance():
    st.title("Future of Finance: 2030")
    st.write(
    "The landscape of global finance is rapidly evolving with the advent of new technologies and shifts in geopolitical power. "
    "Here are some key insights and predictions for the financial world in 2030:"
    )
    st.subheader("Decentralization and The Decline of Dollar Dominance")
    st.write(
    "The centralized global monetary system, dominated by the US dollar, is transitioning to a multi-polar world "
    "with multiple reserve currencies. Currencies like the euro and renminbi may rise in prominence, reflecting "
    "broader global economic shifts."
    )
    st.subheader("Rise of Digital Money")
    st.write(
    "Digital currencies, both private and central-bank issued, are proliferating. This comes with implications "
    "for monetary and financial policymaking. Fintech innovations are driving this change, providing specialized "
    "financial services, including credit and payment solutions, through digital platforms. The acceptance and adoption "
    "of cryptocurrencies are expected to continue."
    )
    st.subheader("Transformation of Traditional Banking")
    st.write(
    "Fintech is set to revolutionize traditional banking and insurance models. New decentralized entities "
    "will emerge, offering liquidity and diverse financial services in a disintermediated manner. New technologies "
    "will introduce novel asset classes, directly connecting savers and borrowers, and commoditizing financial data. "
    "However, this also leads to potential fragmentation and market dislocations."
    )

# Python and Finance Insights
def python_finance():
    st.title("Python and Finance")
    st.write("Python has rapidly become a leading language in the financial sector, with tools and libraries that cater to a variety of tasks ranging from data analysis to trading strategy development.")
    st.write("Here, we will explore various Python tools, libraries, and methodologies pertinent to finance.")

# Main App
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", 
                                  "World Economic Forum Insights", 
                                  "FRED Data Analysis", 
                                  "Future of Finance: 2030", 
                                  "Python and Finance"])

if page == "Home":
    home()
elif page == "World Economic Forum Insights":
    wef_insights()
elif page == "FRED Data Analysis":
    fred_data_analysis()
elif page == "Future of Finance: 2030":
    future_of_finance()
elif page == "Python and Finance":
    python_finance()
