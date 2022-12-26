# Modulos
import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "OneDrive - SENA", "Documentos", "Proyectos Personales", "Proyectos Python", "Administrador de Recetas")

# ? Funcion para contar recetas

def contar_recetas(ruta):
    contador = 0
    # Vamos a buscar todos los archivos que terminen en txt dentro del directorio recetas y en cada carpeta
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# ? Menu inicio

def inicio():
    # Vamos a limpiar la pantalla primero
    system('cls')
    print("*" * 50)
    print('*' * 5 + "Bienvenido al administrador de recetas" + '*' * 5)
    print("*" * 50)
    print(f"\nLas recetas se encuentran en {mi_ruta}")
    # Va a contar la cantidad de recetas que hay en todo el directorio
    print(f"Total recetas: {contar_recetas(mi_ruta)}" )
    eleccion_menu = 'x'
    # Mientras la eleccion no sea numerica o que el numero no este en el rango indicado entonces:
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion:")
        print('''
            [1] - Leer receta
            [2] - Crear nueva receta
            [3] - Crear categoria nueva
            [4] - Eliminar Receta
            [5] - Eliminar categoria
            [6] - Salir del programa
            ''')
        eleccion_menu = input()
    return (eleccion_menu)

# ? Funcion mostrar categorias

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categoria = Path(ruta)
    lista_categoria = []
    contador = 1
    # Recorremos el directorio, con el metodo iterdir recorremos en carpetas
    for carpeta in ruta_categoria.iterdir():
        # convertimos a string el nombre de la categoria
        carpeta_str = str(carpeta.name)
        # Mostramos la categoria con el nombre
        print(f"[{contador}] - {carpeta_str}")
        # Agregamos el directorio a un arreglo
        lista_categoria.append(carpeta)
        contador += 1
    # Retornamos la lista
    return lista_categoria

# ? Funcion elegir categoria

def elegir_categoria(lista):
    # Definimos una condicion dentro de un bucle
    eleccion_correcta = 'x'
    # Mientras no sea un numero o el numero no este dentro del rango ( se usa + 1 porque asi lo ve el usuario)
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")
    # Asi lo ve el usuario
    return lista[int(eleccion_correcta) - 1]

# ? Funcion mostrar recetas

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

# ? Funcion elegir receta

def elegir_receta(lista):
    elegir = 'x'
    while not elegir.isnumeric() or int(elegir) not in range(1, len(lista) + 1):
        elegir = input("Escoge una receta: ")
    return lista[int(elegir) - 1]



menu = 0

# ! Ver una Receta
if menu == 1:
    # Mostrar Categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # Elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # Mostrar recetas
    mis_recetas = mostrar_recetas(mi_categoria)
    # Elegir recetas
    mi_receta = elegir_receta(mis_recetas)
    # leer receta
    # Volver al inicio
    pass

# ! Crear una Receta
elif menu == 2:
    # Mostrar Categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # Elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # Crear Receta
    # Volver Inicio
    pass

# ! Crear una Categoria Nueva
elif menu == 3:
    # Crear categoria
    # volver inicio
    pass

# ! Eliminar una receta
elif menu == 4:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # mostrar recetas
    mis_recetas = mostrar_recetas(mi_categoria)
    # elegir receta
    mi_receta = elegir_receta(mis_recetas)
    # eliminar receta
    # volver a inicio
    pass

# ! Eliminar una Categoria
elif menu == 5:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # eliminar categoria
    # volver al inicio
    pass

# ! Finalizar el programa
elif menu == 6:
    # finalizar
    pass
