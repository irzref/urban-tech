import pandas as pd
from numpy import linalg as LA
import numpy as np
from scipy import sparse
from sklearn.preprocessing import normalize

# reading the dataset
item_df_dr_0 = pd.read_csv("../herbarium-berlin-clean.csv", sep = '\t', index_col=False)
item_df_dr_0 = item_df_dr_0.drop(item_df_dr_0.columns[0], axis=1)

cal_btc_df = item_df_dr_0[["kingdom","phylum","class","order","family","genus","species","decimalLatitude","decimalLongitude"]]
oneh_cal_btc_df = pd.get_dummies(cal_btc_df,prefix=['kingdom','phylum','class','order','family','genus','species'])

# convert to sparse matrix
sparse_df = oneh_cal_btc_df.to_sparse(fill_value=0)
X = sparse.csr_matrix(sparse_df.to_coo())

# normalize (L2 norm) the sparse matrix 
x_norm = normalize(X)

# calculate the similarity and take the 20 most similar items
with open("../norm-simdotp-similar-result.csv","a") as hs:

    #for i in range(X.shape[0]):
    for i in range(x_norm.shape[0]):
    
        #hs.write(','.join(str(e) for e in X.dot(X[i,:].T).toarray().flatten().argsort()[1:20]) + "\n")
        hs.write(','.join(str(e) for e in x_norm.dot(x_norm[i,:].T).toarray().flatten().argsort()[::-1][0:20]) + "\n")