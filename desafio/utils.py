import os, os.path
import  errno

def almacenamiento(name_carpeta,name_file):
    """
        input: nombre de carpeta destino
        output:
             ruta  almacenar  file
    """
    try:
        os.makedirs(name_carpeta)
        carpeta = os.getcwd() + '/'+name_carpeta
        ruta_almacen = os.path.join(os.sep, carpeta, name_file)
        return ruta_almacen
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise