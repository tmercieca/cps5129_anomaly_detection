
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
#based on pseudocode by wikipedia
#https://en.wikipedia.org/wiki/DBSCAN

#return the distance between two multidimensional points
def euclidean_dist_all_dims_dbscan(input_tuple, dataset_tuple):
    distance = 0
    dim_size = len(cc_df_list[0])
    for i in range(dim_size):
        distance += (input_tuple[i] - dataset_tuple[i])**2
    return py.sqrt(distance)


def region_query(point, eps, dataset):
    reachable_points = []
    for p in dataset:
        dist = euclidean_dist_all_dims_dbscan(p, point)
        #print ('point', point)
        if  dist < eps:
            reachable_points.append(p)
    return reachable_points


def DBSCAN(dataset, eps, min_pts):
    outlier_list = []
    visited_points_list = []
    cluster_list = []
    cluster_counter = -1
    
    for point in dataset:
        #marking point as visited
        visited_points_list.append(point) 
        
        reachable_points = region_query(point, eps, dataset)
        
        if len(reachable_points) < min_pts:    
            outlier_list.append(point)
        else:
            cluster_list.append(point)
            cluster_counter+=1
            expand_cluster(point, reachable_points, cluster_list, cluster_counter,eps, min_pts, dataset, visited_points_list)

    print ("Outliers:", len(outlier_list))
    print ("Clusters: " , len(cluster_list))

def expand_cluster(point, reachable_points, cluster_list, cluster_counter, eps, min_pts, dataset, visited_points_list):
    cluster_list.append(point)
    for point in reachable_points:
        if point not in visited_points_list:
            visited_points_list.append(point) 
            reachable_points_new = region_query(point, eps, dataset)
            if len(reachable_points_new) >= min_pts:
                reachable_points += reachable_points_new
        if point not in (i for i in cluster_list):
            cluster_list.append(point)


# In[ ]:


#configure and run dbscan
eps = 2
min_pts = 4

cc_df_list = [tuple(x) for x in cc_df.drop(columns=['Class']).values]
cc_df_list

DBSCAN(cc_df_list,eps,min_pts)



