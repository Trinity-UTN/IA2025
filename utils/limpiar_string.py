import re

def limpiar_string(cadena):
    # Eliminar espacios al principio y final
    cadena = cadena.strip()
    # Eliminar caracteres especiales (excepto letras, números y espacios)
    cadena = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]', '', cadena)
    # Eliminar múltiples espacios intermedios
    cadena = re.sub(r'\s+', ' ', cadena)
    # Capitalizar (primera letra en mayúscula)
    return cadena