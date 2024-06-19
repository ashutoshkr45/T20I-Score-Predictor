import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

# Load the trained model
pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['India','Australia','England','West Indies','New Zealand','Pakistan',
             'South Africa','Sri Lanka','Bangladesh','Afghanistan','Ireland','Zimbabwe']

host_countries = ['South Africa', 'Australia', 'West Indies', 'England', 'Sri Lanka',
       'Zimbabwe', 'Bangladesh', 'India', 'UAE', 'New Zealand', 'USA','Ireland', 'Pakistan']


# Set page configuration
st.set_page_config(page_title="T20I Score Predictor", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Men's T20I Cricket Score Predictor")

# Input fields
col1, col2 = st.columns(2)
with col1:
    bat_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowl_team = st.selectbox('Select Bowling Team', sorted(teams))

loc = st.selectbox('Select Hosting Country', sorted(host_countries))

col3, col4, col5, col6 = st.columns(4)

with col3:
    score = st.number_input('Current Score', step=1, format='%d')  
with col4:
    overs = st.number_input('Overs Bowled (works for over > 5)', step=1, format='%d')  
with col5:
    wickets = st.number_input('Wickets Out', step=1, format='%d')  
with col6:
    last_five = st.number_input('Runs Scored in Last 5 overs', step=1, format='%d')  

# Predict button
if st.button('Predict Score'):
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs if overs > 0 else 0  # Avoids division by zero

    input_df = pd.DataFrame([[bat_team, bowl_team, score, wickets_left, balls_left, crr, last_five, loc]],
                            columns=['Batting Team', 'Bowling Team', 'Runs Scored', 
                                     'Wickets Left', 'Balls Left', 'CRR', 'Last Five', 'Location'])
    result = pipe.predict(input_df)

    st.header("Predicted Score : " + str(int(result[0])))

st.markdown("""
    <div class="footer">
    <p>Made by- Ashutosh Kumar</p>
    </div>
""", unsafe_allow_html=True)