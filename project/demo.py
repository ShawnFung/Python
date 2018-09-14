import tushare as ts
import matplotlib.pyplot as plt
df = ts.get_hist_data('600848')
openVal = df['open']
openVal.sort_index(inplace=True)
plt.figure()
openVal.plot()
plt.show()
