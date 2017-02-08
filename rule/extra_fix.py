# coding=UTF-8
import pandas as pd
import static_params

result = pd.read_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None)
#1824,1707,1418
#1824
#只在10-10 这天有过10的数据

#1707
#             uid  iid
# time
# 2016-10-10  372  372
# 2016-10-11  395  395
# 2016-10-12  311  311
# 2016-10-13  380  380
# 2016-10-14  343  343
# 2016-10-15  374  374
# 2016-10-16  408  408
# 2016-10-17  459  459
# 2016-10-18  396  396
# 2016-10-19  397  397
# 2016-10-20  444  444
# 2016-10-21  362  362
# 2016-10-22  320  320
# 2016-10-23  384  384
# 2016-10-24  238  238

data = [395,311,380,343,374,408,459]
result.iloc[1707-1,1:8] = data
result.iloc[1707-1,8:15] = data


#1418
#             uid  iid
# time
# 2016-10-10   98   98
# 2016-10-11   97   97
# 2016-10-12  104  104
# 2016-10-13   90   90
# 2016-10-14   76   76
# 2016-10-15   77   77
# 2016-10-16   99   99
# 2016-10-17  107  107
# 2016-10-18  106  106
# 2016-10-19   97   97
# 2016-10-20  103  103
# 2016-10-21  112  112
# 2016-10-22   97   97
# 2016-10-23   87   87
# 2016-10-29   43   43
# 2016-10-30   96   96
# 2016-10-31   79   79

data = [97,104,90,76,77,99,107]
result.iloc[1418-1,1:8] = data
result.iloc[1418-1,8:15] = data

#处理偶尔出现的0值

shape = data.shape
for x in range(shape[0]):
    for index in range(shape[1]):
        if(data.iloc[x,index] <= 1):
            data.iloc[x, index] = data[:,index].median()

result.to_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None,index=None)
print result