import pandas as pd
import os
import cPickle

DATA_DIR = "../data/"
DATA_DIR_SEC = 'user_pay_month/'

ISFORMAT = "%Y-%m-%d %H:%M:%S"

def get_hour(time):
    return time.split(' ')[1].split(':')[0]

def user_view_split_by_date():
    if(not os.path.exists(DATA_DIR + DATA_DIR_SEC)):
        os.mkdir(DATA_DIR + DATA_DIR_SEC)

    data = pd.read_csv(DATA_DIR + 'user_pay.txt', header=None)
    data.columns = ['uid', 'iid', 'time']

    data = data[data['time'].astype(str) > '2016-10']

    f = open(DATA_DIR + DATA_DIR_SEC + '2016_10' + ".pkl", 'wb')
    cPickle.dump(data, f, -1)
    f.close()

user_view_split_by_date()
# shop_info = pd.read_csv(DATA_DIR + "shop_info.txt",header=None)