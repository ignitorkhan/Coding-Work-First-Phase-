# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:14:12 2018

@author: MMOHTASHIM
"""
import sys
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
from IPython import get_ipython
style.use("ggplot")
api_key=api_key="fwwt3dyY_pF8LyZqpNsa"

#df=quandl.get("FMAC/HPI_TX",authtoken=api_key)
#df["Value"]=((df["Value"]-df["Value"][0])/df["Value"][0])*100.0
#print(df)
#df_2=quandl.get("ZILLOW/C25706_ZRISFRR",authtoken=api_key)
#df_2["Value"]=((df_2["Value"]-df_2["Value"][0])/df_2["Value"][0])*100.0
#df_3=df.merge(df_2,on="Date",how="inner")
#df_3.rename(columns={"Value_x":"Value FSD","Value_y":"Value LHR"},inplace=True)
##df_3["Value FSD2"]=df_3["Value FSD"]*2
#print(df_3.head())
#get_ipython().run_line_magic('matplotlib', 'qt')
#df_3.plot()
#plt.legend().remove()
#plt.show()
#list_2=["DCMFINSERV","3PLAND","PRSMJOHNSN","HITECH","ORIENTELEC","ICICI500","INDOSTAR","BOROSIL","PITTIENG","IBULISL"]
#df=quandl.get("URC/NYSE_52W_HI",authtoken=api_key)
#main_dataframe=pd.DataFrame()
#for char in list_2:
#    df_2=quandl.get("NSE/"+char,authtoken=api_key)
#    if main_dataframe.empty:
#        main_dataframe=df_2
#    else:
#        main_dataframe=main_dataframe.merge(df_2,on="Date",how="inner")
#print(main_dataframe)
get_ipython().run_line_magic('matplotlib', 'qt')
#df_2=pd.read_pickle("pickle pickle")
#df_2_correlation=df_2.corr()



#####################################
#df["NSA_oneyear"]=df["NSA Value"].resample("A",how="mean")
#fig=plt.figure()
#ax1=plt.subplot2grid((1,1),(0,0))
##df.dropna(inplace=True)
#i= df.isnull().values.sum()
#print(i)
##df.fillna(method="b/ffill")
#df.fillna(value=sys.maxsize,limit=int(i*.50),inplace=True)
#print(df.head())
#df.plot(ax=ax1)
#plt.legend()
#plt.show()
#######################################
#df=quandl.get("FMAC/HPI_TX",authtoken=api_key)
#print(df.head())
#df["NSA_mean"]=df["NSA Value"].rolling(window=12).mean()
#df["NSA_std"]=df["NSA Value"].rolling(window=12).std()
#df["SA Value"]
#print(df)
#fig=plt.figure()
#ax1=plt.subplot2grid((2,1),(0,0))
#ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)
#df[["NSA Value","NSA_mean"]].plot(ax=ax1)
#df["NSA_std"].plot(ax=ax2)
#plt.legend()
#plt.show()
#df["NA_corr"]=df["NSA Value"].rolling(window=12).corr(df["SA Value"])
#print(df) 
#df[["NSA Value","SA Value"]].plot(ax=ax1)
#df["NA_corr"].plot(ax=ax2,label="NA_corr")
#plt.legend()
#plt.show() 
########################################
#
#i=0
#bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
#df=pd.DataFrame(bridge_height)
#df["STD"]=df["meters"].rolling(2).std()
#df_std=df.describe()
#df=df[(df["STD"]<df_std["meters"]["std"])]      
#print(df)
#df["meters"].plot()
#plt.show()
## 
#################################################################
import pandas as pd
import quandl
import pickle
import numpy as py
from statistics import mean
from sklearn import svm,preprocessing,cross_validation
api_key="fwwt3dyY_pF8LyZqpNsa"
#def state_list():
#    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#    return fiddy_states[0][1][1:]
#    
##the code works but data has changed therefore it might show a NotFoundError
#def grab_initial_state_data():
#    states = state_list()
#
#    main_df = pd.DataFrame()
#
#    for abbv in states:
#        query = "FMAC/HPI_"+str(abbv)
#        df = quandl.get(query, authtoken=api_key)
#        del df["SA Value"]
#        df.columns=[abbv]
#        df[abbv]=((df[abbv]-df[abbv][0])/df[abbv][0])*100
#        if main_df.empty:
#            main_df = df
#        else:
#            main_df = main_df.merge(df,on="Date")
#    main_df.to_pickle("main data.pickle")
#    return main_df     
#def mortgage_30y():
#    df=quandl.get("FMAC/MORTG",trim_start="1975-01-01",authtoken=api_key)
#    df["Value"]=((df["Value"]-df["Value"][0])/df["Value"][0])*100
#    df=df.resample("M").mean()
#    df.columns=["M30"]
#    return df
#def HPI_benchmark():
#    df=quandl.get("FMAC/HPI_USA",authtoken=api_key)
#    del df["SA Value"]
#    df.columns=["USA_HPI"]
#    df["USA_HPI"]=((df["USA_HPI"]-df["USA_HPI"][0])/df["USA_HPI"][0])*100
#    return df
#def sp500_data():
#    df = quandl.get("BCB/7443",trim_start="1975-01-01",authtoken=api_key)
#    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
#    df=df.resample('M').mean()
#    df.rename(columns={'Value':'BUSINESS INDEX'}, inplace=True)
#    df = df['BUSINESS INDEX']
#    return df
#
#def gdp_data():
#    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
#    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
#    df=df.resample('M').mean()
#    df.rename(columns={'Value':'GDP'}, inplace=True)
#    df = df['GDP']
#    return df
#
#def us_unemployment():
#    df = quandl.get("BCB/3787", trim_start="1975-01-01", authtoken=api_key)
#    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
#    df=df.resample('1D').mean()
#    df=df.resample('M').mean()
#    df.rename(columns={'Value':'Unemployment'}, inplace=True)
#    return df
#
#
#
#sp500_data=sp500_data()
#US_GDP=gdp_data()
#us_unemployment=us_unemployment()
#m_30=mortgage_30y()
#HPI_bench=HPI_benchmark()
#HPI_Data=pd.read_pickle("main data.pickle")
#HPI=HPI_Data.join([m_30,sp500_data,US_GDP,us_unemployment,HPI_bench])
#HPI=HPI.dropna()
#HPI.to_html("HPI data.html")
#HPI.to_pickle("HPI data.pickle")
#print(HPI)
#print(HPI.corr())
#######################################################################
def createlabels(f_hpi,c_hpi):
    if f_hpi>c_hpi:
        return 1
    else:
        return 0
def moving_averages(values):
    return mean(values)

housing_data=pd.read_pickle("HPI data.pickle")
housing_data=housing_data.pct_change()
housing_data.replace([py.inf,-py.inf],py.nan)
housing_data.dropna(inplace=True)
housing_data["USA_HPI_Future"]=housing_data["USA_HPI"].shift(-1)
housing_data.dropna(inplace=True)
print(housing_data[["USA_HPI_Future","USA_HPI"]])

housing_data["labels"]=list(map(createlabels,housing_data["USA_HPI_Future"],housing_data["USA_HPI"]))
housing_data.dropna(inplace=True)

#housing_data["M30_mean_hpi"]=housing_data["M30"].rolling(10).apply(moving_averages)
#housing_data.dropna(inplace=True)
#print(housing_data.tail())
#X=py.array(housing_data.drop(["labels","USA_HPI_Future"],1))
#y=py.array(housing_data["labels"])
#X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)
#clf=svm.SVC(kernel="linear")
#clf.fit(X_train,y_train)
#print(clf.score(X_test,y_test))


