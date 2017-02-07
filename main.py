import pandas as pd

def read_test():
    data = pd.read_pickle('data/user_view/2016-10-11.pkl')
    print data
# read_test()