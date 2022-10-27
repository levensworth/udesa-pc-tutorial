'''
La universidad ahora tiene un nuevo dominio (a parte de udesa.edu.ar )
el cual utiliza para alumnos de postgrado (postgrado.udea.edu.ar)

Dado eso ahora debemos modificar nuestra solución anterior para añadir 
un nuevo método create_ms_email_alias el cual reciba los mismos parámetros 
que nuestra antigua función y retorne el email con el nuevo domino.
'''

# solucion previa
class EmailGenerator:
    def __init__(self):
        # esto es atributo del objeto.
        self.domain = 'udesa.edu.ar'

    def create_email_alias(self, name: str, surname: str) -> str:
        return f'{name[0]}{surname}@{self.domain}'

# nueva
class GenericEmailGenerator:
    def __init__(self, domain: str):
        self.domain = domain
        
    def create_email_alias(self, name: str, surname: str) -> str:
        return f'{name[0]}{surname}@{self.domain}'


class UdesaEmailGenerator:
    def __init__(self):
        self.__basic_gen = GenericEmailGenerator('udesa.edu.ar')
        self.__ms_gen = GenericEmailGenerator('postgrado.udesa.edu.ar')

    def create_email_alias(self, name: str, surname: str) -> str:
        return self.__basic_gen.create_email_alias(name, surname)

    def create_ms_email_alias(self, name: str, surname: str) -> str:
        return self.__ms_gen.create_email_alias(name, surname)

    

email_gen = UdesaEmailGenerator()

bachelor = email_gen.create_email_alias('santiago', 'bassani')

master = email_gen.create_ms_email_alias('santiago', 'bassani')

print(bachelor)
print(master)

'''
Nuestra nueva solución es un poco más larga, pero esto se debe a que la hicimos mucho más genérica. Ahora 
tenemos una GenericEmailGenerator class que nos permite crear emails con el mismo patrón para cualquier tipo
organización.
'''