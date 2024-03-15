def load(file, context):
    """Función invocada cuando se carga un archivo en un bucket
    Args:
         file (dict): Información del archivo cargado.
         context (google.cloud.functions.Context): Información de los metadatos del evento.
    """
    print('Le damos la bienvenida al nuevo héroe')
    for k in file:
      print(k, '=', file[k])