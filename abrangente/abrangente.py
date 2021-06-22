import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

data_paths=[
    "archive/domestic-consumption.csv",
    "archive/exports-calendar-year.csv",
    "archive/exports-crop-year.csv",
    "archive/gross-opening-stocks.csv",
    "archive/total-production.csv"
]

df = [pandas.read_csv(data_path) for data_path in data_paths]

def get_means(df):
    df = df.copy()
    countries = df[df.columns[0]]
    mean = df.mean(axis=1)
    df = pandas.concat([countries,mean],axis=1)
    df.columns = ['country',countries.name]
    return df

def make_df(dfs):
    processed_dfs = []
    
    for df in dfs:
        processed_dfs.append(get_means(df))
        
    df = processed_dfs[0]
    
    for i in range(1, len(processed_dfs)):
        df = df.merge(processed_dfs[i], on='country')
    
    return df

data = make_df(df)

print(data)

def preprocess_inputs(df):
    df = df.copy()

    df = df.drop('country', axis=1)
    
    y = df['total_production']
    X = df.drop('total_production', axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=1)
    
    return X_train, X_test, y_train, y_test
  
X_train, X_test, y_train, y_test = preprocess_inputs(data)

print("-----------------------------------")
print(X_train)
print("-----------------------------------")
print(y_train)

model = RandomForestRegressor()
model.fit(X_train, y_train)
print("Modelo Treinado!")

y_pred = model.predict(X_test)

rmse = np.sqrt(np.mean((y_test - y_pred)**2))
print("RMSE: {:.2f}".format(rmse))

r2 = 1 - (np.sum((y_test - y_pred)**2) / np.sum((y_test - y_test.mean())**2))
print("R^2: {:.5f}".format(r2))