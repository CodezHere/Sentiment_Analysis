import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader = SentimentIntensityAnalyzer()

option = st.sidebar.selectbox("Stock Selection", ("MSFT", "TSLA", "AAPL", "GME"))

if option == "TSLA":
    option = st.sidebar.selectbox("Annual or Quarterly?", ('Annual', 'Quarterly'))

    if option == 'Quarterly':
        st.title("Financial & Sentiment Summary")
        st.header("Tesla")
        col1, col2 = st.beta_columns(2)

        with col1:
            st.subheader("Historical Stock Price")
            tesla = yf.Ticker("TSLA")
    #         price_data = tesla.history(period="5d")['Close']
    #         st.line_chart(price_data)

            fig = go.Figure(data=[go.Candlestick(x=tesla.history(period='1mo').index,
                                                open=tesla.history(period='1mo')["Open"],
                                                high=tesla.history(period='1mo')['High'],
                                                low=tesla.history(period='1mo')["Low"],
                                                close=tesla.history(period='1mo')["Close"],
                                                name="Tesla")])
    #         fig.update_xaxes(type='category')
            fig.update_layout(height=440)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Historical Sentiment")
            tweets = pd.read_csv('data/TSLA_tweets.csv')
            tweets = tweets[['created_at', 'text']]
            tweets['created_at'] = pd.to_datetime(tweets.created_at, format='%Y-%m-%d').dt.date
            tweet_scores = pd.DataFrame(tweets['text'].apply(vader.polarity_scores).tolist())
            tweets = tweets.join(tweet_scores, rsuffix='_right')
            mean_scores = tweets.groupby(['created_at']).mean()
            mean_scores = mean_scores.unstack()
            mean_scores = mean_scores.xs('compound').transpose()
            fig = px.bar(mean_scores, labels={"created_at":"Date", "value":"Sentiment Score"})
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)


        with col1:
            st.subheader("Balance Sheet Summary")
            st.subheader("Assets")
            fig = go.Figure(data=[
                go.Bar(name="Cash", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Cash']),
                go.Bar(name="Net Receivables", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Net Receivables']),
                go.Bar(name="Inventory", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Inventory']),
                go.Bar(name="Net Property, Plant and Equipment", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Property Plant Equipment']),
                go.Bar(name="Other Long Term Assets", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Other Assets']),
            ])
            fig.update_layout(barmode='stack')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("")
            st.subheader("Liabilities")
            fig = go.Figure(data=[
                go.Bar(name="Accounts Payable", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Accounts Payable']),
                go.Bar(name="Short Term Debt", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Short Long Term Debt']),
                go.Bar(name="Other Current Liabilities", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Other Current Liab']),
                go.Bar(name="Long Term Debt", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.quarterly_balance_sheet.loc['Long Term Debt'])
            ])

            fig.update_layout(barmode='stack')
            st.plotly_chart(fig, use_container_width=True)



    if option == 'Annual':
        st.title("Financial & Sentiment Summary")
        st.header("Tesla")
        col1, col2 = st.beta_columns(2)

        with col1:
            st.subheader("Historical Stock Price")
            tesla = yf.Ticker("TSLA")
    #         price_data = tesla.history(period="5d")['Close']
    #         st.line_chart(price_data)

            fig = go.Figure(data=[go.Candlestick(x=tesla.history(period='1mo').index,
                                                open=tesla.history(period='1mo')["Open"],
                                                high=tesla.history(period='1mo')['High'],
                                                low=tesla.history(period='1mo')["Low"],
                                                close=tesla.history(period='1mo')["Close"],
                                                name="Tesla")])
    #         fig.update_xaxes(type='category')
            fig.update_layout(height=440)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Historical Sentiment")
            tweets = pd.read_csv('data/TSLA_tweets.csv')
            tweets = tweets[['created_at', 'text']]
            tweets['created_at'] = pd.to_datetime(tweets.created_at, format='%Y-%m-%d').dt.date
            tweet_scores = pd.DataFrame(tweets['text'].apply(vader.polarity_scores).tolist())
            tweets = tweets.join(tweet_scores, rsuffix='_right')
            mean_scores = tweets.groupby(['created_at']).mean()
            mean_scores = mean_scores.unstack()
            mean_scores = mean_scores.xs('compound').transpose()
            fig = px.bar(mean_scores, labels={"created_at":"Date", "value":"Sentiment Score"})
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    #         tesla = yf.Ticker("TSLA")
    #         price_data = tesla.history(period="max")['Close']
    #         st.line_chart(price_data)


        with col1:
            st.subheader("Balance Sheet Summary")
            st.subheader("Assets")
            fig = go.Figure(data=[
                go.Bar(name="Cash", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Cash']),
                go.Bar(name="Net Receivables", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Net Receivables']),
                go.Bar(name="Inventory", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Inventory']),
                go.Bar(name="Net Property, Plant and Equipment", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Property Plant Equipment']),
                go.Bar(name="Other Long Term Assets", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Other Assets']),
            ])
            fig.update_layout(barmode='stack')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("")
            st.subheader("Liabilities")
            fig = go.Figure(data=[
                go.Bar(name="Accounts Payable", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Accounts Payable']),
                go.Bar(name="Short Term Debt", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Short Long Term Debt']),
                go.Bar(name="Other Current Liabilities", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Other Current Liab']),
                go.Bar(name="Long Term Debt", x=['2020', '2019', '2018', '2017'], y=tesla.balance_sheet.loc['Long Term Debt'])
            ])

            fig.update_layout(barmode='stack')
            st.plotly_chart(fig, use_container_width=True)