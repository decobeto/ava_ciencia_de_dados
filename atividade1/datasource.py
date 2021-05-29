import urllib.request
import pandas as pd
import openpyxl
import pandas_profiling

try:    
    f = open("2.9.xlsx")
except IOError:
    print("Ops! Arquivo não encontrado, efetuando o download...")
    url = ("https://www.tesourotransparente.gov.br/ckan/dataset/fc2ea6ab-2130-4525-98f6-8bf04407f7fe/resource/ef6a250b-75bf-44c7-8c9f-8a746b6f469e/download/2.9.xlsx")    
    urllib.request.urlretrieve(url,'2.9.xlsx')
    
df = pd.read_excel("2.9.xlsx")
print(df)
print (df.dtypes)

profile = pandas_profiling.ProfileReport(df)
profile.to_file('report.html')
print(df.shape)

print (df.describe().iloc[:, :2])
print ("Dados ausentes: " , df.isnull().sum())

mask = df.isnull().any(axis=1)
