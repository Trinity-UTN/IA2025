from rest_framework import viewsets
from rest_framework.decorators import action
from clase_16_05.service import ServiceIA
from utils.base_response import BaseResponse

class ChatBotViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["post"])
    def analizar(self, request):
        return BaseResponse.response(
            ServiceIA.analizar_sentimiento(request.data["reseña"],request.data["nombre"]),
            200,
            "created",
            None
        )
    
    def create(self, request):
        return BaseResponse.response(ServiceIA.procesar_reseñas_y_guardar_dataset(), 200, "created", None)
    
    
