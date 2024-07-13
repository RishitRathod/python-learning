import numpy as np
import pandas as pd

# #basic data structure in pandas
# #series:-one dimensional labelled array, dataframe
# # task1 object creation Using series
# s=pd.Series([1,(1,2,3),2,[3,5,6],np.nan,7])
# print(s)

# #task 2 object creation Using dataframe
dates = pd.date_range("20230926",periods=4)
# print(dates)
df = pd.DataFrame(np.array([[1,2],[3,4],[5,6],[7,8]]), index=dates, columns=list("AB"))
# print(df)

# #task 3
df1=pd.DataFrame({"A":100,"B":200,"C":500,"D":pd.Series(30,index=list(range(3)))})
# print(df1)
# print(df1.dtypes)

# #task 4
# print(df.head(2))
# print(df.tail(2))
# print(df.index)
# print(df.columns)


# # Task 1: NumPy representation of the underlying data with DataFrame.to_numpy()
# d1 = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]},dtype="float32")
# arr1 = d1.to_numpy()
# print(arr1)

# # Task 2: describe() shows a quick statistic summary of your data
# s = pd.Series([10, 20, 30, 40])
# k1 = s.describe()
# print(k1)
# print(k1.dtype)
# print("\n")
# s = pd.Series([ np.datetime64("2000-01-01"), np.datetime64("2010-01-01"), np.datetime64("2010-01-01")])
# d1 = s.describe()
# print(d1)


# # Task 3: Transposing your data
# df = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]},dtype="float32")
# d1 = df.transpose()
# arr2 = d1.to_numpy()
# print(arr2)


# # 4. Sorting your data (using DataFrame.sort_index() & DataFrame.sort_values())
# #task 4 transpose of DataFrame
# print(df.T)

# #task 5 Slicing 1 by index and 2nd by values 3rd by lable 4 by location 
# print(df1["E"])
# print(df1[0:3])
# print(df.loc[Dates[0]])
# print(df.loc[:,["A","B"]])
# print(df.loc[:, ["A", "B"]])