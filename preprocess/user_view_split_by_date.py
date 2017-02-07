import pandas as pd
import os
import cPickle

DATA_DIR = "../data/"
ISFORMAT="%Y-%m-%d %H:%M:%S"

def user_view_split_by_date():
    # os.mkdir(DATA_DIR + "user_view")

    data = pd.read_csv(DATA_DIR + 'user_view.txt', header=None)
    length = data.shape[0]
    dictionary = {}
    for index in range(length):
        print index
        date = data.iloc[index,-1].split(' ')[0]
        if(date.startswith('2016-10')):
            file_name = data.iloc[index,-1].split(' ')[0]
            if(not dictionary.has_key(file_name)):
                dictionary[file_name] = [[], [], []]
            dictionary[file_name][0].append(data.iloc[index, 0])
            dictionary[file_name][1].append(data.iloc[index, 1])
            dictionary[file_name][2].append(data.iloc[index, 2].split(' ')[1].split(':')[0])
    data.close()

    for key in dictionary.keys():
        print key
        data_single_day = dictionary[key]
        f = open(DATA_DIR + "user_view/" + key + ".pkl", 'wb')
        cPickle.dump(data_single_day, f, -1)
        f.close()


user_view_split_by_date()
# shop_info = pd.read_csv(DATA_DIR + "shop_info.txt",header=None)