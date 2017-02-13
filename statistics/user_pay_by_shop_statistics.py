import pandas as pd
import static_params
import matplotlib.pyplot as plt

shop_id = '1'

data = pd.read_pickle(static_params.DATA_USER_PAY_BY_SHOP_PATH + shop_id + '.pkl')
data = data[data['time'] > '2016-09']
data =  data.groupby(['time']).count()
data.plot()
print data
plt.show()