import quandl
import pandas as pd
api_key="fwwt3dyY_pF8LyZqpNsa"
df=quandl.get("NASDAQOMX/XNDXT25",auth_token="fwwt3dyY_pF8LyZqpNsa")
df_2=quandl.get("NASDAQOMX/XNDXS2NNR",auth_token="fwwt3dyY_pF8LyZqpNsa")
df=df.merge(df_2,on="Trade Date",how="outer")
df=df.rename(columns={"Index Value_x":"Total Index Return","High_x":"Total Index High",
                   "Low_x":"Total Index Low","Total Market Value_x":"Total Index_ Total Market Value",
                   "Index Value_y":"SM Return","High_y":"SM  High",
                   "Low_y":"SM  Low","Total Market Value_y":"SM _ Total Market Value"})
df.drop(['Dividend Market Value_y', 'Dividend Market Value_x',"SM _ Total Market Value"],axis=1,inplace=True)
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
df.to_csv("Main Data.csv")
