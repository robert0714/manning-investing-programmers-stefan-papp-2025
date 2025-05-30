import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

st.title("Technical Analysis")

ptype = ('NONE', 'MA', 'BOLL', 'MACD', 'CANDLE', 'CLOUD')
tickers = ('TSLA', 'AAPL', 'MSFT', 'ETH-USD', 'BTC-USD')
dropdown = st.selectbox("Select Ticker", tickers)
plot = st.selectbox("Select Plot", ptype)

start = st.date_input('Start Date', pd.to_datetime('2024-01-01'))
end = st.date_input('End Date', pd.to_datetime('today'))

def bollinger(data):
    sma_window_length = 20
    std_dev_factor = 2
    data['SMA'] = data['Close'].rolling(window=sma_window_length).mean()
    rolling_std = data['Close'].rolling(window=sma_window_length).std()
    data['rf'] = (rolling_std * std_dev_factor)
    data['upper'] = data['SMA'] + data['rf']
    data['lower'] = data['SMA'] - data['rf']

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label="Close Price", color="blue", linewidth=1)
    plt.plot(data.index, data['SMA'], label=f"{sma_window_length}-Day SMA", color="orange", linewidth=1.5)
    plt.plot(data.index, data['upper'], label="Upper Bollinger Band", color="green", linestyle="--", linewidth=1)
    plt.plot(data.index, data['lower'], label="Lower Bollinger Band", color="red", linestyle="--", linewidth=1)

    plt.title(f"Bollinger Bands for (20-day window)", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price", fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)
    return plt

def macd(data):
    short_window = 12
    long_window = 26
    signal_window = 9
    data['EMA_12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['MACD'], label='MACD', color='blue')
    plt.plot(data.index, data['Signal_Line'], label='Signal Line', color='red')
    plt.bar(data.index, data['MACD'] - data['Signal_Line'], label='Histogram', color='gray', alpha=0.5)
    plt.legend(loc='best')
    plt.title('MACD Indicator')
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.grid()
    return plt

def ma(data):
    data.reset_index(inplace=True)
    periods = [10, 20, 30, 40, 50, 60]
    for period in periods:
        data[f"SMA_{period}"] = data["Close"].rolling(window=period).mean()

    # Plot Moving Average Ribbon
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Close"], label="Price", color="black", linewidth=1.5)
    for period in periods:
        plt.plot(data["Date"], data[f"SMA_{period}"], label=f"SMA {period}")
    plt.title("Moving Average Ribbon")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    return plt
def candle(data):
    fig, ax = mpf.plot(data, type='candle', style='charles',figsize=(15,10), title='Candlestick Chart', returnfig=True)
    return fig

def cloud(data):
    # Calculate Ichimoku components
    df["Tenkan"] = (df["Close"].rolling(window=9).max() + df["Close"].rolling(window=9).min()) / 2
    df["Kijun"] = (df["Close"].rolling(window=26).max() + df["Close"].rolling(window=26).min()) / 2
    df["Senkou_A"] = ((df["Tenkan"] + df["Kijun"]) / 2).shift(26)
    df["Senkou_B"] = ((df["Close"].rolling(window=52).max() + df["Close"].rolling(window=52).min()) / 2).shift(26)
    df["Chikou"] = df["Close"].shift(-26)

    # Plot Ichimoku Cloud
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price", color="black")
    plt.plot(df.index, df["Tenkan"], label="Tenkan-sen", color="red")
    plt.plot(df.index, df["Kijun"], label="Kijun-sen", color="blue")
    plt.fill_between(df.index, df["Senkou_A"], df["Senkou_B"], where=df["Senkou_A"] >= df["Senkou_B"],
                     color="lightgreen", alpha=0.5)
    plt.fill_between(df.index, df["Senkou_A"], df["Senkou_B"], where=df["Senkou_A"] < df["Senkou_B"],
                     color="lightcoral", alpha=0.5)
    plt.plot(df.index, df["Chikou"], label="Chikou Span", color="purple", linestyle="dotted")

    plt.title("Ichimoku Cloud")
    plt.legend()
    return plt

def plot_ta(title: str, method):
    st.header(title)
    plt = method(df)
    st.pyplot(plt)

if len (dropdown) > 0 and plot != 'NONE':
    df = yf.Ticker(dropdown).history(start=start, end=end)
    match(plot):
        case 'BOLL':
            plot_ta("Bollinger bands", bollinger)
        case 'MA':
            plot_ta("Moving Average Ribbons", ma)
        case 'MACD':
            plot_ta("MACD", macd)
        case 'CANDLE':
            plot_ta("CANDLE", candle)
        case 'CLOUD':
            plot_ta("CLOUD", cloud)