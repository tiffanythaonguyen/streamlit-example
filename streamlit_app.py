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
    
    # Regression (for demonstration, we'll assume last column as dependent variable)
    X = df.iloc[:, :-1]
    X = sm.add_constant(X)  # adding a constant
    y = df.iloc[:, -1]
    model = sm.OLS(y, X).fit()
    st.write(model.summary())

# Function for panel data analysis (simplified for demonstration)
def panel_data_analysis(df):
    # Assuming 'id' and 'time' columns for entities and time respectively
    from linearmodels import PanelOLS
    dependent = df.iloc[:, -1]
    exog = sm.add_constant(df.iloc[:, :-2])
    panel_data = df.set_index(['id', 'time'])
    mod = PanelOLS(dependent, exog, entity_effects=True)
    res = mod.fit(cov_type='clustered', cluster_entity=True)
    st.write(res)

# Main function
def main():
    st.title("PyFiQuant 💼📈🔬")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        
        if st.button("Analyze Data"):
            analyze_data(df)
        
        if st.button("Panel Data Analysis"):
            panel_data_analysis(df)

if __name__ == "__main__":
    main()
