d1 = {'Nombre': 'Jorge', 'Tema': 'Fisica Clásica'}
d2 = {'Nombre': 'Albert', 'Tema': 'Efecto Fotoelectrico'}


d = {
    'Newton': d1,
    'Einstein': d2
}

d['Newton']['Nombre'] = 'Isaac'

d3 = {'Nombre': 'Michael', 'Tema': 'Induccion electromagnetica'}

d['Faraday'] = d3
