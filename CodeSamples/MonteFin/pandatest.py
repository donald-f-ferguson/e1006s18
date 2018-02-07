import pandas as pd

df = pd.read_csv("AAPL.csv", delimiter=",")

print("Row Adj Close, row 3 = ", df["Adj Close"][3])

print("Row 3 = ", df.loc[[2]])