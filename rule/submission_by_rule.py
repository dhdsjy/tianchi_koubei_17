# coding=UTF-8
import pandas as pd
import static_params
def get_date(time):
    return time.split(' ')[0]


data = pd.read_pickle(static_params.DATA_USER_PAY_MONTH_PATH + "2016_10.pkl")

data = data[data['time'] >= '2016-10-25']
#取10月的均值，另外对周五乘以1.1,周六和周日乘以1.2
x = data.groupby(['iid'],as_index=False).count()
print x
# x = x.iloc[10:31,:]
x['uid'] = (x['uid']/7).astype(int)

x['1'] = (x['uid']*0.95).astype(int)
x['2'] = (x['uid']*0.95).astype(int)
x['3'] = (x['uid']*0.95).astype(int)
x['4'] = (x['uid']*1.05).astype(int)
x['5'] = (x['uid']*1.12).astype(int)
x['6'] = (x['uid']*1.12).astype(int)
x['7'] = (x['uid']*0.95).astype(int)
x['8'] = (x['uid']*0.95).astype(int)
x['9'] = (x['uid']*0.95).astype(int)
x['10'] = (x['uid']*0.95).astype(int)
x['11'] = (x['uid']*1.05).astype(int)
x['12'] = (x['uid']*1.12).astype(int)
x['13'] = (x['uid']*1.12).astype(int)
x['14'] = (x['uid']*0.95).astype(int)
x = x.drop(['uid','time'],axis=1)

x.to_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None,index=None)
print x
