import pandas as pd

inp = { "adj_close": [1, 2, 3, 4, 5]}

df = pd.DataFrame(data=inp)

aapl_adj_close = df['adj_close']

print(aapl_adj_close[1:])
print(aapl_adj_close.shift(1)[1:])

aapl_change = (aapl_adj_close[1:] / aapl_adj_close.shift(1)[1:])-1

print(aapl_change)

df2 = {"c1":[4,9], "c2":[2,3]}
ddf = pd.DataFrame(df2)

r = ddf['c1']/ddf['c2']
print(r)