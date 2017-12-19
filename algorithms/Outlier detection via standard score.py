
# coding: utf-8

# In[ ]:


zscore_cc_df = cc_df.drop(columns=['Class'])
cols = list(zscore_cc_df.columns)
col_zscore_list = []

for col in cols:
    col_zscore = col + '_zscore'
    col_zscore_list.append(col_zscore)
    zscore_cc_df[col_zscore] = (zscore_cc_df[col] - zscore_cc_df[col].mean())/zscore_cc_df[col].std(ddof=0)
zscore_cc_df[col_zscore_list] = zscore_cc_df[abs(zscore_cc_df) >= 2][col_zscore_list]

#our df without outliers
zscore_cc_df['outlier'] = zscore_cc_df[col_zscore_list].notnull().any(axis=1)

