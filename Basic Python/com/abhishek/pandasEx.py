import pandas as pd
import numpy as np

s = pd.Series([1,2,4,6,np.nan])
print(s)



numArr = np.array([4,5,6,7])
pdArr = pd.Series(numArr)
print(pdArr)
#0    4
#1    5
#2    6
#3    7

numArr2 = np.array([[4,5,6,7],[8,9,10]])
pdArr2 = pd.Series(numArr2)
print(pdArr2)
#0    [4, 5, 6, 7]
#1      [8, 9, 10]


dict1 = {"1":"dfdfdfd",2: "abhishek",3: "rahim"}
pdarr1= pd.Series(dict1)
print(pdarr1)
#1     dfdfdfd
#2    abhishek
#3     pallavi
#dtype: object

print(pdarr1["1"])
#dfdfdfd

print(pdarr1[["1",2]])
#1     dfdfdfd
#2    abhishek
#dtype: object

print(pdarr1 *2)
# can be performed different operations


data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

spreadsheet1 =  pd.DataFrame(data,columns=['year','team','wins','losses'])
print(spreadsheet1)

