import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('Investigaciones/DB1.csv', delimiter=";")

columnas_deseadas = ['Nombre, Correo, Telefono']
df = df[columnas_deseadas]
duplicados = df.duplicated()



print(df[duplicados])




#print(duplicados)

#print(df.shape)
#print(df[df.isnull().any(axis=1)])

#df = df.dropna(axis=1, how='all')

#conteo_nan = df.isnull().any(axis=1).sum()
#print("Número de filas con al menos un NaN:", conteo_nan)