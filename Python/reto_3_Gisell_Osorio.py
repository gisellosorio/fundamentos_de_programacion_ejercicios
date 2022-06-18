def AutoPartes(ventas:list):
    identificador=('IdProducto','dProducto','pnProducto','cvProducto', 'sProducto','nComprador','cComprador', 'fVenta')
    ventas=list((tuple([x[0] for x in ventas]),)+(tuple([x[1] for x in ventas]),)+(tuple([x[2] for x in ventas]),)+(tuple([x[3] for x in ventas]),)+(tuple([x[4] for x in ventas]),)+(tuple([x[5] for x in ventas]),)+(tuple([x[6] for x in ventas]),)+(tuple([x[7] for x in ventas]),))
    datos=dict(list(zip(identificador,ventas)))
    return datos
    
def consultaRegistro(ventas,idProducto):
    IdProducto=ventas['IdProducto']
    dProducto=ventas['dProducto']
    pnProducto=ventas['pnProducto']
    cvProducto=ventas['cvProducto']
    sProducto=ventas['sProducto']
    nComprador=ventas['nComprador']
    cComprador=ventas['cComprador']
    fVenta=ventas['fVenta']
    mensaje=''
    if idProducto in IdProducto:
        indice=-1
        for i in range(IdProducto.count(idProducto)):
            indice=IdProducto.index(idProducto,indice+1)            
            dProducto1=dProducto[indice]
            pnProducto1=pnProducto[indice]
            cvProducto1=cvProducto[indice]
            sProducto1=sProducto[indice]
            nComprador1=nComprador[indice]
            cComprador1=cComprador[indice]
            fVenta1=fVenta[indice]
            mensaje+=f'Producto consultado : {idProducto}  Descripción  {dProducto1}  #Parte  {pnProducto1}  Cantidad vendida  {cvProducto1}  Stock  {sProducto1}  Comprador {nComprador1}  Documento  {cComprador1}  Fecha Venta  {fVenta1}'+'\n'
    else:
        mensaje='No hay registro de venta de ese producto'
       
    return print(mensaje)

consultaRegistro(AutoPartes([(9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020'),    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),(9852,'Culata', 'XC9875',2,165,'Prueba error',1355846,'14/06/2020'),    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020'),    (9852,'Culata', 'XC9875',2,165,'Pepito Perez',1355846,'14/06/2020')]), 9852)
print()
