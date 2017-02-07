import pandas as pd
import os
import cPickle

DATA_DIR = "../data/"
ISFORMAT="%Y-%m-%d %H:%M:%S"

def user_view_split_by_date():
    if(not os.path.exists(DATA_DIR + "user_pay")):
        os.mkdir(DATA_DIR + "user_pay")

    data = pd.read_csv(DATA_DIR + 'user_pay.txt', header=None)
    data.columns = ['uid', 'iid', 'time']

    data = data[data['time'].astype(str) > '2016-10']
    length = data.shape[0]
    print length
    print data.tail(3)
    print data.head()

    dictionary = {}
    for index in range(length):
        print index
        file_name = data.iloc[index, -1].split(' ')[0]
        if (not dictionary.has_key(file_name)):
            dictionary[file_name] = [[], [], []]
        dictionary[file_name][0].append(data.iloc[index, 0])
        dictionary[file_name][1].append(data.iloc[index, 1])
        dictionary[file_name][2].append(data.iloc[index, 2].split(' ')[1].split(':')[0])

    for key,value in dictionary.items():
        print key
        # data_single_day = dictionary[key]
        f = open(DATA_DIR + "user_pay/" + key + ".pkl", 'wb')
        cPickle.dump(value, f, -1)
        f.close()

user_view_split_by_date()
# shop_info = pd.read_csv(DATA_DIR + "shop_info.txt",header=None)