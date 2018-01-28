from pandas_datareader import data

# download Apple price data into DataFrame
#apple = data.DataReader('AAPL', 'yahoo', start='1/1/2000')


def get_data(ticker, s):
    d = data.DataReader(ticker, 'yahoo', start=s)
    return d

def get_mu(d):
    days = (d.index[-1] - d.index[0]).days
    cagr = ((((d['Adj Close'][-1]) / d['Adj Close'][1])) ** (365.0 / days)) - 1
    print('CAGR =', str(round(cagr, 4) * 100) + "%")
    mu = cagr
    return mu


d1 = get_data('AMZN', '1/1/2018')
#m = get_mu(d1)

#print("Mu = ", m)

print(d1)