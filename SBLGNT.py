#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st

f = open("SBLGNT.txt")
text = f.read()

st.write("This website refers to the SBL Greek New Testament text available online at sites such as") 
st.markdown('[https://gntreader.com/?b=MT&c=1&v=1](https://gntreader.com/?b=MT&c=1&v=1)')

word = st.text_input("Copy the word you would like to count from the Greek text (which should be in lower case), \npaste it here and hit the 'Enter' button: \n\n")

wordcount = text.count(word)

st.write(f"Number of times {word} appears in the NT is {wordcount}.")



# In[ ]:




