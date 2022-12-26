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

# ? Funcion mostrar menu inicio

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
    for carpeta in ruta_categoria.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categoria.append(carpeta)
        contador += 1
    return lista_categoria

menu = 0

# ! Ver una Receta
if menu == 1:
    # Mostrar Categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # Elegir categoria
    # Mostrar recetas
    # Elegir recetas
    # leer receta
    # Volver al inicio
    pass

# ! Crear una Receta
elif menu == 2:
    # Mostrar Categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # Elegir categoria
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
    # mostrar recetas
    # elegir receta
    # eliminar receta
    # volver a inicio
    pass

# ! Eliminar una Categoria
elif menu == 5:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    # eliminar categoria
    # volver al inicio
    pass

# ! Finalizar el programa
elif menu == 6:
    # finalizar
    pass
