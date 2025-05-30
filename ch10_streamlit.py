import streamlit as st
import pandas as pd
import yfinance as yf
st.title("Returns")

tickers = ('TSLA', 'AAPL', 'MSFT', 'ETH-USD', 'BTC-USD')
dropdown = st.multiselect("Select Ticker", tickers)

start = st.date_input('Start Date', pd.to_datetime('2024-01-01'))
end = st.date_input('End Date', pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0)
    return cumret

if len (dropdown) > 0:
    df = relativeret(yf.download(dropdown, start=start, end=end))['Close']
    st.header(f"Returns of {dropdown}")
    st.line_chart(df)
