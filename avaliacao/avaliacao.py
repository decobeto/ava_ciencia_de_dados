import pandas
import matplotlib.pyplot as plt
import numpy as np
from seaborn import heatmap

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

plt.scatter(data['domestic_consumption'],data['exports'])
plt.xlabel("Consumo Doméstico")
plt.ylabel("Exportações")
plt.show()

plt.plot(data['exports_crop_year'], data['country'], color="red",marker="x",linestyle="solid")
plt.plot(data['total_production'], data['country'], color="green",marker="o",linestyle="solid")

plt.title("Relação de Safra de Exportações e Produção Total")
plt.legend(['Safras Exportadas','Produção Total'])
plt.ylabel("Total")
plt.xlabel("Total")
plt.show()

plt.plot(data['exports_crop_year'], data['country'], color="red",marker="x",linestyle="solid")
plt.plot(data['domestic_consumption'], data['country'], color="green",marker="o",linestyle="solid")

plt.title("Relação de Safra de Exportações e Consumo Doméstico")
plt.legend(['Safras Exportadas','Consumo Doméstico'])
plt.ylabel("Total")
plt.xlabel("Total")
plt.show()

plt.bar(data['country'], data['domestic_consumption'])

plt.title("Consumo doméstico por país")
plt.ylabel("Total")
plt.xlabel("País")

plt.show()

plt.bar(data['country'], data['exports'])

plt.title("Exportações por país")
plt.ylabel("Total")
plt.xlabel("País")

plt.show()

plt.bar(data['country'], data['total_production'])

plt.title("Produção total por país")
plt.ylabel("Total")
plt.xlabel("País")

plt.show()

data[['domestic_consumption']] = data.domestic_consumption.fillna(data.domestic_consumption.mean())

correlation =  data.total_production.corr(data.domestic_consumption)
print (f"A correlação do pandas deu {correlation}")

np.corrcoef(data.domestic_consumption, data.total_production)
print (f"A correlação do numpy deu {correlation}")