import streamlit as st
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
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
    
    # Regression analysis
    if 'prcc_f' in df.columns and all(col in df.columns for col in ['sale', 'cogs', 'ppegt']):
        X = df[['sale', 'cogs', 'ppegt']].dropna()
        y = df.loc[X.index, 'prcc_f']
        X = sm.add_constant(X)  # adding a constant
        model = sm.OLS(y, X).fit()
        st.write(model.summary())

        # Correlation heatmap
        st.subheader('Correlation Matrix')
        corr = df[['prcc_f', 'sale', 'cogs', 'ppegt']].corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, ax=ax, cmap="coolwarm", linewidths=.5, fmt=".2f")
        st.pyplot(fig)
    else:
        st.warning("The necessary columns for regression analysis are not found in the uploaded CSV.")

    # Short description of the data
    st.subheader("Short Description")
    st.write(generate_description(df))

def main():
    st.title("PyFiQuant 💼📈🔬")
    st.write("""
    **Principles of this Exercise**:
    - **Data Transparency**: Openness about data sources, methodologies, and assumptions.
    - **Digitalization**: Using modern methods and tools for data processing and presentation.
    - **Accountability**: Taking responsibility for data accuracy and interpretation.
    - **Inclusiveness**: Ensuring the tool is accessible and usable by a wide audience.
    """)
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        
        if st.button("Analyze Data"):
            analyze_data(df)
            
        # Visualization section
        st.sidebar.header("Visualizations")
        selected_plot = st.sidebar.radio("Select plot type", ["Bar plot", "Histogram"])
        
        if selected_plot == "Bar plot":
            x_axis = st.sidebar.selectbox("Select x-axis", df.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", df.columns)
            st.write("Bar plot:")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)
        
        elif selected_plot == "Histogram":
            selected_col = st.sidebar.selectbox("Select column for histogram", df.columns)
            st.write("Histogram:")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(df[selected_col], ax=ax, bins=30, kde=True)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
