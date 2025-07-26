#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st
import numpy as np

sblgnt = open("SBLGNT.txt")
textnt = sblgnt.read()

st.write("This website refers to the SBL Greek New Testament text available online at sites such as") 
st.markdown('[https://gntreader.com/?b=MT&c=1&v=1](https://gntreader.com/?b=MT&c=1&v=1)')

word = st.text_input("Copy the word you would like to count from the Greek text (which should be in lower case), \npaste it here and hit the 'Enter' button: \n\n")

wordcount_nt = textnt.count(word)

st.write(f"Number of times {word} appears in the NT is {wordcount_nt}.\n\n")

mat = open("1-Mt.txt")
luke = open("3-Lk.txt")

df = pd.DataFrame(
    {
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    
    }
)
st.table(df)
  
# In[ ]:




