import pandas as pd
#df == data frame
df = pd.read_csv("archivos\\datos.csv") #names=["nom", "ape"]) podemos cambiarle los nombres a las columnas
print(df)
df2 = pd.read_csv("archivos\\datos.csv")
#obteniendo datos de la columna nombre   
print(df["nombre"])
#print(df["nom"])

#ordenamos dataframe por la edad
#df_ord = df.sort_values("edad")
#print(df_ord)
print("---------------")
#ordenandolo de forma decendente
#df_ord_desend = df.sort_values("edad", ascending=False)
#print(df_ord_desend)
print("---------------")
#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])
print(df_concatenado)
print("---------------")

#accediendo a la primer fila con head()
p_fila= df.head(0)
print(p_fila)
print("---------------")
#accedienedo a las ultimas 3 filas con tail()
ul_fila = df.tail(3)
print(ul_fila)
print("---------------")

#accediendo a la cantidad de filas y colunas totales
filas, columnas = df.shape
print(f"filas: {filas}, columnas: {columnas}")
print("---------------")

#obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)
print("---------------")
