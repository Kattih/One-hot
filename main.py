import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())

data.loc[data['whoAmI'] == 'human', 'human'] = "1"
data.loc[data['whoAmI'] == 'robot', 'robot'] = "1"
data = data.fillna("0")
del data['whoAmI']
print(data)

# print(pd.get_dummies(data['whoAmI']))  # с использованием get_dummies

