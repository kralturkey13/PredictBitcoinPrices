import requests
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from scipy import stats

price_url="https://api.coindesk.com/v1/bpi/historical/close.json"
request=requests.get(price_url)
result=request.json()
bpi=result['bpi']
dates=np.arange(1,32)
prices = list(bpi.values())
pickatype=int(input("polynom(1) or linear(2): "))

if pickatype==1:
    mymodel=np.poly1d(np.polyfit(dates,prices,3))
    myline=np.linspace(1,32,100)
    print(r2_score(prices,mymodel(dates)))
    print(mymodel(50))
    plt.scatter(dates,prices)
    plt.plot(myline,mymodel(myline))
    plt.show()
    
elif pickatype==2:
    slope, intercept, r, p, std_err = stats.linregress(dates, prices)
    def myfunc(x):
      return slope * x + intercept
    mymodel = list(map(myfunc, dates))
    plt.scatter(dates, prices)
    print(r)
    print(myfunc(100))
    plt.plot(dates, mymodel)
    plt.show()
