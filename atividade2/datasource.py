
import urllib.request
import pandas as pd
import openpyxl
import pandas_profiling
import numpy as np
from scipy import stats
import matplotlib.pyplot as plot


try:    
    f = open("2.9.xlsx")
except IOError:
    print("Ops! Arquivo não encontrado, efetuando o download...")
    url = ("https://www.tesourotransparente.gov.br/ckan/dataset/fc2ea6ab-2130-4525-98f6-8bf04407f7fe/resource/ef6a250b-75bf-44c7-8c9f-8a746b6f469e/download/2.9.xlsx")    
    urllib.request.urlretrieve(url,'2.9.xlsx')
    
    
df = pd.read_excel("2.9.xlsx")
print(df)
print (df.dtypes)

# Remove outliers
# df = pd.DataFrame(np.random.rand(100, 3))
# df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

profile = pandas_profiling.ProfileReport(df)
profile.to_file('report.html')
print(df.shape)

print (df.describe().iloc[:, :2])
print ("Dados ausentes: " , df.isnull().sum())

mask = df.isnull().any(axis=1)

data = np.random.randn(20, 4)
dataFrame = pd.DataFrame(data=data, columns=['A', 'B', 'C', 'D'])
dataFrame.plot.scatter(x='C', y='D', title= "SCATTER PLOT")
plot.show(block=True)

dataFrame.plot.box(title="Fatores de Variação", grid=True)
plot.show(block=True)

dataFrame.plot.line(x="A", title="DPMFi - Variação")
plot.show(block=True)

dataFrame.plot.bar(x="A", y="B", rot=70, title="Variação A e B")
plot.show(block=True)

dataFrame.plot.bar(x="C", y="D", rot=70, title="Variação C e D")
plot.show(block=True)