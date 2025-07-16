import streamlit as st
import joblib
import pandas as pd
import re

model=joblib.load(r'D:\Data_Science\7-Machine_Learning\projects\classfication_logistic&SVM&Desicion_tree\8)Rainfall Prediction\rainfallpkl.pkl')

# Page config
st.set_page_config(page_title="Rainfall Prediction", page_icon="🌧️")

# Main title
st.title("Rainfall Prediction System 🌧️")
st.markdown("---")

# Sidebar
st.sidebar.title('Hello this is check Rainfall 🌧️')
st.sidebar.info("Check Rainfall OR Not")

day=st.text_input('day')
pressure=st.text_input('pressure')
maxtemp=st.text_input('maxtemp')
temparature=st.text_input('temparature')
mintemp=st.text_input('mintemp')
dewpoint=st.text_input('dewpoint')
humidity=st.text_input('humidity')
cloud=st.text_input('cloud')
sunshine=st.text_input('sunshine')
winddirection=st.text_input('winddirection')
windspeed=st.text_input('windspeed')

df=pd.DataFrame({
    'day': [float(day)],
    'pressure': [float(pressure)],
    'maxtemp': [float(maxtemp)],
    'temparature': [float(temparature)],
    'mintemp': [float(mintemp)],
    'dewpoint': [float(dewpoint)],
    'humidity': [float(humidity)],
    'cloud': [float(cloud)],
    'sunshine': [float(sunshine)],
    'winddirection': [float(winddirection)],
    'windspeed': [float(windspeed)]
},index=[0])

df.columns = df.columns.str.strip()

if st.button('Confirm'):
    prediction = model.predict(df)
    df.columns = df.columns.str.strip()
    if prediction[0] == 0:
        st.success('Will not rainfall 🌤️')
    else:
        st.warning('Will rainfall 🌧️')

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ for weather prediction")
