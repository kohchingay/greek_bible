#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import streamlit as st
import numpy as np

sblgnt = open("SBLGNT.txt")
nt_text = sblgnt.read()

st.write("This website refers to the SBL Greek New Testament text available online at sites such as") 
st.markdown('[https://gntreader.com/?b=MT&c=1&v=1](https://gntreader.com/?b=MT&c=1&v=1)')

word = st.text_input("Copy the word you would like to count from the Greek text (which should be in lower case), \npaste it here and hit the 'Enter' button: \n\n")

wordcount_nt = nt_text.count(word)

st.write(f"Number of times {word} appears in the NT is {wordcount_nt}.\n\n")

Mt = open("1-Mt.txt")
Mk = open("2-Mk.txt")
Lk = open("3-Lk.txt")
Jn = open("4-Jn.txt")
Ac = open("5-Ac.txt")
Ro = open("6-Ro.txt")
1Co = open("7-1Co.txt")
2Co = open("8-2Co.txt")
Ga = open("9-Ga.txt")
Eph = open("10-Eph.txt")
Php = open("11-Php.txt")
Col = open("12-Col.txt")
1Th = open("13-1Th.txt")
2Th = open("14-2Th.txt")
1Ti = open("15-1Ti.txt")
2Ti = open("16-2Ti.txt")
Tit = open("17-Tit.txt")
Phm = open("18-Phm.txt")
Heb = open("19-Heb.txt")
Jas = open("20-Jas.txt")
1Pe = open("21-1Pe.txt")
2Pe = open("22-2Pe.txt")
1Jn = open("23-1Jn.txt")
2Jn = open("24-2Jn.txt")
3Jn = open("25-3Jn.txt")
Jud = open("26-Jud.txt")
Re = open("27-Re.txt")

wordcount_Mt = Mt.count(word)
wordcount_Mk = Mk.count(word)
wordcount_Lk = Lk.count(word)
wordcount_Jn = Jn.count(word)
wordcount_Ac = Ac.count(word)
wordcount_Ro = Ro.count(word)
wordcount_1Co = 1Co.count(word)
wordcount_2Co = 2Co.count(word)
wordcount_Ga = Ga.count(word)
wordcount_Eph = Eph.count(word)
wordcount_Php = Php.count(word)
wordcount_Col = Col.count(word)
wordcount_1Th = 1Th.count(word)
wordcount_2Th = 2Th.count(word)
wordcount_1Ti = 1Ti.count(word)
wordcount_2Ti = 2Ti.count(word)
wordcount_Tit = Tit.count(word)
wordcount_Phm = Phm.count(word)
wordcount_Heb = Heb.count(word)
wordcount_Jas = Jas.count(word)
wordcount_1Pe = 1Pe.count(word)
wordcount_2Pe = 2Pe.count(word)
wordcount_1Jn = 1Jn.count(word)
wordcount_2Jn = 2Jn.count(word)
wordcount_3Jn = 3Jn.count(word)
wordcount_Jud = Jud.count(word)
wordcount_Re = Re.count(word)

df = pd.DataFrame(
    {
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    "Word Count": [{wordcount_Mt}, {wordcount_Mk}, {wordcount_Lk}, {wordcount_Jn}, {wordcount_Ac}, {wordcount_Ro}, {wordcount_1Co}, {wordcount_2Co}, {wordcount_Ga}, {wordcount_Eph}, {wordcount_Php}, {wordcount_Col}, {wordcount_1Th}, {wordcount_2Th}, {wordcount_1Ti}, {wordcount_2Ti}, {wordcount_Tit}, {wordcount_Phm}, {wordcount_Heb}, {wordcount_Jas}, {wordcount_1Pe}, {wordcount_2Pe}, {wordcount_1Jn}, {wordcount_2Jn}, {wordcount_3Jn}, {wordcount_Jud}, {wordcount_Re}]
    }
)
st.table(df)
  
# In[ ]:




