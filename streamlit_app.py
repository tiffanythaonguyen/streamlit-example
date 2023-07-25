import streamlit as st
import pandas as pd
import pdfreader
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker  # Necessary for MaxNLocator

def extract_content_from_file(file):
    """
    Extracts content from various file types and returns them.
    """
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

def main():
    st.title("FinanceEconTool 💼📈🔬")
    st.subheader("Upload your class files for data collection and processing 📊💡📚")

    # Class Selection
    class_option = st.selectbox(
        "Which class does this file pertain to?",
        ["Math for Finance and Analytics with R", "Analytics for Finance", "Database Management Systems - SQL", 
         "Data Science with Python", "Econometrics"]
    )

    # Sidebar header for Coursework
    st.sidebar.header("Coursework")

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

                # ... Add other plots here ...

            # If PDF file
            elif '.pdf' in file.name:
                content = extract_content_from_file(file)
                st.text_area("PDF Content", content, height=300)

            else:
                st.write("Unsupported file format or empty content.")

            # If you want to see basic statistics from CSV files
            if isinstance(content, pd.DataFrame):
                st.subheader(f"Data Statistics for {file.name}")
                st.write(f"Total Number of Rows: {len(content)}")
                st.write(f"Number of Columns: {len(content.columns)}")
                st.write(f"Columns: {', '.join(content.columns)}")
                st.write(f"Data Types:\n{content.dtypes}")
                st.write(f"Summary Statistics:\n{content.describe()}")

            # Summary Dashboard for Insights
            st.subheader("Summary Dashboard for Insights")
            if isinstance(content, pd.DataFrame):
                numeric_columns = content.select_dtypes(include='number').columns
                st.write(f"Summary Statistics for Numeric Columns:")
                st.write(content[numeric_columns].describe())
                st.write(f"Correlation Matrix for Numeric Columns:")
                st.write(content[numeric_columns].corr())

                st.write(f"Top 10 Key Technical Words:")

if __name__ == '__main__':
    main()
