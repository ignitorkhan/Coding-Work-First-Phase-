# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:14:01 2018

@author: MMOHTASHIM
"""
import pandas as pd
import quandl
import pickle
api_key="fwwt3dyY_pF8LyZqpNsa"
def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]
    
#the code works but data has changed therefore it might show a NotFoundError
def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.merge(df,on="Date")
    return main_df        
    



#pickle_in=open('fiddy_states.pickle','rb')
#Data=pickle.load(pickle_in)
#pickle_in.close()
#Data.to_pickle("pickle pickle")
#data_2=pd.read_pickle("pickle pickle")
