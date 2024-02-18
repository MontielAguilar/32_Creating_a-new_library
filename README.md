# Exercise for Naive Model Development in Python

<a href="https://cdn.pixabay.com/photo/2013/07/13/12/03/flag-159070_1280.png" target="_blank" rel="noopener noreferrer">
  <img src="https://cdn.pixabay.com/photo/2013/07/13/12/03/flag-159070_1280.png" height="30" alt="Bandera">
</a>

This exercise aims to apply basic programming knowledge in Python, focusing on future developments related to machine learning models. The following components will be developed:

## 1. Script NaiveModel.py

This script contains a class called `NaiveModel`, which has 5 public methods:

1. `__init__`: Initialization method of the class.
2. `fit`: Method to calculate the mean of each column of the training data.
3. `predict`: Method to scale new data by dividing them by the corresponding column mean.
4. `save`: Method to save the calculated means to disk.
5. `load`: Method to load the saved means from disk.

## 2. Files outside the package

### 2.1. train_model.py

This file imports the `models` package and creates a `NaiveModel` object, trains it with a dataset, and saves the trained model to disk.

### 2.2. inference_model.py

This file also imports the `models` package, creates a `NaiveModel` object, loads the previously trained model from disk, performs inference on new data, and saves the results to a CSV file.

## Usage

1. Run `train_model.py` to train the model and save it to disk.
2. Run `inference_model.py` to load the trained model, perform inferences with new data, and save the results to a CSV file.

## Dependencies

* Python 3.11
* Pandas
* Pickle

## Resources

* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Python pickle Module](https://docs.python.org/3/library/pickle.html)

## Example Data

The dataset used for this exercise comes from [datahub.io](https://datahub.io/machine-learning/mnist_784#resource-mnist_784), and consists of a dataset of handwritten digits (MNIST).

## Additional Notes

* It is suggested to install all required packages with pip.



# Ejercicio de Desarrollo de Modelo Naive en Python

<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bandera_de_Espa%C3%B1a_%28sin_escudo%29.svg/2560px-Bandera_de_Espa%C3%B1a_%28sin_escudo%29.svg.png" target="_blank" rel="noopener noreferrer">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bandera_de_Espa%C3%B1a_%28sin_escudo%29.svg/2560px-Bandera_de_Espa%C3%B1a_%28sin_escudo%29.svg.png" height="30" alt="Bandera de España">
</a>

Este ejercicio tiene como objetivo aplicar conocimientos básicos de programación en Python, orientándose hacia futuros desarrollos relacionados con modelos de machine learning. Se desarrollarán los siguientes componentes:

## 1. Script NaiveModel.py

Este script contiene una clase llamada `NaiveModel`, que tiene 5 métodos públicos:

1. `__init__`: Método de inicialización de la clase.
2. `fit`: Método para calcular la media de cada columna de los datos de entrenamiento.
3. `predict`: Método para escalar nuevos datos dividiéndolos por la media correspondiente a su columna.
4. `save`: Método para guardar en disco las medias calculadas.
5. `load`: Método para cargar desde disco las medias guardadas.

## 2. Archivos fuera del paquete

### 2.1. train_model.py

Este archivo importa el paquete `models` y crea un objeto `NaiveModel`, lo entrena con un conjunto de datos y guarda el modelo entrenado en disco.

### 2.2. inference_model.py

Este archivo también importa el paquete `models`, crea un objeto `NaiveModel`, carga el modelo previamente entrenado desde disco, realiza la inferencia de nuevos datos y guarda los resultados en un archivo CSV.

## Uso

1. Ejecutar `train_model.py` para entrenar el modelo y guardarlo en disco.
2. Ejecutar `inference_model.py` para cargar el modelo entrenado, realizar inferencias con nuevos datos y guardar los resultados en un archivo CSV.

## Dependencias

- Python 3.11
- Pandas
- Pickle

## Recursos

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python pickle Module](https://docs.python.org/3/library/pickle.html)

## Ejemplo de Datos

El conjunto de datos utilizado para este ejercicio proviene de [datahub.io](https://datahub.io/machine-learning/mnist_784#resource-mnist_784), y consiste en un conjunto de datos de dígitos escritos a mano (MNIST).

## Notas Adicionales

- Se sugiere instalar todos los paquetes requeridos con pip.
