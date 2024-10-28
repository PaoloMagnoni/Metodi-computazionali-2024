ggsett=["Lunedì","Martedì","Mercoledì", "Giovedì","Venerdì", "Sabato", "Domenica"]
ggsett_5=ggsett*5
dicc={}
for i in range(31):
    dicc.update({"{:}".format(i+1):ggsett_5[i]})
print(dicc)
    
