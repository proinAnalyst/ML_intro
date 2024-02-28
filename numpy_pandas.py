import numpy as np
import pandas as pd

# Numpy operations
# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array attributes
print(arr1.shape)  # (5,)
print(arr2.ndim)   # 2
print(arr1.dtype)  # int64

# Array operations
result = arr1 + arr1
result = arr1 * 2
dot_product = np.dot(arr1, arr1)

# Indexing and slicing
print(arr1[0])     # 1
print(arr1[:3])    # [1 2 3]
print(arr1[arr1 > 2])  # [3 4 5]

# Pandas operations
# Creating a DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# DataFrame attributes
print(df.shape)     # (4, 2)
print(df.columns)  # Index(['A', 'B'], dtype='object')
print(df.dtypes)    # A    int64
                    # B    int64
                    # dtype: object

# Accessing data in DataFrame
print(df['A'])     # 0    1
                    # 1    2
                    # 2    3
                    # 3    4
                    # Name: A, dtype: int64
print(df.iloc[0])  # A    1
                    # B    5
                    # Name: 0, dtype: int64
