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
    
    for j in range(main_df.shape[0]):
    #for index, row in main_df.iterrows():
        dis = LA.norm(main_df.iloc[j].values - val_array)
        sim_res = np.append(sim_res, dis)
    
    return np.argsort(sim_res)[:21]

# test dataset
#test_df = oneh_cal_btc_df.iloc[:10]

# loop through each dataset row
similar_item_array = []
used_df = oneh_cal_btc_df
#used_df = test_df

# calculate the similarity and take the 20 most similar items
with open("../caled-similar-result.csv","a") as hs:

    for i in range(used_df.shape[0]):
    #for index, row in used_df.iterrows():
        #print("row : " + str(index), end='\r')
        #res = calculate_ed(row.values, used_df)
        #similar_item_array.append(res)
        
        res = calculate_ed(oneh_cal_btc_df.iloc[i].values, used_df)
        hs.write(','.join(str(e) for e in res) + "\n")
        

        
#end_result = np.array(similar_item_array)
#df1 = pd.DataFrame(end_result)
#df1.to_csv("../caled-similar-result.csv", encoding='utf-8', header=False, index=False)