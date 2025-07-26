#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from IPython.display import Markdown

f = open("SBLGNT.txt")
text = f.read()

print("This website refers to the SBL Greek New Testament text available online at sites such as") 
display(Markdown('[https://gntreader.com/?b=MT&c=1&v=1](https://gntreader.com/?b=MT&c=1&v=1)'))

word = input("Enter the word you would like to count in Greek lower case: ")

wordcount = text.count(word)

display (wordcount)


# In[ ]:




