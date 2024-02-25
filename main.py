from matplotlib import pyplot as plt
from DataBase import DataBase
import scrapper
import time 
from datetime import datetime
import mailer

users = ["shayan5mouktar@gmail.com"]

fileName ="data.txt"
listPrix = []
listDate = []
def loop():
    if DataBase.fileExists(fileName):
        listPrix = list(map(lambda x : x,DataBase.getDataLinePrefixed(fileName,"Prices")))[0].split(";")
        listDate = list(DataBase.getDataLinePrefixed(fileName,"Dates"))[0].split(";")
    else:
        DataBase.createFile(fileName)
        DataBase.appender(fileName,True,["Dates:","Prices:"])
        loop()


    #time.sleep(3600*24)

    lastPrice = scrapper.getLastPrice()
    date_actuelle = datetime.now()
    lastDate = date_actuelle.strftime("%d/%m %H:%M")

    listPrix.append(lastPrice)

    listDate.append(lastDate)

    print(listPrix)
    print(listDate)
    
    DataBase.AppendDataLine(fileName,"Prices",lastPrice)
    DataBase.AppendDataLine(fileName,"Dates",lastDate)

    listPricesInt = [int(element) for element in listPrix]
    minPrix =min(listPricesInt)
    plt.title('Vol GVA-TNR 15/08 -> 6/09')
    plt.xlabel('Tps')
    plt.ylabel('CHF')
    plt.grid(True)



    plt.plot(listDate,listPricesInt, marker='o', linestyle='-')
    plt.xlim(min(listDate), max(listDate))
    for x, y in zip(listDate, listPricesInt):
        plt.text(x, y, f'{y}', fontsize=8, ha='left', va='bottom')
    chart_image_path = 'chart.png'
    plt.savefig(chart_image_path)

    message = "Minimum atteint: "+str(minPrix)
    object ="Prix GVA-TNR le "+ str(date_actuelle)
    destinataire = "shayan5mouktar@gmail.com"

    mailer.send(message, destinataire,chart_image_path,object)



    



    

loop()