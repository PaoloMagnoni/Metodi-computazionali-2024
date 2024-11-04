import sys
sys.path.append("/home/paolomag/metodicomp/Metodi-computazionali-2024/E05")

def somma(n):
    s=0
    for i in range(n+1):
       s=s+i
    return s
def sommarad(n):
    s=0
    for i in range(n):
        s=s+i**0.5
    return s
def sommaprod(n):
    s=0
    p=1
    for i in range(n+1):
       s=s+i
    for i in range(1,n+1):
       p=p*i
    return s,p
def alfasomma(n,alfa=1):
    s=0
    for i in range(n+1):
        s=s+i**alfa
    return s
    
