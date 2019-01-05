import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pylab as graph
import numpy as np
style.use('ggplot')
web_stats={"Day":["1",2,3,4,5,6],
           "Visitors":["43","53","34","45","34","64"],
           "Bounce Rate":[62,72,32,43,53,23]}
df=pd.DataFrame(web_stats)
df.set_index("Day",inplace=True)
print(df)
print(df["Visitors"])
print(np.array(df["Visitors"]))
#df2=pd.DataFrame(np.array(df[["Visitors","Bounce Rate"]]))
#print(df2)
#graph.figure(1)
#graph.plot(web_stats["Day"],web_stats["Visitors"])
#graph.show()
#df=pd.read_csv("ZILLOW-Z77006_ZRISFRR.csv")
#df.set_index("Date",inplace=True)
#print(df.head())
#df=pd.read_csv("newcsv.csv")
#print(df.head())
#df=pd.read_csv("newcsv.csv",index_col=0)
#print(df.head())
#df.columns=["Houston"]
#print(df.head())
##df.to_csv("newcsv3.csv")
##df.to_csv("newcsv4.csv",header=False)
##df=pd.read_csv("newcsv4.csv",names=["Date","Houston"],index_col=0)
##print(df.head())
##df.to_html("example.html")
#df=pd.read_csv("newcsv4.csv",names=["Date","Houston"])
#print(df.head())
#df.rename(columns={"Date":"Todate","Houston":"7706_hpt"},inplace=True)
#print(df.head())
#
#dic=[1,2,3,4]
#dic_2=[]
#dic_2.append(dic)
#dic=[3,4,6,7]
#dic_2.append(dic)
#print(dic_2)