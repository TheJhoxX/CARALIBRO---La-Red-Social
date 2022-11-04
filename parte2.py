''' --Víctor Jorge Sibaja--'''

# CARALIBRO™
import time


# Conjunto basado en tablas de dispersión
class miHashSet:
    def __init__(self):
        self.capacidad = 8
        self.contador = 0  # Equivalente a n de la teoría
        self.t = [None]*8
        self.factorC = float(2)/3

    def hashF(self, clave):
        return clave % self.capacidad

    def addClave(self, clave):

        if float(self.contador)/self.capacidad >= self.factorC:
            self.capacidad <<= 1
            ns = [None]*self.capacidad
            for i in range(self.capacidad >> 1):
                if (self.t[i]):
                    n = self.hashF(self.t[i])
                    while ns[n] is not None:
                        n = (5*n+1) % self.capacidad
                    ns[n] = self.t[i]
            self.t = ns
        h = self.hashF(clave)
        while self.t[h] is not None:
            if self.t[h] == clave:
                return
            h = (5*h + 1) % self.capacidad
        self.t[h] = clave
        self.contador += 1

    # Devuelve true si contiene el elemento y false si no lo contiene
    def contiene(self, clave):

        h = self.hashF(clave)
        while self.t[h] is not None:
            if self.t[h] == clave:
                return True
            h = (5*h + 1) % self.capacidad
        return False


class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.grumos = {}

    # Encuentra la raíz del set x

    def find(self, x):

        # Encuentra la raíz del set
        if (self.parent[x] != x):

            # Si x no es la raíz de si mismo no es la raíz del conjunto
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Une dos sets representados por x e y

    def Union(self, x, y):

        # Encuentra la raíz de los sets x e y
        xset = self.find(x)
        yset = self.find(y)

        # Si tienen la misma raíz ya están en el mismo set
        if xset == yset:
            return

        # Si la altura es distinta pone el de menor altura debajo del de mayor altura
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # Si la altura es la misma pone uno cualquiera debajo del otro y al que está arriba lo incrementa en 1
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

    def contGr(self):
        self.grumos = {}
        for i in range(len(self.parent)):
            x = self.find(self.parent[i])
            if x not in self.grumos:
                self.grumos[x] = 1
            else:
                self.grumos[x] = self.grumos[x] + 1


def obtenerRed(nombreFichero, nombreFicheroAux):
    fich_leer = open(nombreFichero, "r")
    fich_lineas = fich_leer.readlines()

    if nombreFicheroAux == "":
        pass
    else:
        fichaux_leer = open(nombreFicheroAux, "r")
        fichaux_lineas = fichaux_leer.readlines()
        for i in range(len(fichaux_lineas)):
            fich_lineas.append(fichaux_lineas[i])

    # Guardo n y m
    n = int(fich_lineas[0])
    m = int(fich_lineas[1])

    # Obtención lista red
    red = []
    for i in range(2, len(fich_lineas)):
        aux = fich_lineas[i].split()
        tuple(aux)
        red.append(aux)

    primeraEtapa = [n, m, red]
    tuple(primeraEtapa)
    return primeraEtapa


def obtenerUsr(listaConexiones):
    usr = miHashSet()
    for i in range(len(listaConexiones)):
        aux = list(listaConexiones[i])
        for j in range(0, 2):
            usr.addClave(int(aux[j]))

    return usr


def obtenerGrumos(listaConexiones, diccionario):
    grus = DisjSet(len(diccionario))

    for i in range(len(listaConexiones)):
        aux = listaConexiones[i]
        x = diccionario[int(aux[0])]
        y = diccionario[int(aux[1])]
        grus.Union(x, y)

    grus.contGr()  # Obtiene los grumos después de hacer las operaciones de unión
    return grus.grumos


def ordenarGrumos(listaGrumos):
    # Ordenado en función de tamaño de grumo
    listaGrumos.sort(key=lambda x: x[1], reverse=True)
    # Conversión de cada par (raiz,tamaño) a tuplas para no permitir asignación
    for i in range(len(listaGrumos)):
        listaGrumos[i] = tuple(listaGrumos[i])

    return listaGrumos


