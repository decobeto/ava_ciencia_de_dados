import pandas
import matplotlib.pyplot as plt
import numpy as np

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