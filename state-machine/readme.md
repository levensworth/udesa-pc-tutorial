# Consigna:

1. 
    Escribir una función `parse_date` que reciba por argumento un string. En caso que el string conforme el 
    formato: `dd[separador]mm` donde `[separador]` es uno de los siguientes simbolos (`:`, `/`, `-`) mienstras que `d` y `m` deben ser enteros. Entonces devolveremos una tupla con el valor numérico, caso contrario `None`
    de forma (`dd`, `mm`). 
    Ejemplos de entrada:
    - `"1234:66"` -> retornaremos `(1234, 66)`
    - `"23/8"` -> retornaremos `(23, 8)`
    - `"/0"` -> retornaremos `None`

2. Una URL (Uniform Resource Locator), es la forma estandar que tenemos de acceder a recursos 
   utilizando un navegador. Dichas direcciones, tienen una estructura que las hace fáciles de 
   entender que por simplificación tomaremos de la siguiente forma:
   RUL: `SCHEMA|PROTOCOL`://`AUTHORITY|DOMAIN`/`RESOURCE`
   Se pide escribir una función que dado un stirng que represente una URL, escriba por pantalla
   el siguinete mensaje:
   > disect_url('http://google.com/')
   ```
   URL: http://google.com/
   SCHEMA: http
   AUTHORIY: google.com
   RESOURCE: /
   ```
