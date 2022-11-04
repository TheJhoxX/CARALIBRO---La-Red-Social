# CARALIBRO ™ - LA RED SOCIAL
**Práctica realizada para la asignatura de Estructura de Datos y Algoritmos para la Universidad de Valladolid en el curso 2021-2022.**

# ENUNCIADO
El planteamiento y objetivo de ambas partes es el mismo: se plantea una red social organizada a base de "conexiones de amistad" bidireccionales (si x es amigo de y entonces y es amigo de x). Cuando un usuario publica algo, esto es enviado a sus amigos y cada uno puede decidir si reenviarlo a su vez a sus amigos y así sucesivamente.
Se denomina grumo a un conjunto de usuarios que son mutuamente accesibles en la red. En el siguiente gráfico se muestra una red de 15 usuarios donde existen 4 grumos (los números son los identificadores de los usuarios y cada línea indica una conexión de amistad)
![image](https://user-images.githubusercontent.com/87580006/199970997-97635912-51ff-4051-8f2b-12fe0247a02f.png)

Los usuarios que no pertenezcan al grumo no recibirán lo enviado pero los que sí pertenezcan lo recibirán casi seguro (porque están relacionado), por ello el objetivo es que la mayoría de los usuarios pertenezcan a un mismo grumo

Si tomamos como ejemplo el gráfico de la página anterior, podemos apreciar que existen cuatro grumos de tamaños 6, 4, 3 y 2 usuarios, en orden descendente. Si, por ejemplo, el objetivo fuera conseguir que en un único grumo estuviesen más del 85% de los usuarios, podemos ver que uniendo los 3 grumos más grandes tendríamos el (6+4+3)/15 = 87% de los usuarios en él. Una forma de conseguirlo sería pagar a los usuarios 32 y 43 para que se hicieran amigos y hacer lo
mismo con los usuarios 3 y 18:
![image](https://user-images.githubusercontent.com/87580006/199971322-b1f94683-768e-4269-ac4c-e931d302cd51.png)

Por supuesto existen otras muchas posibilidades, para unir dos grumos basta con se hagan amigos cualquier usuario del primero con cualquier usuario del segundo. Es importante que se pague a la menor cantidad posible de personas, por eso se deben unir los grumos mayores, y es fácil observar
que para unir n grumos basta con crear n-1 nuevas relaciones de amistad.

El objetivo es el crear una aplicación a la que se proporcionará el estado actual de la red (el listado con las conexiones de amistad existentes) y el porcentaje mínimo de usarios que queremos que estén en el grumo de mayor tamaño. La aplicación analizará la red detectando los grumos existentes
y su tamaño, y si detecta que el grumo de mayor tamaño no contiene un determinado porcentaje mínimo de usuarios, entonces presentará una propuesta de relaciones de amistad “por dinero” con
las que se podría conseguir ese objetivo

## DESCRIPCIÓN TÉCNICA
La información sobre la red se proporciona como un fichero de texto donde la primera línea contiene un entero que indica el número de usuarios (n), la segunda línea un entero que indica el número de conexiones de amistad (m) y despues le siguen m líneas cada una de ellas conteniendo dos enteros separados por un espacio en blanco

## SIN OPTIMIZAR (PARTE 1)
En esta parte el algoritmo es prefijado
![image](https://user-images.githubusercontent.com/87580006/199971956-4c244de4-a9b9-400a-baf5-9ff81d734df7.png)

## OPTIMIZADA (PARTE 2)
En esta parte se permite usar un algoritmo distinto y programar estructuras de datos para mejorar la eficiencia de la parte 1

## SALIDA ESPERADA
### SIN USO DE FICHERO EXTRA
![image](https://user-images.githubusercontent.com/87580006/199972426-501213e7-60d4-4b77-b011-344ab5479bcd.png)
### CON USO DE FICHERO EXTRA
![image](https://user-images.githubusercontent.com/87580006/199972502-37a0f4d0-adca-43c8-9cda-eccfd20ceb75.png)

## MI DESARROLLO PARA LA PARTE 2
En mi caso programe una clase: miHashSet con las operaciones necesarias para poder resolver lo que necesitara, llegando a tardar la ejecución de todo el programa 14.32 segundos para una entrada de 20 millones de usuarios (para la cual anteriormente el programa hubiera tardado un tiempo mucho mayor)



