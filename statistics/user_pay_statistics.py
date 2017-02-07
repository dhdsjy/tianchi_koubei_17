import pandas as pd
data = pd.read_pickle("../data/user_pay_month/2016-10.pkl")
print data.describe()