def conectarGrumos(porcentaje, numUsuarios, listaGrumos):
    conectarGrumos = []
    procesado = 0

    # En caso de que el primer grumo ya supere/iguale el porcentaje
    aux = listaGrumos[0]
    if ((aux[1]/numUsuarios*100) >= porcentaje):
        aux = tuple(aux)
        conectarGrumos.append(aux)

        return conectarGrumos

    for i in range(len(listaGrumos)):
        if ((procesado/n * 100) >= porcentaje):
            break
        aux = listaGrumos[i]
        aux = tuple(aux)
        conectarGrumos.append(aux)
        procesado = procesado + aux[1]

    return conectarGrumos


def nuevasRelaciones(listaConexiones):
    archivo = open("extra.txt", "w")
    for i in range(len(listaConexiones) - 1):
        aux = listaConexiones[i]
        aux2 = listaConexiones[i+1]
        archivo.write(str(aux[0]) + " " + str(aux2[0]) + "\n")

    archivo.close()


print("ANÁLISIS DE CARA LIBRO\n----------------------")
print("Fichero principal: ", end="")
fich_name = str(input())
it_fich = time.time()
print("Fichero de nuevas conexiones (pulse enter si no existe): ", end="")
fichaux_name = str(input())
primeraEtapa = obtenerRed(fich_name, fichaux_name)
ft_fich = time.time()


list(primeraEtapa)
n = primeraEtapa[0]
m = primeraEtapa[1]
red = primeraEtapa[2]
print("Lectura de fichero: " + str(ft_fich - it_fich) + " seg")
print(str(n) + " usuarios " + str(m) + " conexiones")

print("Porcentaje tamaño mayor grumo: ", end="")
porcentaje = int(input())

itPrograma = time.time()
it_usuarios = time.time()
usr = obtenerUsr(red)
ft_usuarios = time.time()
print("Creación lista usuarios: " + str(ft_usuarios - it_usuarios) + " seg")

# Con esto ahora puedo usar los métodos que he creado en mi DisjSet y que el índice no salga del rango
dict = {}
cont = 0
for i in range(len(usr.t)):
    if (usr.t[i] != None):
        dict[usr.t[i]] = cont
        cont += 1

it_grumos = time.time()
grus = obtenerGrumos(red, dict)
ft_grumos = time.time()
print("Creación lista grumos: " + str(ft_grumos - it_grumos) + " seg")

# Grus va a ser una lista de listas que serán un par: (raizGrumo, tamañoGrumo)
grus = list(grus.items())


it_ordenar = time.time()
grus = ordenarGrumos(grus)
conect = conectarGrumos(porcentaje, n, grus)

# Descodificar la raiz del grumo. Hago que pare cuando se haya superado/igualado el porcentaje porque los demás no me hacen falta
for i in range(len(conect)):
    aux = list(conect[i])
    aux[0] = list(dict.keys())[list(dict.values()).index(aux[0])]
    conect[i] = aux

ft_ordenar = time.time()
print("Ordenación y selección de grumos: " +
      str(ft_ordenar - it_ordenar) + " seg")
print("Existen " + str(len(grus)) + " grumos")

if (len(conect) == 1):
    aux = conect[0]
    aux2 = int(aux[1])
    print("El mayor grumo contiene " + str(aux2) +
          " usuarios (" + str((aux2/n)*100) + "%)")
    print("No son necesarias nuevas relaciones de amistad")

else:
    print("Se deben unir los " + str(len(conect)) + " mayores")
    for i in range(0, len(conect)):
        aux = conect[i]
        print("#" + str(i+1) + ": " +
              str(aux[1]) + " usuarios (" + str((aux[1]/n)*100) + "%)")

    print("Nuevas relaciones de amistad (salvadas en extra.txt)")
    for i in range(len(conect) - 1):
        aux = conect[i]
        aux2 = conect[i+1]
        print(str(aux[0]) + " <-> " + str(aux2[0]))

    nuevasRelaciones(conect)

ftPrograma = time.time()
print("Tiempo total: " + str(ftPrograma - itPrograma))