# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:08:46 2023

@author: Arati
"""

import streamlit as st
import pickle


load = open('random_forest.pkl', 'rb')
model = pickle.load(load)

st.title(' Telecommunication Company Churn Prediction')
# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("telecommunication company.jpeg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=700)

def predict(Intl_plan, Day_mins, Customer_calls, Voice_messages, Day_charge):
    pred= model.predict([[Intl_plan, Day_mins, Customer_calls, Voice_messages, Day_charge]])
    return pred

def start():
    Intl_plan = st.selectbox('Do you have intl plan',('yes', 'no'))
    Day_mins = st.number_input('how many day mins calls')
    Customer_calls = st.number_input('customer calls')
    Voice_messages= st.number_input('number of voice messages')
    Day_charge = st.number_input('charges paid for day')
    
    if st.button('Predict'):
        result = predict(Intl_plan, Day_mins, Customer_calls, Voice_messages, Day_charge)
        st.success('will customer churn? {}'.format(result))
        
if __name__=='__main__':
    start()
    
    
    
    
    
    
    
    
    

