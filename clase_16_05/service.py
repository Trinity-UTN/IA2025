from transformers import pipeline

# Cargamos el modelo y tokenizer (solo una vez)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="finiteautomata/beto-sentiment-analysis",
    tokenizer="finiteautomata/beto-sentiment-analysis"
)

class ServiceIA:
    """ Service IA

    El mismo contiene la logica para poder analizar una reseña y retornar el sentimiento encontrado
    Functions:
        analizar_sentimiento: 
            - args: str reseña, str nombre
            - return: dict

        generar_dataset:
            - args: None
            - return: None
    """
    LABELS = {
        "POS": "Positivo",
        "NEG": "Negativo",
        "NEU": "Neutral"
    }

    @classmethod
    def analizar_sentimiento(cls, reseña: str, nombre: str) -> dict:
        """Analizar sentimiento
        Funcion que utiliza la inteligencia artificial para analizar el sentimiento de una reseña
        Args:
            reseña (str): Reseña de algo
            nombre (str): Nombre de la reseña

        Returns:
            dict: {
                "nombre": str,
                "reseña": str,
                "sentimiento": str,
                "confianza": float
            }
        """

        if not reseña or not nombre:
            return {"error": "Se requieren 'nombre' y 'reseña'"}

        resultado = sentiment_analyzer(reseña)[0]

        return {
            "nombre": nombre,
            "reseña": reseña,
            "sentimiento": cls.LABELS.get(resultado["label"], "Desconocido"),
            "confianza": round(resultado["score"], 4)
        }
    
    @classmethod
    def generar_dataset(cls):
        """Generar Dataset
        El mismo genera un dataset etiquetado a partir de una lista de reseñas.
        El data set tiene el siguiente formato:

        reseña, sentimiento

        Args:
            reseñas (_type_): _description_
        Returns:
            _type_: _description_
        """
        
        entrada='C:/Users/Usuario/OneDrive/Paginas Web/ClaseIA/IA2025/clase_16_05/reseñas_sistemas.txt'
        
        #Nombre del data set de salida
        salida="dataset.txt"

        resultados = []

        #Obtenemos las reseñas del archivo antes mencionado
        with open(entrada, "r", encoding="utf-8") as f:
            reseñas = [line.strip().strip('"') for line in f if line.strip()]

        # Analizamos las reseñas con la funcion analizar_sentimiento
        # En la misma nos genera un diccionario con la reseña y el sentimiento
        for i, reseña in enumerate(reseñas):
            resultado = ServiceIA.analizar_sentimiento(reseña, nombre=f"Reseña {i+1}")
            resultados.append((reseña, resultado["sentimiento"]))

        # Guardar el dataset como CSV-like (con comillas)
        with open(salida, "w", encoding="utf-8") as f:
            for reseña, sentimiento in resultados:
                reseña_limpia = reseña.replace('"', '""')  # Escapamos comillas
                f.write(f'"{reseña_limpia}","{sentimiento}"\n')

        return None