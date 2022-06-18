def cliente(informacion:dict)->dict:
    id=informacion['id_cliente']
    nombre=informacion['nombre']
    edad=informacion['edad']
    primer_ingreso=informacion['primer_ingreso']
    apto=True
    if edad>18:
        valor_boleta=20000
        descuento=0.05
        atraccion='X-Treme'
        total_boleta=valor_boleta
        if primer_ingreso==True:
            total_boleta=valor_boleta*(1-descuento)
    elif edad>=15 and edad<=18:
        valor_boleta=5000
        descuento=0.07
        atraccion='Carros chocones'
        total_boleta=valor_boleta
        if primer_ingreso==True:
            total_boleta=valor_boleta*(1-descuento)
    elif edad>=7 and edad<15:
        valor_boleta=10000
        descuento=0.05
        atraccion='Sillas voladoras'
        total_boleta=valor_boleta
        if primer_ingreso==True:
            total_boleta=valor_boleta*(1-descuento)
    else:
        apto=False
        atraccion='N/A'
        total_boleta='N/A'

    datos={
        'nombre': nombre,
        'edad': edad,
        'atraccion':atraccion,
        'apto':apto,
        'primer_ingreso':primer_ingreso,
        'total_boleta':total_boleta
    }
    return datos


informacion={
    'id_cliente':1,
    'nombre':'Johana Fernandez',
    'edad':20,
    'primer_ingreso':True
}

print(cliente(informacion))

informacion={
    'id_cliente':2,
    'nombre':'Gloria Suarez',
    'edad':3,
    'primer_ingreso':True
}

print(cliente(informacion))

informacion={
    'id_cliente':3,
    'nombre':'Tatiana Suarez',
    'edad':17,
    'primer_ingreso':False #True
}

print(cliente(informacion))

informacion={
    'id_cliente':4,
    'nombre':'Tatiana Ruiz',
    'edad':8,
    'primer_ingreso':False #True
}

print(cliente(informacion))




#def function()
#   pass
'''pass is just a placeholder for functionality to be added later'''