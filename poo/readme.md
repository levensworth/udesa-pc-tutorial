# Programación Orientada a Objetos:
Esta es una pequeña introducción al paradigma de programación orientado a objetos.


## Definiciones:
Veamos un poco de terminología básica.

### Objeto:
Es la unidad básica del paradigma. Se define como una estructura porpia que debe cumplir con
lo siguiente:
- Debe poseer un estado interno
- Debe poseer un comportamiento. Responder ante mensajes del exterior.
- Debe tener una identidad. Una forma de unicidad que identifique a cada objetos único.

En Python esto se logra utilizando el tipo `class`. 

### Fundamentos del paradigma:
El paradigma posee 4 pialres fundamentales que veremos a continuación, puede entontrar implementaciones
bajo la carpeta `fundamentals-implemented`.

**Abstracciœn**
La implementación de código no debe ser accesible por quien no corresponde. Es decir, 
si un método de una clase solo sirve para si misma y no debe ser utilizada por otros objetos.
Cuando llamamos a un método, no nos itneresa su implementación sino lo que esperamos del mismo.

**Encapsulamiento**
Un objeto debe contener toda la información que necesita para operar, es decir todo el estado
del propio objeto debe estar auto contenido en el mismo.

**Polimorfismo**
Refiere a la habilidad de un objeto de comporarse de diferentes formas en diferenes contextos.
Si un método actua de diferente forma en base al estado interno del objeto o del mensaje es un ejemplo
de polimorfismo.
Ejemplo: Un objeto `switch` que represente el interruptor de luz. El mismo tiene un método que sea `press`
que repsenta la acción de tocar el interruptor. Depende del estado del interruptor, este método puede prender
o apagar la luz.

**Inheritance**
Refiere a la habilidad de los objetos de heredar características de otros objetos ancestros. Generalmente,
utilizamos esta habilidad para definir comportamientos comunes entre varios objetos.


## Ejercitación:
Se recomienda seguir la guía de ejercicios dados en clase, una vez terminado dicha guía puede optar por un
ejercicio más intensivo que se encuentra en la carpeta `todo-list` dicho encunciado representa un problema
concreto y contiene una guía de resolución para ayudarlos a pensar la solución en este paradigma.


## Fundamentos:
Podemos encontrar los fundamentos del paradigma en python dentro del archivo `fundamentals.md`

