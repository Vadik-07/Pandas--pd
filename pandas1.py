import numpy as np
import pandas as pd
import sys

dict1 = {
    "Name" : ["vadik","Yash","Vinnet","sharthak"],
    "Marks" : [66,77,66,77],
    "City" : ["us","uk","japan","Austriala"]
}

df = pd.DataFrame(dict1)
# print(df)

df.to_csv('friends.csv')
df.to_csv('friends_index_false.csv',index=False)

print(df.head(2))
print(df.tail(2))
print(df.describe())

trainData = pd.read_csv('Book-1.csv')
print(trainData)

print(trainData["Speed"])
trainData["Speed"][3] = 200
print(trainData["Speed"][3])

trainData.to_csv('Book-1.csv')

ser = pd.Series(np.random.random(10))
print(ser)

newdf = pd.DataFrame(np.random.rand(335,5), index=np.arange(335))

print(newdf.head())
print(newdf.describe())

print(newdf.index)
print(newdf.columns)

print(newdf.to_numpy())

print(newdf.T)

print(newdf.sort_index(axis=1, ascending=False))
print(newdf.sort_index(axis=0, ascending=False))

newdf2 = newdf.copy()
newdf2[0][0] = 0.445362

print(newdf.head())
print(newdf2.head())

newdf.columns = list("ABCDE")
newdf2.columns = list("ABCDE")

newdf.loc[0,"A"] = 2007
print(newdf.head())
print(newdf2.head(2))

print(newdf.loc[[1,2], ["C","D"]])
print(newdf.loc[:, ["C","D"]])
print(newdf.loc[[1,2], :])

print(newdf.loc[(newdf["A"] < 0.3) & (newdf["C"] > 0.3)])
print(newdf.iloc[1,2])
print(newdf.iloc[[0,1],[1,2]])

newdf = newdf.drop([0,3,4,200,333], axis=0)
# if we use inplace=True it will do at that place like
newdf.drop(["E"],axis=1,inplace=True)
print(newdf.head())

# To fix Indexing again

newdf.reset_index(drop=True, inplace=True)
print(newdf.head())

print(newdf["B"].isnull())

# newdf["B"] = None
# but use
newdf.loc[:, "B"] = np.random.rand(len(newdf))
print(newdf)

df2 = pd.DataFrame({
    "name": ['Alfard', 'Batman', 'Alfard'],
    "toy": [np.nan, np.nan, np.nan],
    "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]
})

print("Original DataFrame:")
print(df2.head())

# Remove columns or Row where all values are NaN
df2 = df2.dropna(how="all", axis=1)
print("\nDataFrame after dropping columns with all NaN values:")
print(df2.head())

# To remove Duplicate
print(df2.drop_duplicates(subset=['name'])) # there is also keep search it

print(df2.shape)
print(df2.info())

print(df2['name'].value_counts(dropna=False))

# 
# Question
# 

# this become so big number
# qdf = pd.DataFrame(np.random.randint(-sys.maxsize,sys.maxsize, size=(3,2), dtype=np.int64))
qdf = pd.DataFrame(np.random.randint(0,100, size=(3,2)))
print(qdf)
print(qdf.describe())
print(qdf.mean())
print(qdf.corr())
print(qdf.count())
print(qdf.max())
print(qdf.min())
print(qdf.median())
print(qdf.std())

# We can read any Sheet just change the name at sheet_name 
data = pd.read_excel('sheet2.xlsx', sheet_name='Sheet2')
# data = pd.read_excel('sheet2.xlsx', sheet_name='Sheet1')
print(data)

data.iloc[2, 1] = 400
data.to_excel('sheet2.xlsx', sheet_name='Sheet2')