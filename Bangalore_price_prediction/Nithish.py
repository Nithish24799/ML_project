#!/usr/bin/env python
# coding: utf-8

# In[8]:


import houseprediction as hp
import streamlit as st


# In[12]:


st.title("Bangalore house price prediction")
BHK=st.text_input("Please select size(BHK) 1,2,3,4,5")
sqft=st.text_input("Please select sqftf from 1000 - 5000")
bath=st.text_input("Please select bath 1,2,3,4,5,")
location=st.text_input("Please choose area if not specify known please fill 'other'")
if st.button("Calcuate"):
    try:
        st.success(hp.price_predict(location,sqft,bath,BHK))
    except:
        st.error("Location is not found Try again")

