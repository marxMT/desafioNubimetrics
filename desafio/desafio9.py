from datetime import datetime,timedelta

def generateLastDaysPaths(date, days):
    lista=[]
    url_base = "https://important@location/"
    date_inicial = datetime.strptime(date, "%Y%m%d")-timedelta(days)
    for i in range(days):
        date_inicial+=timedelta(1)
        url = url_base +date_inicial.strftime('%Y/%m/%d/')
        lista.append(url)
    return lista
if __name__=="__main__":
    l = generateLastDaysPaths("20210410",10)
    for i in l:
        print(i)
