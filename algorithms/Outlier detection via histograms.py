
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

#(feature value, feature histogram)
def build_histogram_for_feature(feature, show, feature_name):
    bins = np.ceil(np.sqrt(number_of_rows_in_df))
    histogram = np.histogram(feature, bins=int(bins))
    if show is True:
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)
        hist, bins = histogram
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        plt.bar(center, hist, align='center', width=width)
        plt.title('Frequency per Bin for feature ' +feature_name)
        plt.ylabel('Frequency')
        plt.xlabel('Bins')
        plt.show()
    return histogram

def is_point_outlier_using_histogram(point, histogram):
    histogram_freq = histogram[0]
    histogram_bins = histogram[1]
    number_of_bins = histogram_bins.size
    
    for item in np.digitize(point,histogram_bins):
        if point < histogram_bins[0]:
            print('OUTLIER point greater than lower bound bin')
            return True
        elif point > histogram_bins[number_of_bins-1]:
            print('OUTLIER point greater than upperbound bin')
            print (item, histogram_bins[number_of_bins-1])
            return True
        elif histogram_freq[item] == 0:
            #print (point, item, histogram)
            print ('OUTLIER point in an empty bin')
            return True
        else:
            return False


# In[ ]:


def is_feature_outlier_via_dataset(multidim_point, dataset):
    dataset_features = dataset.drop(columns='Class').columns #todo: improve / catch error
    
    for feature in dataset_features:
        histogram = build_histogram_for_feature(dataset[feature], True, feature)
        
        for index, point in enumerate(multidim_point):
            if (is_point_outlier_using_histogram([point], histogram) == True):
                return True
    return False

#using sample point
is_feature_outlier_via_dataset([0.403034,-0.822843,0.502292,0.219422,0.215153],cc_df)

