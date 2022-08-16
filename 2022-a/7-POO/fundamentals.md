# Python y objetos:
En este documento intentaremos entender como logra el lenguaje de programación Python
implementar los conceptos del paradigma de objetos.

Primero debemos entender que todo elemento con el que interactuaron en Python es un `objeto`.
Desde los `int` hasta los `bool` y todo lo que hay en el medio, siempre fueron objetos implementados
por el lenguaje.

## Como implementar un objeto.
Para implementar un nuevo objeto propio, comenzamos por la definción de una clase.
Esto se logra con el indicador `class`. Recordar que los nombres de las clases Comienzan 
con mayúscula y siguen el formato camel case. 

```
class MyClass:
    ...
```
Luego, cuando queremos generar una "instancia" de dicha clase, debemos invocarla tal como si fuera 
una función.
```
my_class_instance = MyClass()
```

Para entender lo que ocurre debemos pensar en la **definición** de la clase (donde utilizamos `class`) 
como la definción de un plano para una edificación. Este plano no es más que un conjunto de directivas
para que otra persona logre obtener el edificio deseado. 
En cambio, cuando **instanciamos** (llamamos a la clase) lo que está pasando es que le indicamos a Pythonq
que deseamos una nueva instancia de un objeto que cumpla con las características que dispone es clase. El
lenguaje, simplemente está contruyendo un nuevo edificio basado en el plano que le dijimos que use. Ahora, 
como dos edificos construídos del mismo plano, dos instancias de la misma clase no son el mismo objeto.

## Estados y comportamientos:
La principal potencia de los objetos proviene de que los mismo contengan **estados** y **comportamientos**.
En criollo, esto quiere decir que los objetos deben tener variables y funciones porpias. Ahora bien, como 
podemos asignarle estas al objeto? Sencillamente lo hacemos en la definición del objeto.

Para crear un nuevo método (la forma de refernos a funciones de una clase). Simplemente creamos una función
pero lo hacemos dentro del `scope` de la clase y debemos agregar un argumento por default a todos los métodos.

```
class MyClass:
    def my_method(self):
        ...

my_instnace = MyClass()
my_instance.my_method() # no requiere ningun argumento, self es autoasignado por Python.
```
En este caso `self` es un argumento que tenemos por default en todos los métodos de la clase y es auto asignado por 
el propio lenguaje (es decir que a la hora de invocarlo, no debemos asignarlo)

Este argumetno es una referencia a la propia instancia, es una forma que tenemos dentro del método para acceder
a otros elementos del objeto como lo son variables y otras funciones.


veamos como puede ser utilizado:
```
class MyClass:
    def method_1(self):
        self.attribute_1 = 10

    def method_2(self):
        return self.attribute_1 + 20
```

En este caso, cuando alguien llame al método `method_1`, lo que hace es crear un estado (o modificarlo en caso que ya existiera) del objeto
llamado `attribute_1` asignandole un valor. Piensen en esto como modificar una clave de un diccionario, cuando el valor existe lo reemplazamos 
y si no existía lo creamos. Luego, en el `method_2` hacemos uso de dicho estado para justamente devolver un valor, notese que si el usuario no invoca al `method_1` entonces `attribute_1` no existe, por ende si no se invoca a `method_1` antes de llamar a `method_2` el interprete
lanza un error.


## Constructores:
Cuando creamos una instancia de una clase  (llamamos al nombre de la clase como: `MyClass()`) ocurre una serie de pasos internamente, los 
cuales intentaremos entender ahora mismo.

Si seguimos con el ejemplo anterior, veamos que ocurre cuando queremos generar una instancia de la clase.

```
instancia = MyClass()
```
Al invocar a la clase, lo que ocurre es la siguiente secuencia de pasos:
- Python entiende que queremos crear un nuevo objeto con la definición de la clase `MyClass`
- El interprete busca un metodo llamado `__init__` dentro de la clase.
- Al no encontrarlo, busca en su padre. Como no especificamos ningún padre entonces tiene el ancenstro universal llamado `object`
- encuentra el método `__init__` dentro de `object` y lo invoca.
- Este método devuelve por defecto (sin tener que poner el `return`) una nueva instancia de dicho objeto.

En esta mirada, nos olvidamos de ciertos detalles muy específicos de implementación que no vienen al caso y nos concentramos en entender
los puntos principales de la secuencia.

Los constructores, son siempre el método llamao `__init__`, si la clase no lo define se utiliza por default el de su padre o primer ancestro
que lo defina.
Este método solo se invoca una vez, a la hora de crear una nueva instancia del objeto. Los utilizamos como punto de partida para inicializar 
variables o hacer ciertos comportamientos específicos del inicio de un obeto.
