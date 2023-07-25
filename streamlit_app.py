import streamlit as st
import pandas as pd
import pdfreader
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker
import plotly.graph_objs as go

# Define the function to extract content from various file types and return them
def extract_content_from_file(file):
    if '.csv' in file.name:
        df = pd.read_csv(file)
        return df
    elif '.pdf' in file.name:
        reader = pdfreader.SimplePDFViewer(file)
        reader.navigate(1)
        reader.render()
        text = " ".join(reader.canvas.strings)
        return text
    return None

# Define the function to get top technical words from the content
def get_top_technical_words(text, top_n=10):
    words = text.split()
    word_freq = pd.Series(words).value_counts()
    top_words = word_freq.head(top_n)
    return top_words

# Define the main function for your Streamlit app
def main():
    st.title("FinanceEconTool 💼📈🔬")
    st.subheader("Upload your class files for data collection and processing 📊💡📚")

    # Initialize content with None
    content = None

    # File Uploader
    uploaded_files = st.file_uploader("Upload Files", type=['csv', 'pdf'], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            # If CSV file
            if '.csv' in file.name:
                data = pd.read_csv(file)
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

            # If PDF file
            elif '.pdf' in file.name:
                content = extract_content_from_file(file)
                st.text_area("PDF Content", content, height=300)

            else:
                st.write("Unsupported file format or empty content.")

    # Summary Insights
    st.header("Summary Insights 📊")

    # Example insights (you can replace this with actual insights based on data analysis)
    st.markdown(
        """
        - The data shows a positive correlation between "Finance" and "Economics".
        - The average word count per document is 1500 words.
        - The most common topic in the documents is "Financial Modeling".
        """
    )

    # Interactive Charts
    st.header("Interactive Charts 📉")

    # Example chart (you can replace this with actual charts based on data visualization)
    data = pd.DataFrame({
        "Topic": ["Finance", "Economics", "Financial Modeling", "Quantitative Finance", "Data Science"],
        "Frequency": [45, 32, 27, 15, 10]
    })

    fig = go.Figure(go.Bar(
        x=data["Topic"],
        y=data["Frequency"],
        marker_color='rgb(26, 118, 255)'
    ))

    fig.update_layout(
        title="Frequency of Topics",
        xaxis_title="Topic",
        yaxis_title="Frequency",
    )

    st.plotly_chart(fig)

    # Recommendations
    st.header("Recommendations 🔍")

    # Example recommendations (you can replace this with actual recommendations based on data analysis)
    st.markdown(
        """
        Based on the data analysis, we recommend focusing on the following areas:
