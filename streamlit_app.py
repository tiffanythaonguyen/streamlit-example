import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_description(df):
    """Generate a dynamic short description of the dataset."""
    num_cols = df.shape[1]
    num_rows = df.shape[0]
    description = f"This dataset contains {num_cols} columns and {num_rows} rows.\n\n"

    if 'year' in df.columns or 'date' in df.columns:
        description += "It seems to be time series data given the presence of a 'year' or 'date' column.\n\n"
    else:
        description += "The dataset appears to be cross-sectional as there's no evident 'year' or 'date' column.\n\n"

    return description

def analyze_data(df):
    # Basic insights
    st.write(f"Total Columns: {df.shape[1]}")
    st.write(f"Total Rows: {df.shape[0]}")
    st.write(f"Index: {df.index}")

    for column in df.columns:
        st.write(f"Unique values in {column}: {df[column].nunique()}")

    # Plot total of numeric columns in a bar graph
    sum_data = df.sum(numeric_only=True)
    fig, ax = plt.subplots(figsize=(12, 6))
    sum_data.plot(kind='bar', ax=ax)
    ax.set_title('Sum of Numeric Columns')
    ax.set_ylabel('Total')
    ax.set_xlabel('Columns')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig)

    # Snapshot of the data
    st.subheader("Snapshot of the Data")
    st.write(df.head())

    # Short description of the data
    st.subheader("Short Description")
    st.write(generate_description(df))

def main():
    st.title("PyFiQuant 💼📈🔬")
    
    st.sidebar.markdown("""
    **PyFiQuant** is designed to enhance data transparency, digitalization, 
    accountability, and inclusiveness in the realm of finance and economics.
    """)

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        if st.button("Analyze Data"):
            analyze_data(df)

if __name__ == "__main__":
    main()
