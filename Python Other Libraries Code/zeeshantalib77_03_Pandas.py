import pandas as pd
data={'a': 0., 'b': 1., 'c': 2.}
s=pd.Series(data)
print(s)

import pandas as pd
data={'Name':["Ali","Hamza","Zeeshan","Talib"],'Age':[21,22,23,24]}
df=pd.DataFrame(data,index={'rank1','rank2','rank3','rank4'})
print(df)