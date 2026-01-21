from operazioni import somma, sottrazione, moltiplicazione

def calcolatrice(operazione: str, a:float,b:float):
    if operazione == "somma":
        return somma(a,b)
    elif operazione == "sottrazione":
        return sottrazione(a,b)
    elif operazione == "moltiplicazione":
        return moltiplicazione(a,b)
    else:
        return None


if __name__=="__main__":
    print(calcolatrice("somma",3,5))
    print(calcolatrice("sottrazione",10,5))
    print(calcolatrice("moltiplicazione",1,5))
    print("operazione non valida:",calcolatrice("divisione",5,5))