import pandas as pd
import numpy as nm

data = pd.read_csv('/home/nicolasrodrigeztorres04/Documents/machine_Learning*2/datasets/tratamiento_datos.csv')
print(data.info())
print(data['Nivel_Educación'])