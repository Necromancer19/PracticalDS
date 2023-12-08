################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
GBase = Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/'
ml.style.use('ggplot')

data=[
['London',	29.2, 17.4],
['Glasgow',	18.8, 11.3],
['Cape Town',	15.3, 9.0],
['Houston',	22.0, 7.8],
['Perth',	18.0, 23.7],
['San Francisco',	11.4, 33.3]
]
os_new=pd.DataFrame(data)
pd.Index(['Item', 'Value', 'Value Percent', 'Conversions', 'Conversion Percent',
       'URL', 'Stats URL'],
      dtype='object')

os_new.rename(columns = {0 : "Warehouse Location"}, inplace=True)
os_new.rename(columns = {1 : "Profit 2016"}, inplace=True)
os_new.rename(columns = {2 : "Profit 2017"}, inplace=True)
os_new.reset_index(drop=True, inplace=True)  # Resetting the index here

explode = (0, 0, 0, 0, 0, 0)
labels = os_new['Warehouse Location'].tolist()
colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightcyan', 'lightblue']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

os_new.plot(kind="pie", y='Profit 2016', autopct='%.2f%%',
            shadow=True, explode=explode, legend=False, colors=colors_mine,
            ax=axes[0], labels=labels, fontsize=10)

os_new.plot(kind="pie", y='Profit 2017', autopct='%.2f%%',
            shadow=True, explode=explode, legend=False, colors=colors_mine,
            ax=axes[1], labels=labels, fontsize=10)
plt.tight_layout()
plt.show()
sPicNameOut1=GBase+'pie_explode.png'
plt.tight_layout()
plt.savefig(sPicNameOut1,dpi=600)

os_new.iloc[:5].plot(figsize=(10, 10),kind='line',x='Warehouse Location',\
           y=['Profit 2016','Profit 2017']); 
sPicNameOut3=GBase+'line.png'
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut3,dpi=600)

os_new.iloc[:5].plot(figsize=(10, 10),kind='bar',x='Warehouse Location',\
           y=['Profit 2016','Profit 2017']); 
sPicNameOut4=GBase+'bar.png'
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut4,dpi=600)

os_new.iloc[:5].plot(figsize=(10, 10),kind='barh',x='Warehouse Location',\
           y=['Profit 2016','Profit 2017']);
sPicNameOut5=GBase+'hbar.png'
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut5,dpi=600)

os_new.iloc[:5].plot(figsize=(10, 10),kind='area',x='Warehouse Location',\
           y=['Profit 2016','Profit 2017'],stacked=False);
sPicNameOut6=GBase+'area.png' 
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut6,dpi=600)

os_new.iloc[:5].plot(figsize=(10, 10),kind='scatter',x='Profit 2016',\
           y='Profit 2017',color='DarkBlue',marker='D'); 
sPicNameOut7=GBase+'scatter.png'
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut7,dpi=600)

os_new.iloc[:5].plot(figsize=(13, 10),kind='hexbin',x='Profit 2016',\
           y='Profit 2017', gridsize=25); 
sPicNameOut8=GBase+'hexbin.png' 
plt.tight_layout()
plt.show()
plt.savefig(sPicNameOut8,dpi=600)
