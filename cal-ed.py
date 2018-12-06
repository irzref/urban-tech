import pandas as pd
from numpy import linalg as LA
import numpy as np


# reading the dataset
item_df_dr_0 = pd.read_csv("../herbarium-berlin-clean.csv", sep = '\t', index_col=False)
item_df_dr_0 = item_df_dr_0.drop(item_df_dr_0.columns[0], axis=1)

cal_btc_df = item_df_dr_0[["kingdom","phylum","class","order","family","genus","species","decimalLatitude","decimalLongitude"]]
oneh_cal_btc_df = pd.get_dummies(cal_btc_df,prefix=['kingdom','phylum','class','order','family','genus','species'])


# method to calculate the euclidean distance for each row
def calculate_ed(val_array, main_df):
    sim_res = np.array([])
    
    for index, row in main_df.iterrows():
        dis = LA.norm(row.values - val_array)
        sim_res = np.append(sim_res, dis)
    
    return np.argsort(sim_res)[:20]



# loop through each dataset row
similar_item_array = []
used_df = oneh_cal_btc_df

for index, row in used_df.iterrows():
    #print("row : " + str(index), end='\r')
    res = calculate_ed(row.values, used_df)
    similar_item_array.append(res)
    
    
end_result = np.array(similar_item_array)
df1 = pd.DataFrame(end_result)
df1.to_csv("../result-similarity.csv", encoding='utf-8', header=False, index=False)