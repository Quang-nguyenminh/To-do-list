import pandas as pd

df = pd.read_csv('To-do list.csv')
matrix = df.values  # NumPy array
print(matrix)
