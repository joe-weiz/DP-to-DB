# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:09:12 2019

@author: JWeiz
"""

#import pandas as pd
from pandas import read_clipboard
from pandas import melt
from datetime import datetime

#record the time of capture
now = datetime.now()

#Ask user for SKU
sku = input("Type the lazy code of the SKU you're capturing: ") 

#read the clipboard into a dataframe
df = pd.read_clipboard(sep='\t', header = [0,1,2])

#reshape the dataframe into 'tall' or 'stacked' format
dfmelt = pd.melt(df,id_vars = [(' ',' ',' '),(' ', ' ', ' .1')])

#create a column and set it to equal the capture timestamp
dfmelt['timestamp'] = now

#create a column and set it to equal the
dfmelt['lazycode'] = sku

#copy reshaped dataframe back into clipboard
dfmelt.to_clipboard()
