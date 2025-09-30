class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.categorias = ["Ciencia", "Literatura", "Historia"]

    def registrar_libro(self, titulo, categoria):
        
        if categoria in self.categorias:
            self.libros.append((titulo, categoria))
            
            print("+----------------------------------------+")
            print(f"| Libro '{titulo}' registrado en '{categoria}'.")
            print("+----------------------------------------+")

        else:

            print("+----------------------------------------+")
            print("| Categoría no válida.")

    def registrar_usuario(self, nombre):
        self.usuarios.append(nombre)
            
        print("+----------------------------------------+")
        print(f"| Usuario '{nombre}' registrado.")
        print("+----------------------------------------+")
        
# Programa Principal
biblio = Biblioteca()

while True:
    print("+========================================+")
    print("| Bienvenido a la Biblioteca             |")
    print("+========================================+")
    print("| Seleccione una opción:                 |")
    print("| 1. Registrar libro                     |")
    print("| 2. Registrar usuario                   |")
    print("| 3. Ver libros registrados              |")
    print("| 0. Salir                               |")
    print("+========================================+")
    
    opcion = input("| Ingrese el número de la opción: ")

    if (opcion == "1"):
        titulo = input("| Ingrese el título del libro: ")
        categoria = input("| Ingrese la categoría (Ciencia, Literatura, Historia): ")
        biblio.registrar_libro(titulo, categoria)

    elif (opcion == "2"):
        nombre = input("| Ingrese el nombre del usuario: ")
        biblio.registrar_usuario(nombre)

    elif (opcion == "3"):

        print("\n| Libros registrados:")
        if len(biblio.libros) == 0:
            print("| No hay libros.")
        else:
            for libro in biblio.libros:
                print("| - ",libro[0],"(",libro[1],")")

    elif (opcion == "0"):
        print("----------------------------------------")
        print("| Saliendo del programa")
        print("----------------------------------------")
        break

    else: 
        print("----------------------------------------")
        print("| Opcion Invalida")
        print("----------------------------------------")
