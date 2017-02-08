import pandas as pd
import numpy as np
import cPickle
import static_params
def get_date(time):
    return time.split(' ')[0]

def user_pay_get_last_week():
    data = pd.read_pickle(static_params.DATA_USER_PAY_MONTH_PATH + "2016_10.pkl")

    data = data[data['time'] >= '2016-10-25']
    data['time'] = data['time'].apply(get_date)

    data = data.groupby(['iid','time'],as_index=False).count()

    result = pd.DataFrame(np.arange(1,2001),columns=['iid'])

    for index in range(25,32):
        date = '2016-10-' + str(index)
        result[date] = np.zeros((result.shape[0],1))

    length = data.shape[0]

    for row in data.values:
        result.loc[row[0] - 1,row[1]] = row[2]

    f = open(static_params.DATA_PATH + "user_pay_last_week.pkl", 'wb')
    cPickle.dump(result, f, -1)
    f.close()

user_pay_get_last_week()