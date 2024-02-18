import pandas as pd
from models.naive_model import NaiveModel

# Leer el conjunto de datos
data = pd.read_csv("https://datahub.io/machine-learning/mnist_784/r/mnist_784.csv") #-> Importamos los datos desde la web 
                                                                                    #-> Otra forma podría ser con pd.read_csv si estuviese descargado

# Crear y entrenar el modelo
model = NaiveModel()                                                                #-> igualamos palabra model a la clase NaiveModel()
model.fit(data)                                                                     #-> Entrenamos el modelo (recordamos: fit aqui es el metodo de naive_model.py)

# Guardar el modelo entrenado
model.save("naive_model.pkl")                                                       #-> Guardamos el modelo
