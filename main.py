import csv

f = 'cvs/ciencias1_1.csv'
def cargaMedallero(fileName: str) -> list[dict]:
    df = []
    with open(f, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            df.append({            
                'apellidos': tuple(row[0].split(' ')),
                'nombres': tuple(row[1].split(' ')),
                'departamento': row[2],
                'institucion': row[3]
            })
    return df

def getInstituciones(medallero: list[dict]) -> list[str]:
    instituciones = []
    for medalla in medallero:
        institucion = medalla['institucion']
        if institucion not in instituciones:
            instituciones.append(institucion)
    return tuple(set(instituciones))

def getMedallas(medallero: list[dict]) -> dict:
    INSTITUCIONES = getInstituciones(medallero=medallero)
    medallas = dict(zip(INSTITUCIONES, len(INSTITUCIONES)*[0]))
    for medalla in medallero:
        institucion = medalla['institucion']
        i = medallas[institucion]
        medallas[institucion] = i + 1
    return(medallas)

df = cargaMedallero(f)
MEDALLAS = getMedallas(df)
for i in getInstituciones(df):
    print(i, MEDALLAS[i])