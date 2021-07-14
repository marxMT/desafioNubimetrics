from datetime import datetime, timedelta

def generateMonthlyPathList(year, month, day):
    elementos =[]
    url_base = "https://important@location/"
    day = int(day)
    for i in range(1, day+1):
        i_str = str(i)
        tam_day = len(i_str)
        if tam_day==1:
            url = url_base + year+'/'+month+'/0'+str(i)+'/'
        else:
            url = url_base +year+'/'+month+'/'+str(i)+'/'
        elementos.append(url)
    return elementos
    
if __name__=="__main__":
    l = generateMonthlyPathList("2021","05","17")
    for i in l:
        print(i)