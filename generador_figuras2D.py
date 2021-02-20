

def main():
    print("1.- Crear figura")
    print("2.- Listar una clasificación de figuras")
    print("3.- Listar todas las figuras")
    print("4.- Mostrar suma de todas las áreas")
    print("5.- Mostrar la suma de todos los perímetros")
    print("6.- Limpiar lista")
    print("0.- Salir")

# figuras sera un listado de diccionarios
figuras = []
op = int
contador = 0


def menu_figuras():
    global op
    while(op!=0):
        global contador
        contador += 1
        print("Que figura desea anotar?")
        print("1.- Un cuadrado")
        print("2.- Un triangulo")
        print("3.- Un circulo")
        op=int(input("Escriba la opcion: "))
        if op == 1:
            print("Ha seleccionado agregar un Cuadrado")
            lado = float(input("Dame el valor del lado del cuadrado: "))
            crear_cuadrado(lado, contador)
        if op == 2:
            print("Ha seleccionado agregar un triangulo")
            lado_a=float(input("Dame el valor del lado a del triangulo"))
            lado_b=float(input("Dame el valor del lado b del triangulo"))
            lado_c=float(input("Dame el valor del lado c del triangulo"))
            crear_triangulo(lado_a,lado_b,lado_c)

        else:
            print("Escribe un numero del 1 al 3, o 0 para salir")

def crear_triangulo(lado_a,lado_b,lado_c):
    
    altura = float
    
    if(lado_a == lado_b and lado_c == lado_b):
        print("se trata de un triangulo equilatero")
        altura= ((3**1/3) * lado_a)/2

    
    if(lado_a==lado_c and lado_a !=lado_b and lado_c!=lado_b):
        print("se trata de un triangulo isoseles")

    if(lado_a != lado_b and lado_b!=lado_c and lado_a!=lado_c):
        print("Se trata de un triangulo escaleno")




    def area_triangulo(lado_a):
        pass

    def perimetro_triangulo(lado_a,lado_b,lado_c):
        res=lado_a+lado_b+lado_c
        return res
    




def crear_cuadrado(lado,contador):
    def area_cuadrado(lado):
        res=lado*lado
        return res

    def peri_cuaddrado(lado):
        res= lado *4
        return res
        
    global figuras
    area_cuadradosss = area_cuadrado(lado)
    peri_cuadradosss = peri_cuaddrado(lado)
    diccionario_cuadrado = \
        {
            "numFig":contador,
            "tipo":"Cuadrdado",
            "area":area_cuadradosss,
            "perimetro":peri_cuadradosss
        }
    figuras.append(diccionario_cuadrado)
    



while(op!=0):
    main()
    op=int(input("Escriba una opcion: "))
    
    if op == 1:
        menu_figuras()

    


# agregamos diccionario a la lista figura con apped
