import pandas as pd
import static_params

shop_id = '1'

data = pd.read_pickle(static_params.DATA_USER_PAY_BY_SHOP_PATH + shop_id + '.pkl')

print data