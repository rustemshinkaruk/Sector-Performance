import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

fin=pd.read_csv('XLF-fin.csv')
util=pd.read_csv('XLU-utilities.csv')
disc=pd.read_csv('XLY-disc.csv')
stapels=pd.read_csv('XLP-staples.csv')
energy=pd.read_csv('XLE-energy.csv')
health=pd.read_csv('XLV-health.csv')
industr=pd.read_csv('XLI-industrial.csv')
tech=pd.read_csv('XLK-tech.csv')
telecom=pd.read_csv('XLC-telecome.csv')
mat=pd.read_csv('XLB-materials.csv')
real=pd.read_csv('XLRE-real.csv')


fin.Date=fin.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
util.Date=util.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
disc.Date=disc.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
stapels.Date=stapels.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
energy.Date=energy.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
health.Date=health.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
industr.Date=industr.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
tech.Date=tech.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
telecom.Date=telecom.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
mat.Date=mat.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
real.Date=real.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))


fin.set_index('Date',inplace=True)
util.set_index('Date',inplace=True)
disc.set_index('Date',inplace=True)
stapels.set_index('Date',inplace=True)
energy.set_index('Date',inplace=True)
health.set_index('Date',inplace=True)
industr.set_index('Date',inplace=True)
tech.set_index('Date',inplace=True)
telecom.set_index('Date',inplace=True)
mat.set_index('Date',inplace=True)
real.set_index('Date',inplace=True)

legend=['Financials','Utilities','Discretionary','Stapels','Energy','Health','Industrial',
        'Tech','Telecom','Materials','Real Estate']
sectors=['fin','util','disc','stapels','energy','health','industr','tech',
         'telecom','mat','real']
for i in sectors:
    eval("plt.plot("+i+".Close)")
plt.Close()

for i in sectors:
    exec(i+"['ret']=("+i+".Close-"+i+".Close.shift(1))/"+i+".Close.shift(1)")

for i in sectors:
    exec(i+"['Cumsum']="+"np.cumsum("+i+".ret)")

for i in sectors:
    exec(i+"="+i+".dropna()")
    
rank_ret=[]
for i in sectors:
    exec("rank_ret.append(max("+i+".Cumsum.values[np.where("+i+".index>'2020-02-23')]))")
results=pd.DataFrame(legend,rank_ret)
results



for i in sectors:
    eval("plt.plot(np.cumsum("+i+".ret))")
plt.vlines('2020-03-18 00:00:00',-1.3,1.3,color='red')  
plt.annotate('March 2020',xy=('2019-11-05 00:00:00',1.32),fontsize=15)
plt.title("Cumulative Return of sectors")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
  
plt.legend(legend)
fig = plt.gcf()
fig.set_size_inches(11.5, 7.5)
fig.savefig('sectors.png', dpi=100)
plt.Close()

cum_return_after_crisis=[]
for i in sectors:
    exec("cum_return_after_crisis.append(np.cumsum("+i+".ret.values[np.where("+i+".index>'2020-03-18')])[-1])")

results2=pd.DataFrame(cum_return_after_crisis,legend,columns=["Cumulative Return"])
results2["Rank"]=(results2["Cumulative Return"].rank(ascending=False).values).astype(int)
results2

results2.to_csv("results.csv")



























