# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:08:49 2018

@author: MMOHTASHIM
"""
#import pandas as pd
#import quandl
#api_key="icx5c5kKwwVUatF8syyD"
#df=quandl.get("FMAC/HPI_AK", authtoken=api_key)
#print(df.head())
#fiddy_states=pd.read_html("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")
##print(fiddy_states[0])
#print(fiddy_states[0][1])
#for abbv in fiddy_states[0][1][1:]:
#    print("FMAC/HPI_"+str(abbv))
#import pandas as pd
#import numpy as np
#df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55]},
#                   index = [2001, 2002, 2003, 2004])
#
#df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55]},
#                   index = [2005, 2006, 2007, 2008])
#
#df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'Low_tier_HPI':[50, 52, 50, 53]},
#                   index = [2001, 2002, 2003, 2004])
#concat=pd.concat([df1,df2,df3])
#print(concat)
#df4=df1.append(df2)
#print(df4)
#s=pd.Series([80,2,53],index=['HPI','Int_rate', 'US_GDP_Thousands'])
#df4=df1.append(s,ignore_index=True)
#e=np.array(df4[["HPI","Int_rate","US_GDP_Thousands"]])
#df4=pd.DataFrame(e,index = [2001, 2002, 2003, 2004,2005])
#df4.rename(columns={0:"HPI",1:"Int_rate",2:"GDP"},inplace=True)
#print(df4)
import pandas as pd
#
#df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55]},
#                   index = [2001, 2002, 2003, 2004])
#
#df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55]},
#                   index = [2005, 2006, 2007, 2008])
#
#df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Unemployment':[7, 8, 9, 6],
#                    'Low_tier_HPI':[50, 52, 50, 53]},
#                   index = [2001, 2002, 2003, 2004])
#print(pd.merge(df1,df2,on=["HPI","Int_rate"]))
#df1.set_index("HPI",inplace=True)
#df3.set_index("HPI",inplace=True)
#df5=df1.join(df3)
#print(df5)
#df1 = pd.DataFrame({
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55],
#                    'Year':[2001, 2002, 2003, 2004]
#                    })
#
#df3 = pd.DataFrame({
#                    'Unemployment':[7, 8, 9, 6],
#                    'Low_tier_HPI':[50, 52, 50, 53],
#                    'Year':[2001, 2003, 2004, 2005]})
#df1.set_index("Year",inplace=True)
#df3.set_index("Year",inplace=True)
#print(df1.merge(df3,on="Year",how="outer"))

import quandl 
df=quandl.get("EOD/HD",authtoken="fwwt3dyY_pF8LyZqpNsa")
print(df)