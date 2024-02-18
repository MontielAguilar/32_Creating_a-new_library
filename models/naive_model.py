import pandas as pd
import pickle

class NaiveModel:
    """
    Clase NaiveModel (Es un baseline model o modelo ingenuo).
    En este caso sirve para establecer el punto de partida.
    """

    def __init__(self):
        """
        Inicializa la clase NaiveModel. (Mediante el uso de __init__ e iniciar atributos)
        Se mantiene el self como formalismo obligatorio
        Se mantiene means en None, para que sea usado posteriormente cuadno almacene medias.
        """
        self.means = None

    def fit(self, data):
        """
        Calcula la media de cada columna y la almacena en self.means.
        Denominación fit, con fin de entrenar modelo con datos de entrada.
        data (pd.DataFrame): Datos de entrada.
        """
        self.means = data.mean() #-> En este caso, means ya no esta en None, sino que hace la media de data (de todo el DF)

    def predict(self, data):
        """
        Escala los datos de entrada dividiendo cada valor por la media correspondiente.
        Fin: Hacer prediccioones una vez que el modelo has ido entrenado (por def fit)
        Datos: data (pd.DataFrame): Datos de entrada / Usa el mismo que fit
        Retorna: los datos escalados
        Recordar que: 
            Escalar busca por asi decirlo: 
                que todos los datos "tengan" una escala comun, de esta manera, el posible modelo de ML puede tener mayor rendimiento
                Esto ayuda, porque si los datos son diferentes, puede haber problemas de magnitudes, caracteristicas y demas historrias.
                Aunque por regla general se suele usar la normalización o la estandarización, aqui se hace una "especie de normalización"
                    basada en: asemejar los datos basados en las medias.
        """
        scaled_data = data.copy()                       #-> Hace una copia de data (del DF)
        for column in data.columns:                     #-> Itera entre columnas del data y le aplica el escalado
            scaled_data[column] /= self.means[column]   #-> Escala los datos (columna por columna) dividiendo por la media
        return scaled_data                              #-> Me retorna el DF escalado


    def save(self, filename):
        """
        Guarda las medias en un archivo pickle.
        filename: ruta del archivo
        Se serializa mediante dump
        """
        with open(filename, 'wb') as f:                 #-> Forma aprendida en el curso wb: write and open binary / y as f: para llamar al codigo de forma sencilla
            pickle.dump(self.means, f)                  #-> Abre el pickle en modo esritura y binario y serializa los elementos (convierte el objeto en secuencia de bytes)

    def load(self, filename):
        """
        Carga las medias desde un archivo pickle.
        filename: Ruta del archivo 
        """
        with open(filename, 'rb') as f:                 #-> Forma aprendida en el curso wb: write and open binary / y as f: para llamar al codigo de forma sencilla
            self.means = pickle.load(f)                 #-> Carga el archivo pickle acorde a f
