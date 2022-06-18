'''
def CDT(usuario,capital,tiempo):
    if tiempo<=2:
        porcentaje_a_perder=0.02
        valor_a_perder=capital*porcentaje_a_perder
        valor_total=capital-valor_a_perder
    else:
        porcentaje_interes=0.03
        valor_intereses=capital*porcentaje_interes*tiempo/12
        valor_total=capital+valor_intereses
    mensaje='Para el usuario '+str(usuario)+' La cantidad de dinero a recibir, según el monto inicial '+str(capital)+' para un tiempo de '+str(tiempo)+' meses es: '+str(valor_total)
    return mensaje

print(CDT('AB1012',1000000,3))
print('\n')
print(CDT('ER3366',650000,2))
'''

def CDT(usuario,capital,tiempo):
    if tiempo<=2:
        porcentaje_a_perder=0.02
        valor_a_perder=capital*porcentaje_a_perder
        valor_total=capital-valor_a_perder
    else:
        porcentaje_interes=0.03
        valor_intereses=capital*porcentaje_interes*tiempo/12
        valor_total=capital+valor_intereses
    mensaje=f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'
    return mensaje

print(CDT('AB1012',1000000,3))
print('\n')
print(CDT('ER3366',650000,2))
