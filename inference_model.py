from models.naive_model import NaiveModel
import pandas as pd

def main():
    """
    denominamos main porque es la función principal de este .py
    carga de modelo
    Lectura de DF el cual llamamos new_data
    aplicamos prediccion
    guardamos prediccion
    """
    model = NaiveModel()                                #-> El modelo es el creado por la "libreria" models.naive_model

    model.load(r'G:\Mi unidad\1 DS\1 Archivos py\naive_model.pkl')  
                                                        #-> Cargamos el modelo

    new_data = pd.read_csv(r'G:\Mi unidad\1 DS\1 Archivos py\ejercicio 5\csv\mnist_784_csv.csv') 
                                                        # Importamos el archivo csv y lo lee

   
    predictions = model.predict(new_data)               #-Aqui esta la magia: Recordamos que teniamos un metodo llamado predict (en naive_model.py)

        
    predictions.to_csv('predictions.csv', index=False)  #-> Guardamos el nuevo DF csv

if __name__ == "__main__":
    main()

    """esta construcción permite que el código dentro de main() se ejecute solo cuando el script se ejecuta directamente, 
    y no cuando se importa como un módulo en otro script. """
