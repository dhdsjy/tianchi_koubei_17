import pandas as pd
import numpy as np
import static_params
data = pd.read_pickle(static_params.DATA_PATH + 'user_pay_last_two_weeks.pkl')
data = data.drop(['iid'],axis=1)

data = data.T
data.columns = np.arange(1,2001).astype(str)
print data
shape = data.shape
for x in range(shape[0]):
    for index in range(shape[1]):
        key = str(index +1)
        if(data.iloc[x,index] <= 1):
            data.iloc[x, index] = data[key].median()
        # data[key].loc[data[key] <= 1] = data[key].mean().astype(int)

print data.astype(int)
