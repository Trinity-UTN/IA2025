from transformers import pipeline

# Cargamos el modelo y tokenizer (solo una vez)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="finiteautomata/beto-sentiment-analysis",
    tokenizer="finiteautomata/beto-sentiment-analysis"
)

class ServiceIA:
    LABELS = {
        "POS": "Positivo",
        "NEG": "Negativo",
        "NEU": "Neutral"
    }

    @classmethod
    def analizar_sentimiento(cls, reseña: str, nombre: str) -> dict:
        if not reseña or not nombre:
            return {"error": "Se requieren 'nombre' y 'reseña'"}

        resultado = sentiment_analyzer(reseña)[0]

        return {
            "nombre": nombre,
            "reseña": reseña,
            "sentimiento": cls.LABELS.get(resultado["label"], "Desconocido"),
            "confianza": round(resultado["score"], 4)
        }