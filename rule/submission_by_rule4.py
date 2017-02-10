# coding=UTF-8
import pandas as pd
import static_params

data = pd.read_pickle(static_params.DATA_PATH + 'user_pay_last_two_weeks.pkl')

# #取前两星期的均值
# mean = data.iloc[:,1:].mean(1)
# print mean
# for index in range(1,data.shape[1]):
#     data.iloc[:,index] = mean

data = data.astype(int)
print data

data.to_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None,index=None)