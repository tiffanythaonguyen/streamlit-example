import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go
import statsmodels.api as sm
from linearmodels import PanelOLS

# Data analysis
def analyze_data(df):
  st.write(df.shape)
  st.write(df.columns)
  st.write(df.index)
  
  for col in df.columns:
    st.write(df[col].nunique())
    
  X = sm.add_constant(df.iloc[:,:-1]) 
  y = df.iloc[:,-1]
  model = sm.OLS(y,X).fit()
  st.write(model.summary())

# Panel data analysis  
def panel_data_analysis(df):
  dependent = df.iloc[:,-1]
  exog = sm.add_constant(df.iloc[:,:-2])
  panel_data = df.set_index(['id','time'])
  mod = PanelOLS(dependent, exog, entity_effects=True)
  res = mod.fit(cov_type='clustered', cluster_entity=True)
  st.write(res)

# Fetch FRED data
def fetch_fred_data(series,start,end):
  return pdr.DataReader(series,'fred',start,end)

# Plot time series  
def plot_timeseries(df, series):
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=df.index, y=df[series], mode='lines', name=series))
  fig.update_layout(title=f"Time Series Plot for {series}", xaxis_title="Date", yaxis_title=series)
  st.plotly_chart(fig)

# Monte Carlo simulation
def monte_carlo_simulation():
   S0 = 100  
   T = 1.0
   r = 0.05
   sigma = 0.2
   num_simulations = 1000
   num_steps = 252

   # Simulation code
   paths = np.zeros((num_simulations, num_steps))
   paths[:,0] = S0
   for i in range(1,num_steps):
     rand = np.random.standard_normal(num_simulations)
     paths[:,i] = paths[:,i-1] * np.exp((r - sigma**2/2)*dt + sigma*rand*np.sqrt(dt))  

   # Display paths   
   for i in range(10):
     st.line_chart(paths[i])

# Portfolio optimization
def portfolio_optimization():
  returns = np.array([[0.01, 0.02, 0.015], [0.012, 0.018, 0.017], [-0.015, 0.019, 0.01]])

  def objective(weights):
    port_ret = np.sum(returns.mean() * weights) * 252
    port_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights))) 
    return -port_ret / port_vol

  constraints = ({'type':'eq','fun':lambda w: np.sum(w)-1})
  bounds = tuple((0,1) for asset in range(returns.shape[1]))

  result = minimize(objective, [0.33,0.33,0.33], method='SLSQP',bounds=bounds,constraints=constraints)

  st.write(result.x)
