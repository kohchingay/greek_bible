#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd

f = open("SBLGNT.txt")
text = f.read()

print("This website refers to the SBL Greek New Testament text available online at sites such as") 
display(Markdown('[https://gntreader.com/?b=MT&c=1&v=1](https://gntreader.com/?b=MT&c=1&v=1)'))

word = input("Copy the word you would like to count from the Greek text (which should be in lower case), \npaste it here and hit the 'Enter' button: \n\n")

wordcount = text.count(word)

display (f"Number of times {word} appears in the NT is {wordcount}.")


# In[ ]:




