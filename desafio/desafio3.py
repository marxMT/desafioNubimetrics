import pandas as pd
import numpy as np
import utils
import json

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

def generate_df_required(data):
    df_sellers = pd.json_normalize(data,max_level=4, sep='-')
    df_sellers = df_sellers[['body-site_id','body-id','body-nickname','body-points']]
    df_sellers.columns = ['siteId','sellerId','sellerNickname','sellerPoints']
    positivo = df_sellers[df_sellers['sellerPoints']>0]
    cero =  df_sellers[df_sellers['sellerPoints']==0]
    negativo =  df_sellers[df_sellers['sellerPoints']<0]
    dic_df = dict({'positivo':positivo, 'cero':cero, 'negativo' : negativo})
    return dic_df

def storage_csv(dic_df):
    for k in dic_df:
        patron = 'MPE/2021/07/13/'
        patron = patron + k +'/'
        nombre_file = k + '.csv'
        ruta = utils.almacenamiento(patron,nombre_file)
        dic_df[k].to_csv(ruta, index= False)

if __name__=="__main__":
    file = 'data/Sellers.json'
    data = read_json(file)
    dic_df = generate_df_required(data)
    storage_csv(dic_df)
