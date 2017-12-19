
# coding: utf-8

# In[3]:


def euclidean_dist_all_dims(input_tuple, dataset_tuple):
    distance = 0
    max_dim = len(input_tuple.columns)-1 #ignore distance for last column; assuming it is class
    for i in range(max_dim):
        distance += (input_tuple.iat[0,i] - dataset_tuple.iat[0,i])**2
    return py.sqrt(distance)

def generate_neighbour_set(input_tuple, dataset):
    d = []
    max_dim = len(input_tuple.columns)-1 #ignore distance for last dimension - assuming class passed
    size_of_dataset_tuple = len(dataset)
    for i in range(size_of_dataset_tuple):
        d.append((dataset.iat[i,max_dim], euclidean_dist_all_dims(input_tuple, dataset.iloc[i:i+1])))
    return pd.DataFrame(d, columns=('Class', 'eu_dist'))

def select_class_from_k_neighbours(neighbour_df, k):
    sorted_neighbour_df = neighbour_df.sort_values(by='eu_dist',ascending=True);
    return sorted_neighbour_df.head(k)['Class'].mode().iat[0]


# In[ ]:


a = []
for i in range(len(test)):
    max_dim = len(test.columns)-1 #ignore distance for last dimension - assuming it is class
    
    #compare entry from test to all those in train sets using k=5
    a.append((test.iat[i, max_dim], select_class_from_k_neighbours(generate_neighbour_set(test.iloc[i:i+1],train), 3)))

knn_results_df = pd.DataFrame(a, columns=('Actual', 'kNN-Implementation'))


# In[4]:


#KNN with sklearn
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3, algorithm='kd_tree')
neigh.fit(train.drop(columns=['Class']), train['Class']) 
knn_results_sklearn = neigh.predict(test.drop(columns=['Class']))


# In[ ]:


#compare our predictions to sklearn's; highlight where different
knn_results_df['sklearn'] = knn_results_sklearn
knn_results_df[knn_results_df.apply(pd.Series.nunique, axis=1) != 1]

