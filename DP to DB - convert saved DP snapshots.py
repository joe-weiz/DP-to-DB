# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:09:12 2019

@author: JWeiz
"""

from pandas import read_clipboard
from pandas import melt
#from datetime import datetime


#read the clipboard into a dataframe
df = read_clipboard(sep='\t', header = [0,1,2])

#record the time of capture
now = df.columns[0][0]

#capture lazycode
sku = df.columns[0][1]

#reshape the dataframe into 'tall' or 'stacked' format
dfmelt = melt(df,id_vars = [(now,sku,' '),(' ', ' ', ' ')])

#create a column and set it to equal the capture timestamp
dfmelt['timestamp'] = now

#create a column and set it to equal the
dfmelt['lazycode'] = sku

#rename account columns
dfmelt = dfmelt.rename(columns={(now,sku,' '): "Account1", 
                                (' ', ' ', ' '): "Account2",
                                'variable_0':'PeriodWeek',
                                'variable_1':'Datatype_Weekday',
                                'value':'Demand'})

#I believe this column is useless. It just shows "Value" every row.
#Comment the line out if you want to keep the column.
dfmelt = dfmelt.drop(columns = 'variable_2')

#copy reshaped dataframe back into clipboard
dfmelt.to_clipboard()
