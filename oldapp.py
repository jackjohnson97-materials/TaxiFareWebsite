import streamlit as st
import requests
import datetime

st.markdown('''
# TaxiFareModel front

## Please complete the fields below to allow you predict a cab fare in NY.
''')

# pickup_time = st.text_input('Insert a pickup datetime')
pickup_date = st.date_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'

pickup_longitude = st.number_input('Insert the pickup longitude',value=40.7614327)
pickup_latitude = st.number_input('Insert the pickup latitude',
                                  value=-73.9798156)
dropoff_longitude = st.number_input('Insert the dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('Insert the dropoff latitude',value=-73.9797156)
passenger_count = st.number_input('Select a passenger count',value=1)

url = 'https://taxifare.lewagon.ai/predict'
params = dict(pickup_datetime=pickup_datetime,
              pickup_longitude=pickup_longitude,
              pickup_latitude=-pickup_latitude,
              dropoff_longitude=dropoff_longitude,
              dropoff_latitude=dropoff_latitude,
                passenger_count=passenger_count)
# st.write(params)
# get the prediction and assign it to variable repsonse
response = requests.get(url, params=params)
prediction = response.json()
pred = prediction['prediction']
pred
## Finally, we can display the prediction to the user
# st.write(f"Your fare will cost an estimated $ {round(response.get('prediction'),2)}")
