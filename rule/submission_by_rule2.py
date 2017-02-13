# coding=UTF-8
import pandas as pd
import static_params

#取前一星期直接复制两遍
data = pd.read_pickle(static_params.DATA_PATH + 'user_pay_last_week.pkl')

result = data.copy()

result = pd.merge(result,data,on='iid')
result.iloc[:,11] = result.iloc[:,11]*1.05
result = result.astype(int)

result.to_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None,index=None)
