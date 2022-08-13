# Forma de encararlo:
## Determinar Estados:
Para poder segmentar una url en los pasos que nos piden debemos tener en cuenta las parte que la conforman.
- Schema
- Authority
- Resource
  
Ahora bien, dado que la separación de schema y authority es compuesta (no es un simple caracter) debemos contemplarlo como un estado o multiples.

## Determinar Cambios de estados:
Afortunadamente, los cambios de estados son sencillos, simplemente sabemos que los schemas terminar con `://` que los recrusos comienzan con `/` por lo que podemos asumir el siguiente diagrama.


![state machine](img/url_state_machine.png)

## Plasmar la idea:
Una vez tenemos nuestro diagrama, tan solo se trata de llevar esta idea a código. siempre considerar que el punto de inicio de una máquina de estados es la lectura **elemnto por elemnto**, mantiendo una referncia al estado actual y determinando el siguiente estado en base al elemnto.