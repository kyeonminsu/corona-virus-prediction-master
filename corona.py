import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot

df=pd.read_csv('time_series_19-covid-Confirmed.csv')
df.head()