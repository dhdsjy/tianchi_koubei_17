import pandas as pd
import static_params

extra_result = pd.read_csv(static_params.DATA_PATH + 'extra_result.csv',header=None)
print extra_result

submission = pd.read_csv(static_params.OUTPUT_PATH + 'submission.csv')
for index in range(extra_result.shape[0]):
    print extra_result.iloc[index,0]
    submission.iloc[extra_result.iloc[index,0],1:] = extra_result.iloc[index,1:]

f = open(static_params.OUTPUT_PATH + 'submission.csv')

submission.to_csv(static_params + 'submissiob.csv',header=None,index=None)