import pandas as pd
import static_params
import cPickle
import os

def get_date(time):
    return time.split(' ')[0]


if(not os.path.exists(static_params.DATA_USER_PAY_BY_SHOP_PATH)):
    os.mkdir(static_params.DATA_USER_PAY_BY_SHOP_PATH)

data = pd.read_csv(static_params.DATA_PATH + 'user_pay.txt',header=None)

data.columns = ['uid','iid','time']

data['iid'] = data['iid'].astype(str)
data['time'] = data['time'].apply(get_date)

grouped = data.groupby(['iid'],as_index=False)
print type(grouped)

for name,group in grouped:
    f = open(static_params.DATA_USER_PAY_BY_SHOP_PATH + str(name) + '.pkl', 'wb')
    cPickle.dump(group,f,-1)
    f.close()