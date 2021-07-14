import requests
import json
import os, os.path
import  errno
import utils

class Consulta_Api_ML:
    items=[]
    def __init__(self, ml_url):
        self.ml_url = ml_url

    def request_get(self,url):
        return requests.get(url).json()
    
    def busqueda(self, offset):
        url = self.ml_url
        url = url +'&offset='+str(offset)
        print('Buscando: '+ url)
        result_json = self.request_get(url)
        if(result_json is not None): self.items= result_json['results']
        print('Finalizo Busqueda: '+ url)


if __name__ == "__main__":
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA5725'
    ml_json = Consulta_Api_ML(url)
    ml_json.busqueda(1)
    ruta_almacen = utils.almacenamiento('searchjson202107','result_json.json')
    with open(ruta_almacen,'w') as file:
        json.dump(ml_json.items, file)
        print("Finalizo la carga ........")
    