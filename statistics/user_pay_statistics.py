import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import static_params

data = pd.read_pickle(static_params.DATA_USER_PAY_MONTH_PATH + "2016_10.pkl")

def get_date(time):
    return time.split(' ')[0]

data['time'] = data['time'].apply(get_date)
data = data[data['time'] >= '2016-10-10']
data = data[data['iid'] == 1999]
#1985,1998,1995
#1824,1707,1418

x = data.groupby(['time']).count()
print x.shape

print x['uid'].mean()
print x['uid'].max()
print x['uid'].min()

print x
# x = x.drop(['uid','iid'],axis=1)
# x.sort(['time'])
x.plot()
plt.show()