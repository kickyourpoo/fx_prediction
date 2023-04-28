import streamlit as st
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from catboost import CatBoostClassifier
import pickle

def Long(X):
    # Load saved model
    LDA = pickle.load(open(r'long_lda.pkl', 'rb'))
    # Make predictions
    y_pred = LDA.predict(X)
    return y_pred

def Short(X):
    # Load saved model
    CBC = pickle.load(open(r'short_cbc.pkl', 'rb'))
    # Make predictions
    y_pred = CBC.predict(X)
    return y_pred

st.title("FX Trade Prediction")

st.write("""
Take profit or stop loss before it's too late!
""")

# Get user input for forex data
Open = st.number_input("Enter the Open price:", step=0.000001, format="%.6f")
Close = st.number_input("Enter the Close price:", step=0.000001, format="%.6f")
volume = st.number_input("Enter the Volume:", step=1, format="%d")
atr = st.number_input("Enter the ATR:", step=0.000001, format="%.6f")
entry = st.number_input("Enter the Entry price:", step=0.000001, format="%.6f")
stop_loss = st.number_input("Enter the Stop Loss price:", step=0.000001, format="%.6f")
take_profit = st.number_input("Enter the Take Profit price:", step=0.000001, format="%.6f")
adx = st.number_input("Enter the ADX value:", step=0.000001, format="%.6f")
ema7_change = st.number_input("Enter the EMA7 change:", step=0.000001, format="%.6f")

# Display user input values
st.write("Open price:", Open)
st.write("Close price:", Close)
st.write("Volume:", volume)
st.write("ATR:", atr)
st.write("Entry price:", entry)
st.write("Stop Loss price:", stop_loss)
st.write("Take Profit price:", take_profit)
st.write("ADX value:", adx)
st.write("EMA7 change:", ema7_change)

model_options = ['Long', 'Short']
selected_model = st.selectbox('Are you long or short Pound-Yen?', model_options)

# predict
if st.button("Trade Result"):
    X = [[Open, Close, volume, atr, entry, stop_loss, take_profit, adx, ema7_change]]

    if selected_model == 'Long':
        y_pred = Long(X)
        st.write('You long the market??!!')
    else:
        y_pred = Short(X)
        st.write('You short the market??!!')

    if y_pred == 1:
        st.write("HUAT AH!")
    else:
        st.write("Up lorry...")

