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
    return int(eleccion_menu)

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

# ? Funcion leer una receta

def leer_receta(receta):
    print(Path.read_text(receta))

# ? Funcion crear una Receta

def crear_receta(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de tu receta: ")
        # Escribe el nombre con la extencion del archivo
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        # Agrega el contenido que va a tener la receta
        contenido_receta = input()
        # Se genera la ruta nueva donde se crea
        ruta_nueva = Path(ruta, nombre_receta)
        
        # Si el archivo o ruta no existe con ese nombre, entonces
        if not os.path.exists(ruta_nueva):
            # Creamos o escribimos la receta nueva en la direccion indicada, incluyendo el contenido
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")
    
# ? Funcion crear una categoria

def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print("Escribe el nombre de tu categoria: ")
        # Escribe el nombre con la extencion del archivo
        nombre_categoria = input()
        # Se genera la ruta nueva donde se crea
        ruta_nueva = Path(ruta, nombre_categoria)
        
        # Si el archivo o ruta no existe con ese nombre, entonces
        if not os.path.exists(ruta_nueva):
            # Creamos el directorio o carpeta nueva
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

# ? Funcion eliminar receta

def eliminar_receta(receta):
    # Metodo para eliminar un arhivo con path
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

# ? Funcion eliminar categoria

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

# ? Funcion volver a inicio

def volver_inicio():
    eleccion_regresar = "x"
    
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresione v para volver al menu: ")

finalizar_programa = False
while not finalizar_programa:
    menu = inicio()
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
        leer_receta(mi_receta)
        # Volver al inicio
        volver_inicio()
        pass

# ! Crear una Receta
    elif menu == 2:
        # Mostrar Categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # Crear Receta
        crear_receta(mi_categoria)
        # Volver Inicio
        volver_inicio()
        pass

# ! Crear una Categoria Nueva
    elif menu == 3:
        # Crear categoria
        crear_categoria(mi_ruta)
        # volver inicio
        volver_inicio()
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
        eliminar_receta(mi_receta)
        # volver a inicio
        volver_inicio()
        pass

# ! Eliminar una Categoria
    elif menu == 5:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar categoria
        eliminar_categoria(mi_categoria)
        # volver al inicio
        volver_inicio()
        pass

# ! Finalizar el programa
    elif menu == 6:
        finalizar_programa = True
        # finalizar
        pass


