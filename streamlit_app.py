import streamlit as st
import pandas as pd
import statsmodels.api as sm

# Function for basic statistical analysis
def analyze_data(df):
    # Basic insights
    st.write(f"Total Columns: {df.shape[1]}")
    st.write(f"Total Rows: {df.shape[0]}")
    st.write(f"Index: {df.index}")
    for column in df.columns:
        st.write(f"Unique values in {column}: {df[column].nunique()}")
    
    # Regression (for demonstration, we'll assume 'prcc_f' as dependent variable)
    # Using 'sale', 'cogs', and 'ppegt' as independent variables
    X = df[['sale', 'cogs', 'ppegt']].dropna()
    y = df.loc[X.index, 'prcc_f']
    X = sm.add_constant(X)  # adding a constant
    model = sm.OLS(y, X).fit()
    st.write(model.summary())

    # Correlation
    st.subheader('Correlation Matrix')
    st.write(df[['prcc_f', 'sale', 'cogs', 'ppegt']].corr())

    # Short description of the data
    st.subheader("Short Description")
    st.write("""
    This dataset provides financial indicators for various companies across different years, 
    ranging from asset details to income metrics. The dataset includes information such as 
    sales, cost of goods sold, property, plant, and equipment (gross), and the closing stock 
    price, among other variables.
    """)

# Main function
def main():
    st.title("PyFiQuant 💼📈🔬")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        
        if st.button("Analyze Data"):
            analyze_data(df)

if __name__ == "__main__":
    main()
