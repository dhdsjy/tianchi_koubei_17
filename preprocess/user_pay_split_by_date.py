import pandas as pd
import os
import cPickle
import static_params

DATA_DIR = "../data/"
ISFORMAT = "%Y-%m-%d %H:%M:%S"

def get_hour(time):
    return time.split(' ')[1].split(':')[0]

def user_view_split_by_date():
    if(not os.path.exists(static_params.DATA_USER_PAY_PATH)):
        os.mkdir(static_params.DATA_USER_PAY_PATH)

    data = pd.read_csv(static_params.DATA_PATH  + 'user_pay.txt', header=None)
    data.columns = ['uid', 'iid', 'time']

    data = data[data['time'].astype(str) > '2016-10']

    for index in range(1, 32):
        print index
        if(index < 10):
            date = '2016-10-0' + str(index)
        else:
            date = '2016-10-' + str(index)

        data_single_day = data[data['time'].str.startswith(date + ' ')]
        data_single_day['time'] = data_single_day['time'].apply(get_hour)

        f = open(static_params.DATA_USER_PAY_PATH  + date + ".pkl", 'wb')
        cPickle.dump(data_single_day, f, -1)
        f.close()

user_view_split_by_date()
# shop_info = pd.read_csv(DATA_DIR + "shop_info.txt",header=None)