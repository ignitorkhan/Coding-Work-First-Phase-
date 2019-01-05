# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:08:49 2018

@author: MMOHTASHIM
"""
import pandas as pd
import matplotlib.pyplot as plt
import quandl
from statistics import mean
import numpy as np
from IPython import get_ipython
api_key="fwwt3dyY_pF8LyZqpNsa"
def get_data_company(company_name):
    df=quandl.get("EURONEXT/"+str(company_name),authtoken=api_key)
    df=pd.DataFrame(df["Last"])
    df.rename(columns={"Last":"Price"},inplace=True)
    df_2=df.resample("M").mean()
    return df_2
def get_data_euronext():
    df_2=pd.read_csv("EuroNext 100 Historical Data.csv")
    df_2=df_2.loc[0:6, :]
    df_2=pd.DataFrame(df_2[["Date","Price"]])
    return df_2
def calculate_beta(company_name):
    df=get_data_euronext()
    df_2=get_data_company(company_name)
    xs=np.array((df["Price"]))
    ys=np.array(df_2["Price"])
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    get_ipython().run_line_magic('matplotlib', 'qt')
    print("Your Beta is"+ str(m))
    regression_line = [(m*x)+b for x in xs]
    plt.scatter(xs,ys,color='#003F72')
    plt.plot(xs, regression_line)
    plt.show()
    return m, b





    