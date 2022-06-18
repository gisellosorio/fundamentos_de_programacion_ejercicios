def ordenes(rutinaContable):
    from functools import reduce 
    #1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)]
    #               4*25842      +       18*23254.99
    #Sumar el total de cada tupla de cada lista
    h=list(map(lambda l: [l[0]]+list(map(lambda p:p[1]*p[2],l[1:])),rutinaContable))
    #    [1201, 103371.96, 418589.82, 440567.55]
    k=list(map(lambda c:[c[0]]+[reduce(lambda a,b:round(a+b,2),c[1:])],h))
    #    [[1201, 962529.33], [1202, 388477.56], [1203, 418859.8], [1204,2247.57]]
    w=list(map(lambda x: x if (x[1]>=600000) else(x[0],x[1]+25000),k))  
    # [[1201, 962529.33], (1202, 413477.56), (1203, 443859.8), (1204,27247.57)]
    print('----------------- Inicio Registro diario -----------------')
    for u in range(len(w)): # range(len(4)): 0 1 2 3
        print(f'La factura {w[u][0]} tiene un total en pesos de {w[u][1]:,.2f}')
    print('----------------- Fin Registro diario -----------------')

ejem1=[
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]

ordenes(ejem1)