import pandas as pd

# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'
#rutaFileCsv ='text.txt'

def listaPeliculas(rutaFileCsv: str) -> str:
    if (rutaFileCsv.replace('?raw=true','')).endswith('.csv'):
        try:
            df=pd.read_csv(rutaFileCsv, index_col=0)
            df1=pd.pivot_table(df[['Country','Language','Gross Earnings']].dropna(),values='Gross Earnings',index=['Country','Language'])
            return df1.head(10)
        except:
            return 'Error al leer el archivo de datos' 
    else:
        return 'Extensión inválida'

print(listaPeliculas(rutaFileCsv)) 
