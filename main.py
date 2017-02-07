import pandas as pd

def read_test():
    data = pd.read_pickle('data/user_view_month/2016_10.pkl')
    print data
read_test()