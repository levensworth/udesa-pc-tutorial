'''
La facultad necesita crear los usuarios de email para cada empleado 
siguiendo al convención: [inicial del nombre][appelido]@Udesa.edu.ar

por ejemplo:
santiago bassani => sbassani@udea.edu.ar


crear una clase que tenga un método create_email_alias, la cual reciba
un nombre y apellido y retorne el email alias para ese ususario.

'''

class EmailGenerator:
    def __init__(self):
        # esto es atributo del objeto.
        self.domain = 'udesa.edu.ar'

    def create_email_alias(self, name: str, surname: str) -> str:
        return f'{name[0]}{surname}@{self.domain}'



# ejemplo de uso

udesa_email_gen = EmailGenerator()

email_santi = udesa_email_gen.create_email_alias('santiago', 'bassani')

print(email_santi)

