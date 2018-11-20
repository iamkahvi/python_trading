from iexfinance import Stock
from iexfinance import get_historical_data
from datetime import datetime
from IPython.lib.deepreload import reload as dreload

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

start = datetime(2017, 2, 9)
end = datetime(2017, 5, 24)

# https://iextrading.com/apps/stocks/
df = get_historical_data("VOO", start=start, end=end, output_format='pandas')

print(df.head())

# df.plot()
# plt.show()

tsla = Stock('TSLA')
print(tsla.get_price())
