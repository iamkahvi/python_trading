# coding: utf-8

get_ipython().run_line_magic('run', 'trading.py')
get_ipython().run_line_magic('history', '')
get_ipython().system('ls')
df.index
df.columns
df.values
df.head
df.head(10)
df.describe
df.describe()
df.head(5)
df.sort_values(by=high)
df.sort_values(by='high')
df.sort_values(by='high', ascending=False)
df.sort_values(by='high', ascending=False).head(10)
df.sort_values(by=df.volume, ascending=False).head(10)
df.sort_values(by='volume', ascending=False).head(10)
get_ipython().run_line_magic('save', 'nov_20 ')
get_ipython().run_line_magic('save', 'nov_20 0-19')
