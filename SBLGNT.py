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

word = st.text_input("Copy the word you would like to count from the Greek text (which should be in lower case), \n\npaste it here and hit the 'Enter' button:\n\n\n\n")

wordcount_nt = nt_text.count(word)

st.write(f"Number of times {word} appears in the NT is {wordcount_nt}.\n\n")

Mt = open("1-Mt.txt").read()
Mk = open("2-Mk.txt").read()
Lk = open("3-Lk.txt").read()
Jn = open("4-Jn.txt").read()
Ac = open("5-Ac.txt").read()
Ro = open("6-Ro.txt").read()
CoA = open("7-1Co.txt").read()
CoB = open("8-2Co.txt").read()
Ga = open("9-Ga.txt").read()
Eph = open("10-Eph.txt").read()
Php = open("11-Php.txt").read()
Col = open("12-Col.txt").read()
ThA = open("13-1Th.txt").read()
ThB = open("14-2Th.txt").read()
TiA = open("15-1Ti.txt").read()
TiB = open("16-2Ti.txt").read()
Tit = open("17-Tit.txt").read()
Phm = open("18-Phm.txt").read()
Heb = open("19-Heb.txt").read()
Jas = open("20-Jas.txt").read()
PeA = open("21-1Pe.txt").read()
PeB = open("22-2Pe.txt").read()
JnA = open("23-1Jn.txt").read()
JnB = open("24-2Jn.txt").read()
JnC = open("25-3Jn.txt").read()
Jud = open("26-Jud.txt").read()
Re = open("27-Re.txt").read()

wordcount_Mt = Mt.count(word)
wordcount_Mk = Mk.count(word)
wordcount_Lk = Lk.count(word)
wordcount_Jn = Jn.count(word)
wordcount_Ac = Ac.count(word)
wordcount_Ro = Ro.count(word)
wordcount_1Co = CoA.count(word)
wordcount_2Co = CoB.count(word)
wordcount_Ga = Ga.count(word)
wordcount_Eph = Eph.count(word)
wordcount_Php = Php.count(word)
wordcount_Col = Col.count(word)
wordcount_1Th = ThA.count(word)
wordcount_2Th = ThB.count(word)
wordcount_1Ti = TiA.count(word)
wordcount_2Ti = TiB.count(word)
wordcount_Tit = Tit.count(word)
wordcount_Phm = Phm.count(word)
wordcount_Heb = Heb.count(word)
wordcount_Jas = Jas.count(word)
wordcount_1Pe = PeA.count(word)
wordcount_2Pe = PeB.count(word)
wordcount_1Jn = JnA.count(word)
wordcount_2Jn = JnB.count(word)
wordcount_3Jn = JnC.count(word)
wordcount_Jud = Jud.count(word)
wordcount_Re = Re.count(word)

df = pd.DataFrame(
    {
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    "Word Count": [{wordcount_Mt}, {wordcount_Mk}, {wordcount_Lk}, {wordcount_Jn}, {wordcount_Ac}, {wordcount_Ro}, {wordcount_1Co}, {wordcount_2Co}, {wordcount_Ga}, {wordcount_Eph}, {wordcount_Php}, {wordcount_Col}, {wordcount_1Th}, {wordcount_2Th}, {wordcount_1Ti}, {wordcount_2Ti}, {wordcount_Tit}, {wordcount_Phm}, {wordcount_Heb}, {wordcount_Jas}, {wordcount_1Pe}, {wordcount_2Pe}, {wordcount_1Jn}, {wordcount_2Jn}, {wordcount_3Jn}, {wordcount_Jud}, {wordcount_Re}],
    "Percentage": [{100*wordcount_Mt/wordcount_nt}, {100*wordcount_Mk/wordcount_nt}, {100*wordcount_Lk/wordcount_nt}, {100*wordcount_Jn/wordcount_nt}, {100*wordcount_Ac/wordcount_nt}, {100*wordcount_Ro/wordcount_nt}, {100*wordcount_1Co/wordcount_nt}, {100*wordcount_2Co/wordcount_nt}, {100*wordcount_Ga/wordcount_nt}, {100*wordcount_Eph/wordcount_nt}, {100*wordcount_Php/wordcount_nt}, {100*wordcount_Col/wordcount_nt}, {100*wordcount_1Th/wordcount_nt}, {100*wordcount_2Th/wordcount_nt}, {100*wordcount_1Ti/wordcount_nt}, {100*wordcount_2Ti/wordcount_nt}, {100*wordcount_Tit/wordcount_nt}, {100*wordcount_Phm/wordcount_nt}, {100*wordcount_Heb/wordcount_nt}, {100*wordcount_Jas/wordcount_nt}, {100*wordcount_1Pe/wordcount_nt}, {100*wordcount_2Pe/wordcount_nt}, {100*wordcount_1Jn/wordcount_nt}, {100*wordcount_2Jn/wordcount_nt}, {100*wordcount_3Jn/wordcount_nt}, {100*wordcount_Jud/wordcount_nt}, {100*wordcount_Re/wordcount_nt}]
    }
)

rounded_df = df.round(decimals=0)
st.dataframe(rounded_df)


import altair as alt

# Prepare your data
source = pd.DataFrame({
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    "Percentage": [100*wordcount_Mt/wordcount_nt, 100*wordcount_Mk/wordcount_nt, 100*wordcount_Lk/wordcount_nt, 100*wordcount_Jn/wordcount_nt, 100*wordcount_Ac/wordcount_nt, 100*wordcount_Ro/wordcount_nt, 100*wordcount_1Co/wordcount_nt, 100*wordcount_2Co/wordcount_nt, 100*wordcount_Ga/wordcount_nt, 100*wordcount_Eph/wordcount_nt, 100*wordcount_Php/wordcount_nt, 100*wordcount_Col/wordcount_nt, 100*wordcount_1Th/wordcount_nt, 100*wordcount_2Th/wordcount_nt, 100*wordcount_1Ti/wordcount_nt, 100*wordcount_2Ti/wordcount_nt, 100*wordcount_Tit/wordcount_nt, 100*wordcount_Phm/wordcount_nt, 100*wordcount_Heb/wordcount_nt, 100*wordcount_Jas/wordcount_nt, 100*wordcount_1Pe/wordcount_nt, 100*wordcount_2Pe/wordcount_nt, 100*wordcount_1Jn/wordcount_nt, 100*wordcount_2Jn/wordcount_nt, 100*wordcount_3Jn/wordcount_nt, 100*wordcount_Jud/wordcount_nt, 100*wordcount_Re/wordcount_nt]
})

# Create the Altair donut chart

c = alt.Chart(source).mark_arc(innerRadius=70).encode(
    theta=alt.Theta(field="Percentage", type="quantitative"),
    color=alt.Color(field="Book", type="nominal", title="Book"),
    order=alt.Order(field="Percentage", sort="descending") # Optional: order arcs by value
).properties(
    title="Word Count of {word}"
)

# Display the chart in Streamlit
st.title("Streamlit Donut Chart with Altair")
st.altair_chart(c)

# In[ ]:




