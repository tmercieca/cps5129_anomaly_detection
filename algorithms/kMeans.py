
# coding: utf-8

# In[1]:


# K Means Clustering
from random import *

def update_k_definitions(k_df, result_df):
    for k in range(len(k_df)):
         for i in range(dim_size):
            k_df.iat[k,i] = result_df.groupby(['Class']).mean().iat[k,i]
    return k_df

def calculate_class(input_tuple, k_df):
    shortest_dist = 9999999999
    new_class = 9999999999
    for k in k_df.iterrows():
        k_tuple = pd.DataFrame(k[1]).transpose()
        new_dist = euclidean_dist_all_dims(input_tuple, k_tuple)
        if (new_dist <= shortest_dist):
            shortest_dist = new_dist
            new_class = k_tuple['Class'].iloc[0]
    return new_class
    
def insert_entry(insert_tuple, k_df, result_df):
    result_df = result_df.append(insert_tuple)
    if ((1 in result_df['Class'].values) and (0 in result_df['Class'].values)):
        k_df = update_k_definitions(k_df, result_df)
    return result_df

def generate_initial_k_values_randomly(k_df, k_count):
    for k in range(k_count):   
        d = []
        for i in range(dim_size):
            d.append(uniform(0.5,0.6))
        to_insert = pd.DataFrame(d).transpose()
        to_insert['Class'] = k
        k_df = k_df.append(to_insert, ignore_index=True)
    return k_df


# In[ ]:


k_count = 2
k_df = pd.DataFrame()
result_df = cc_df

dim_size = len(cc_df.columns) -1

k_df = generate_initial_k_values_randomly(k_df, 2)    
cc_df.drop(columns='Class')
cc_df['Class'] = calculate_class(cc_df, k_df)

#run the k_means 20 or so times
for j in range(20):
    for i, row in result_df.iterrows():
        insert_row = pd.DataFrame(row).transpose()
        result_df.at[i,'Class'] = calculate_class(insert_row.drop(columns='Class'), k_df)    
    update_k_definitions(k_df, result_df)


# In[ ]:


#view our result
result_df['Class'].value_counts(normalize=True)


# In[ ]:


#try sklearn's implementation
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, max_iter=10000000, algorithm='full', random_state=0).fit(cc_df.drop(columns=['Class']))
kmeans.predict(cc_df.drop(columns=['Class']))

