import pandas as pd
import static_params


submission = pd.read_csv(static_params.OUTPUT_PATH + 'submission.csv',header=None)

print submission[submission.iloc[:,1] < 10]