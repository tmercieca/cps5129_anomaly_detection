
# coding: utf-8

# In[ ]:


get_ipython().magic('matplotlib inline')
#some imports
import pandas as pd
import numpy as py


# In[1]:


#load dataset and describe it
#dataset thanks to https://www.kaggle.com/dalpozz/creditcardfraud
cc_df = pd.read_csv('creditcard.csv');
cc_df.dropna(inplace=True)
cc_df.describe()


# In[ ]:


#reduce dataset as desired
cc_df = cc_df.head(2000)
cc_df.drop(columns=['Time', 'Amount','V1','V2','V3', 'V5', 'V6', 'V7', 'V8', 'V9','V10','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21', 'V22', 'V23', 'V24', 'V25'], inplace=True)


# In[ ]:


#normalization functionality between 0 and 1, min and max
scaler = MinMaxScaler()
print(scaler.fit_transform(cc_df))
for index in cc_df.columns:
    cc_df[[index]] = scaler.fit_transform(cc_df[[index]])


# In[ ]:


cc_df['Class'].value_counts(normalize=True)


# In[ ]:


#split into testing and training sets
from sklearn.model_selection import train_test_split

# Split data
train, test = train_test_split(cc_df, test_size=0.3)

