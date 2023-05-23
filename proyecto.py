import os # se importa la libreria os para manejar achivos

CARPETA = 'contactos/' #  carpeta de contactos 
EXTENSION = '.txt' # Extencion de archivo

# Contactos 
class Contacto:
    def __init__(self,nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria



def app():

    crear_directorio() # revisa si la carpeta existe o no 
    
    mostrar_menu() # se crea menu CRUD 

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una Opcion: \r\n')
        opcion = int(opcion)# convertir un string en numero

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2: 
            editar_contacto()
            preguntar == False        
        elif opcion == 3: 
            print('Ver contacto')
            preguntar == False 
        elif opcion == 4: 
            print('Buscar contacto')
            preguntar == False 
        elif opcion == 5: 
            print('Eliminar contacto')
            preguntar == False  
        else:
            print('Opcion no valida. Intente de nuevo')        
            # no se coloca false para que haga el siclo en caso de que no de la opcion 

def editar_contacto():
    print('Escribe el nombre del contacto a Editar ')
    nombre_anterior = input('Nombre al contacto a Editar: \r\n')

    existe = existe_contacto(nombre_anterior)
    if existe :
        print('puedes editar')
    else:
        print('El contacto no existe')    


def agregar_contacto():
    print('Agrega El Contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')

    # revisar si ya existe el contacto 
    existe = existe_contacto(nombre_anterior)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('ingresa el numero de telefono:\r\n')
            categoria_contacto = input('Ingresa la categoria:\r\n')

            # mostarr mensaje de exito 
            print('\r\n Contacto Creado Correctamente \r\n ')

            # Instaciar la clase 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n')
            archivo.write('Telefono:' + contacto.telefono + '\r\n')
            archivo.write('Categoria:' + contacto.categoria + '\r\n')
    else:
        print("Ese contacto ya existe")

    # reiniciar la app
    app()    



def mostrar_menu(): # se crea el crud 
    print('Selecione la funcion deseada:')
    print('1) Agregar contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists (CARPETA): # validar si esxite o no 
        os.makedirs(CARPETA) # crea la carpeta 
       
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()    