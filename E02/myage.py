from datetime import datetime, timedelta
def età():
    v=[None] * 3
    data=["giorno","mese","anno"]
    for i in range(3):
       v[i]=input("Immetti "+data[i]+" di nascita ")
    mydate = datetime.strptime(v[0]+"/"+v[1]+"/"+v[2],"%d/%m/%Y")
    print("Data di nascita inserita: ")
    print(mydate)
    datenow = datetime.now()
    timediff = datenow - mydate
    tots = timediff.total_seconds()
    agey=tots//(365*24*60*60)
    aged=tots//(24*60*60)
    print("Anni {:}".format (agey))
    print("Giorni {:}".format (aged))
    print("Secondi {:}".format (tots))
    
età()
