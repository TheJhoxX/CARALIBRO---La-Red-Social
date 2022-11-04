# --Víctor Jorge Sibaja--

# CARALIBRO™
import time  # Para poder hacer las mediciones de tiempo


# Función que retorna una tupla que contiene en el elemento [0] el número de usuarios, en el elemento [1] el número de conexiones y en el elemento [2] la lista red
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

# Función que retorna cada grumo


def uber_amigos(usuario_inicial, red, grumo):
    if usuario_inicial not in grumo:  # [usuario_inicial]
        grumo.append(usuario_inicial)
    else:
        pass
    for i in range(len(red)):
        aux = list(red[i])
        # Si el usuario inicial aparece en la conexión se añade el otro usuario al grumo por ser conexión suya
        if usuario_inicial in aux:
            for j in range(len(aux)):
                if (aux[j] not in grumo) & (aux[j] != usuario_inicial):
                    grumo.append(aux[j])
                    uber_amigos(aux[j], red, grumo)
        else:
            pass

    return grumo


# Función que retorna la lista usr
def obtenerUsrList(redList):
    usr = []
    for i in range(len(redList)):
        aux = list(redList[i])
        for j in range(0, 2):
            if (aux[j] not in usr):
                usr.append(aux[j])

    return usr


# Función que retorna la lista grus
def obtenerGrusList(usrList):
    grus = []
    asig = []
    grumo = []
    usr = usrList
    for i in range(len(usr)):
        if usr[i] not in asig:
            current_usr = usr[i]
            grumo = []
            grumo = uber_amigos(current_usr, red, grumo)
            for j in range(len(grumo)):
                aux = grumo[j]
                if aux not in asig:
                    asig.append(aux)
            grus.append(grumo)

    return grus


# Función que retorna una lista de los grumos que deben conectarse y los usuarios que deben conectarse de dichos grumos en otra lista
def obtenerGrumosConectar(grusList, porcentajeMax):
    procesados = 0
    grus = grusList
    # Ordeno grus del grumo de mayor tamaño al grumo de menor tamaño
    grus.sort(key=len, reverse=True)
    porcentaje = porcentajeMax

    gr_conectar = []  # Lista que contiene que grumos deben conectarse
    for i in range(len(grus)):
        if (procesados / n) * 100 >= porcentaje:
            break
        aux = grus[i]
        gr_conectar.append(aux)
        for j in range(len(aux)):
            if (procesados / n) * 100 >= porcentaje:
                break
            else:
                procesados = procesados + 1

    conexiones = [gr_conectar, obtenerUsuariosConectar(gr_conectar)]
    tuple(conexiones)
    return conexiones


# Función que retorna una lista que contiene las conexiones entre usuarios que se tienen que realizar
def obtenerUsuariosConectar(grConectarList):
    gr_conectar = grConectarList
    # Lista que deberá contener cada una de las conexiones que deben producirse entre usuarios
    usr_conectar = []
    for i in range(len(gr_conectar)):
        if i > len(gr_conectar) - 2:
            break
        else:
            aux = gr_conectar[i]
            aux2 = gr_conectar[i + 1]
            usr_conectar.append(aux[0] + " " + aux2[1])

    return usr_conectar


# Guardado de nuevas relaciones en el fichero extra.txt
def nuevasRelaciones(conexionesUsuarios):
    archivo = open("extra.txt", "w")
    for i in range(len(conexionesUsuarios)):
        archivo.write(str(conexionesUsuarios[i]) + "\n")
    archivo.close()


print("ANÁLISIS DE CARA LIBRO\n----------------------")
# Introducir nombre del fichero y guardar cada línea como un elemento de una lista
print("Fichero principal: ", end="")
fich_name = str(input())
it_fich = time.time()

print("Fihero de nuevas conexiones (pulse enter si no existe): ", end="")
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

# Obtención lista usr
it_usuarios = time.time()
usr = obtenerUsrList(red)
ft_usuarios = time.time()
print("Creación lista usuarios: " + str(ft_usuarios - it_usuarios) + " seg")

# Obtención asig y grus
it_grumos = time.time()
grus = obtenerGrusList(usr)
ft_grumos = time.time()
print("Creación lista grumos: " + str(ft_grumos - it_grumos) + " seg")

it_ordenar = time.time()
# Conexiones es una tupla que devuelve la función obtenerGrumosConectar, el elemento [0] de listar la tupla es los grumos que se deben conectar y el elemento [1]
# es una lista con las conexiones nuevas que deben formarse
conexiones = obtenerGrumosConectar(grus, porcentaje)
list(conexiones)
gr_conectar = conexiones[0]
usr_conectar = conexiones[1]

ft_ordenar = time.time()
print("Ordenación y selección de grumos: " +
      str(ft_ordenar - it_ordenar) + " seg")

print("Existen " + str(len(grus)) + " grumos")
if len(gr_conectar) > 1:
    print("Se deben unir los " + str(len(gr_conectar)) + " mayores")
else:
    print(
        "El mayor grumo contiene: "
        + str(len(gr_conectar[0]))
        + " usuarios ("
        + str((len(gr_conectar[0]) / n) * 100)
        + "%)"
    )

if len(gr_conectar) > 1:
    for i in range(len(gr_conectar)):
        aux = grus[i]
        print(
            "#"
            + str(i + 1)
            + ": "
            + str(len(aux))
            + " usuarios ("
            + str((len(aux) / n) * 100)
            + "%)"
        )
else:
    pass

if len(gr_conectar) > 1:
    print("Nuevas relaciones de amistad (salvadas en extra.txt)")
    for i in range(len(usr_conectar)):
        print(str(usr_conectar[i]).replace(" ", " <-> "))
else:
    print("No son necesarias nuevas relaciones de amistad")

# Genero el archivo con conexiones extra
nuevasRelaciones(usr_conectar)
