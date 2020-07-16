#!/usr/bin/env python
# coding: utf-8

# In[364]:


import pandas as pd
import numpy as np
import re
data=pd.read_csv("C:/Users/ETTTT/Desktop/ASL.csv")
negative=pd.read_csv("C:/Users/ETTTT/Desktop/negative.csv",header=None )
client=pd.read_csv("C:/Users/ETTTT/Desktop/client.csv",header=None )
positive=pd.read_csv("C:/Users/ETTTT/Desktop/positive.csv",header=None )


# In[365]:


#Delete Negatve keywords 
data.loc[:,'keywordsplit']=data.loc[:,'Keyword'].apply(str.split, args=(" ", ))
#create a loop to search each line 
dff=data['keywordsplit'].apply(lambda x: [w for w in x if w in negative[0].to_list()])
Index=[]
for  i in range(len(dff)):
    if len(dff.loc[i]):
        Index.append(i)
    i+=1
data=data.drop(data.index[Index])
data
#data.to_csv(r'C:/Users/ETTTT/Desktop/select_kewords.csv', index = False)


# In[366]:


#Clean Client positive keywords, split by ',' & '/'
client=client[0].to_list()
client=client+client[3].split(',')+client[4].split('/')+client[11].split('/')
client=[w.lower() for w in list(client)]
client


# In[367]:


# Match client positive keywords
index=[]
data=data.reset_index()
for j in range(len(client)):
    for  i in range(len(data)):
        if re.findall('\\b'+client[j]+'\\b',data.loc[i,'Keyword']): 
            index.append(i)
index=list(set(index))# select unique index, as some of index shows more than once.
match=data.loc[index]
match


# In[368]:


# Match  positive keywords
index2=[]
positive=positive[0].to_list()
for j in range(len(positive)):
    for  i in range(len(data)):
        if re.findall('\\b'+positive[j]+'\\b',data.loc[i,'Keyword']): 
            index2.append(i)
index2=list(set(index2))
match2=data.loc[index2]
match2
#match2.to_csv(r'C:/Users/ETTTT/Desktop/select_kewords.csv', index = False)


# In[369]:


match2.to_csv(r'C:/Users/ETTTT/Desktop/select_kewords.csv', index = False)


# In[ ]:




