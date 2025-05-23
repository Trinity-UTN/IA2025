import time
from django.http import JsonResponse
from datetime import datetime

class BaseResponse ():
    """BaseResponse
    Template de respuesta http
    Args:
        data (any)
        status (int)
        message (str)
        errors (str[])
    Returns:
        _type_: _description_
    """
    @classmethod
    def response (cls, data = None, status=200, message="", errors=None):
        
        return JsonResponse(
            {
            "data": data, 
            "message": message,
            "errors": errors,
            "timestamp":  datetime.utcnow().isoformat() + 'Z'
            }, 
            status=status)
    
    @classmethod
    def response_paginated (cls, data = None, status=200, message="", errors=None):
        return JsonResponse(
            {
            "data": data['results'],
            "count": data['count'],
            "total_pages": data['total_pages'],
            "current_page": data['current_page'],
            "page_size": data['page_size'], 
            "message": message,
            "errors": errors,
            "timestamp":  datetime.utcnow().isoformat() + 'Z'
            }, 
            status=status)