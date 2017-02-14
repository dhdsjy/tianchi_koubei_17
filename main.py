# coding=UTF-8
from preprocess.data_process import preprocess
from rule.submission_by_rule4 import get_result_by_last_three_weeks_mean
from rule.extra_fix import extra_fix

#预处理数据，获取切分后的数据
# preprocess()
#按当前效果最好的前三星期均值作为结果
get_result_by_last_three_weeks_mean()
#最后做少量人工调整
extra_fix()
