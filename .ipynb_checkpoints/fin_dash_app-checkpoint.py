import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go

option = st.sidebar.selectbox("Annual or Quarterly?", ('Annual', 'Quarterly'))

if option == 'Quarterly':
    st.title("Financial & Sentiment Summary")
    st.header("Tesla")
    col1, col2 = st.beta_columns(2)

    with col1:
        st.subheader("Historical Stock Price")
        tesla = yf.Ticker("TSLA")
        price_data = tesla.history(period="max")['Close']
        st.line_chart(price_data)

    with col2:
        st.subheader("Historical Sentiment")
        tesla = yf.Ticker("TSLA")
        price_data = tesla.history(period="max")['Close']
        st.line_chart(price_data)


    with col1:
        st.subheader("Balance Sheet Summary")
        st.subheader("Assets")
        fig = go.Figure(data=[
            go.Bar(name="Cash", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Cash']),
            go.Bar(name="Net Receivables", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Net Receivables']),
            go.Bar(name="Inventory", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Inventory']),
            go.Bar(name="Net Property, Plant and Equipment", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Property Plant Equipment']),
            go.Bar(name="Other Long Term Assets", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Other Assets']),
        ])
        fig.update_layout(barmode='stack')
        st.plotly_chart(fig)

    with col2:
        st.subheader("")
        st.subheader("Liabilities")
        fig = go.Figure(data=[
            go.Bar(name="Accounts Payable", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Accounts Payable']),
            go.Bar(name="Short Term Debt", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Short Long Term Debt']),
            go.Bar(name="Other Current Liabilities", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Other Current Liab']),
            go.Bar(name="Long Term Debt", x=['Q4 2020', 'Q3 2020', 'Q2 2020', 'Q1 2020'], y=tesla.balance_sheet.loc['Long Term Debt'])
        ])

        fig.update_layout(barmode='stack')
        st.plotly_chart(fig)