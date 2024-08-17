import pandas as pd
import numpy as np

data = pd.read_csv('/home/nicolasrodrigeztorres04/Documents/machine_Learning*2/datasets/tratamiento_datos.csv',index_col=0)
#print(data.describe())
#print(data.info())
data_subs = data.info()
# setear cada columna para sacar una lista de los datos que hay e cada columna
for i in data.columns:
    if  i != 'Ingresos' :
        set_data = set(data[i].to_list())
    #print(i,set_data)
"""
set_edad = set(data['Edad'].to_list())
set_genero = set(data['Género'].to_list())
set_ingresos = set(data['Ingresos'].to_list())
set_altura = set(data['Altura'].to_list())
set_ciudad = set(data['Ciudad'].to_list())
set_educacion = set(data['Nivel_Educación'].to_list())
set_hijos = set(data['Hijos'].to_list())
print(set_genero)"""

# 1. Tratamiento de datos
#este paso básicamente sirve para cambiar o tratar los valores negativos
data['Edad'] = data['Edad'].apply(lambda a: np.nan if a < 0 else a)
data['Ingresos'] = data['Ingresos'].apply(lambda a: np.nan if a < 0 else a)
data['Hijos'] = data['Hijos'].apply(lambda x: x*(-1) if x < 0 else x)

# 2. Imputación de datos
# en este metodo de imputacion se trae la media de cada columna, y si el dato no existe es decir,
#es nulo entonces se cambia por la media o el nuevo valor
for column in ['Edad','Ingresos','Hijos']:
    value_new = data[column].median()
    data[column] = data[column].fillna(value_new)
    
for col in ['Ciudad','Género']:
    moda = data[col].mode()[0]
    data[col] = data[col].fillna(moda)

    
#mapeo de datos, aqui se cambian los valores mal escritos por un diccionario
maping = {
    'Género' : 'Genero',
    'mastre' : 'Master',
    'pHd' : 'PhD',
    'Bachelors' : 'Bachelor',
    'no education' : 'NE'
}
data['Nivel_Educación'] = data['Nivel_Educación'].replace(maping)
#ahora s emanejan los datos nulos o que no aparecen 
data['Nivel_Educación'] = data['Nivel_Educación'].fillna('NE')

#casteo de datos
#en este paso se cambian los tipos de datos a los que más se ajsuten a las necesidades
data['Edad'] = data['Edad'].astype(int)
data['Ingresos'] = data['Ingresos'].astype(float)
data['Hijos'] = data['Hijos'].astype(int)

print(data['Nivel_Educación'])
print(data.info())


