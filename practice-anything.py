
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15)
clf=LinearRegression()
clf.fit(X_train.reshape(-1, 1), y_train)
print(clf.score(X_test.reshape(-1, 1), y_test))
print(df)

    time+=unix_day
    df.loc[current_date]=[np.nan for _ in range(len(df.columns)-1)] +[i]

print(df)
py.plot(df["GDP"])
py.plot(df["Forecasted GDP"])
py.legend()
py.show()
