import pandas as pd
import numpy as np

def get_csv(ruta):
    return pd.read_csv(ruta,index_col=0)
def remove_negative_values(data,column):
    data[column] = data[column].apply(lambda x: np.nan if x < 0 else x)
    return data
def remove_outlier_values(data,column,threshold = 2):
    #promedio
    prom = data[column].mean()
    #desviacion estandar 
    std = data[column].std()
    #mascara del filtrado
    data[column] = data[column].mask(np.abs((data[column] - prom) / std) > threshold, np.nan)
    return data
def map_column_values(data,column,mapping):
    data[column] = data[column].apply(lambda val: mapping.get(val,val))
    return data

def fill_na_in_column(data,column,fill_value):
    data[column] = data[column].fillna(fill_value)
    return data
def cast_to_int(data,column):
    data[column] = data[column].astype(int)
    return data
def preprocess_data(data):
    education_mapping = {
    'Género' : 'Genero',
    'mastre' : 'Master',
    'pHd' : 'PhD',
    'Bachelors' : 'Bachelor',
    'no education' : 'NE',
    'NaN' : 'Desconocido'
    }
    gender_mapping = {
        'f' : 'F',
        'm' : 'M'
    }
    return (
        data.pipe(remove_negative_values,'Edad')
        .pipe(remove_negative_values,'Ingresos')
        .pipe(remove_negative_values,'Altura')
        .pipe(remove_outlier_values,'Edad')
        .pipe(remove_negative_values,'Hijos')
        .pipe(remove_negative_values,'Altura')
        .pipe(map_column_values,'Género',gender_mapping)
        .pipe(map_column_values,'Nivel_Educación',education_mapping)
        .pipe(fill_na_in_column,'Edad',data['Edad'].median())
        .pipe(fill_na_in_column,'Ingresos',data['Ingresos'].mean())
        .pipe(fill_na_in_column,'Altura',data['Altura'].mean())
        .pipe(fill_na_in_column,'Ciudad','Desconocida')
        .pipe(fill_na_in_column,'Nivel_Educación','Desconocido')
        .pipe(fill_na_in_column,'Hijos',data['Hijos'].median())
    )
data = get_csv('/home/nicolasrodrigeztorres04/Documents/machine_Learning*2/datasets/tratamiento_datos.csv')
print(data)
preprocess_data(data=data)
print(data)
