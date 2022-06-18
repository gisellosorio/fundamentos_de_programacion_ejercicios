def ordenes(rutinaContable):
    from functools import reduce                                    #Importar librerías
    sum_acum= lambda acumulador=0,elemento=0: acumulador+elemento
    print('------------------------ Inicio Registro diario ---------------------------------')
    for norden in rutinaContable:
        numorden=norden[0]
        cant=[x[1] for x in norden[1:]]
        uniprecio=[x[2] for x in norden[1:]]
        sub_total=list(map(lambda x,y: x*y,cant,uniprecio))
        total=reduce(sum_acum,sub_total,0)
        if total<600000:
            total+=25000
        mensaje=f'La factura {numorden} tiene un total en pesos de {total:,.2f}'
        print(mensaje)
    print('-------------------------- Fin Registro diario ----------------------------------')

ejem1=[
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]

ordenes(ejem1)