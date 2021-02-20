
import math

# figuras sera un listado de diccionarios
figuras = []
op = int
contador = 0

def main():
    print("----------------------------")
    print("1.- Crear figura")
    print("2.- Listar una clasificación de figuras")
    print("3.- Listar todas las figuras")
    print("4.- Mostrar suma de todas las áreas")
    print("5.- Mostrar la suma de todos los perímetros")
    print("6.- Limpiar lista")
    print("0.- Salir")
    print("----------------------------")

def menu_figuras():
    global op
    while(op!=9):
        global contador
        contador += 1
        print("----------------------------")
        print("Que figura desea anotar?")
        print("1.- Un cuadrado")
        print("2.- Un triangulo")
        print("3.- Un circulo")
        print("9.- Para regresar al menu anterior")
        op=int(input("Escriba la opcion: "))
        print("----------------------------")
        if op == 1:
            print("Ha seleccionado agregar un Cuadrado")
            lado = float(input("Dame el valor del lado del cuadrado: "))
            print("----------------------------")
            crear_cuadrado(lado, contador)
        if op == 2:
            print("Ha seleccionado agregar un triangulo")
            print("Nota:si quieres un isoseles, que \"a\" y \"c\" sean iguales")
            lado_a=float(input("Dame el valor del lado a del triangulo: "))
            lado_b=float(input("Dame el valor del lado b del triangulo: "))
            lado_c=float(input("Dame el valor del lado c del triangulo: "))
            print("----------------------------")
            crear_triangulo(lado_a,lado_b,lado_c)
        if op == 3:
            print("Ha seleccionado agregar un circulo")
            radio = float(input("Dame el valor del radio del circulo: "))
            print("----------------------------")
            crear_circulo(radio)
        else:
            print("Escribe un numero del 1 al 3, o 0 para regresar al menu anterior")

def crear_circulo(radio):
    def area_circulo(radio):
        res = math.pi * (radio ** 2)
        return res
    def perimetro_circulo(radio):
        res = 2 * math.pi * radio
        return res

    area=area_circulo(radio)
    perimetro = perimetro_circulo(radio)

    diccionario_circulo = \
        {
            "id":contador,
            "tipo":"Circulo",
            "area":area,
            "perimetro":perimetro
        }
    figuras.append(diccionario_circulo)

def crear_triangulo(lado_a,lado_b,lado_c):
    
    def area_triangulo(lado,altura):
        res = (lado*altura)/2
        return res 

    def perimetro_triangulo(lado_a,lado_b,lado_c):
        res=lado_a+lado_b+lado_c
        return res

    tipo=""
    area=perimetro=altura=0.0
    
    if(lado_a == lado_b and lado_c == lado_b):
        print("se trata de un triangulo equilatero")
        tipo="Triangulo Equilatero"
        altura= ((3**(1/3)) * lado_a)/2
        area=area_triangulo(lado_a,altura)
        perimetro=perimetro_triangulo(lado_a,lado_b,lado_c)


    
    if(lado_a==lado_c and lado_a !=lado_b and lado_c!=lado_b):
        print("se trata de un triangulo isoseles")
        tipo="Triangulo Isoseles"
        #Raiz de ((a^2 menos b^2))/4
        altura = ((((lado_a**2) - (lado_b**2))/4)**(1/2))
        area = area_triangulo(lado_b,altura)
        perimetro=perimetro_triangulo(lado_a,lado_b,lado_c)


    if(lado_a != lado_b and lado_b!=lado_c and lado_a!=lado_c):
        print("Se trata de un triangulo escaleno")
        tipo="Triangulo Escaleno"
        sp=(lado_a+lado_b+lado_c)/2
        #raiz cuadrada de (sp x ( sp-lado_a)x(sp-lado_b) x (sp - lado_c))
        area = (sp*(sp-lado_a)*(sp-lado_b)*(sp-lado_a))**(1/2)
        perimetro=perimetro_triangulo(lado_a,lado_b,lado_c)


    diccionario_triangulo = \
        {
            "id":contador,
            "tipo":tipo,
            "area":area,
            "perimetro":perimetro
        }
    figuras.append(diccionario_triangulo)

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
            "id":contador,
            "tipo":"Cuadrado",
            "area":area_cuadradosss,
            "perimetro":peri_cuadradosss
        }
    figuras.append(diccionario_cuadrado)

######### Separando las funciones #################

def listar_clasificaciones(tipo):
    for i in figuras:
        
        bandera =0
        if i.get('tipo')==tipo:
            print(i)
            bandera +=1
    if (bandera == 0):
        print(f"No se encontro ningun tipo de: {tipo}")
        
    #Notas para guiarme
    """
    #dicc toma el valor del diccionario
    for dicc in figuras:
        for k,v in dicc.items():
            print(f"Tenemos a {k} junto con {v}")

            print(dicc['tipo':clasificacion])

            if k == clasificacion:
                print(f"la {k} junto con {v}")
                for k,v in dicc():
                    print(f"Tenemos a {k} junto con {v}")
                
                
                for k,v in dicc,items():
                    print(f"Para cada {k} hay una {v}")"""
                #its working
                # print(f"Para cada {k} hay una {v}")
    
def sumador_areas():

    def suma_areas(tipo):
        suma_areas=0.0
        for i in figuras:
            if i.get('tipo')== tipo:
                suma_areas = suma_areas+i.get('area')
                """
                for k,v in i.items:
                    suma_areas=0
                suma_areas=suma_areas=0
                """

        return suma_areas 
            
    # Podria poner un for aqui, pero no parece que valga la pena
    # Forma pitera de hacerlo
    for j in ["Cuadrado","Triangulo Equilatero","Triangulo Isoseles",\
        "Triangulo Escaleno","Circulo"]:
    
        if j == "Cuadrado":
            sumador_de_areas = suma_areas(j)
            print(f"Para {j} su suma de areas es igual a {sumador_de_areas}")

        if j == "Triangulo Equilatero":
            sumador_de_areas = suma_areas(j)
            print(f"Para {j} su suma de areas es igual a {sumador_de_areas}")

        if j == "Triangulo Isoseles":
            sumador_de_areas = suma_areas(j)
            print(f"Para {j} su suma de areas es igual a {sumador_de_areas}")

        if j == "Triangulo Escaleno":
            sumador_de_areas = suma_areas(j)
            print(f"Para {j} su suma de areas es igual a {sumador_de_areas}")

        if j == "Circulo":
            sumador_de_areas = suma_areas(j)
            print(f"Para {j} su suma de areas es igual a {sumador_de_areas}")

    #Forma sencilla y facil de explicar de hacer
    """ 
    tipo="Cuadrado"
    suma_areas_cuadrado=suma_areas(tipo)
    print(f"Para {tipo} su suma de areas es igual a {suma_areas_cuadrado}")

    tipo="Triangulo Equilatero"
    suma_areas_Tri_Equi=suma_areas(tipo)
    print(f"Para {tipo} su suma de areas es igual a {suma_areas_Tri_Equi}")

    tipo="Triangulo Isoseles"
    suma_areas_Tri_Isos=suma_areas(tipo)
    print(f"Para {tipo} su suma de areas es igual a {suma_areas_Tri_Isos}")

    tipo="Triangulo Escaleno"
    suma_areas_Tri_Esca=suma_areas(tipo)
    print(f"Para {tipo} su suma de areas es igual a {suma_areas_Tri_Esca}")

    tipo="Circulo"
    suma_areas_circulo=suma_areas(tipo)
    print(f"Para {tipo} su suma de areas es igual a {suma_areas_circulo}")
    """

def sumador_perimetros():

    def suma_perimetros(tipo):
        suma_perimetros=0.0
        for i in figuras:
            if i.get('tipo')== tipo:
                suma_perimetros = suma_perimetros+i.get('perimetro')

        return suma_perimetros 
            
    # Podria poner un for aqui, pero no parece que valga la pena
    # Forma pitera de hacerlo
    for j in ["Cuadrado","Triangulo Equilatero","Triangulo Isoseles",\
        "Triangulo Escaleno","Circulo"]:
    
        if j == "Cuadrado":
            sumador_de_areas = suma_perimetros(j)
            print(f"Para {j} su suma de perimetros es igual a {sumador_de_areas}")

        if j == "Triangulo Equilatero":
            sumador_de_areas = suma_perimetros(j)
            print(f"Para {j} su suma de perimetros es igual a {sumador_de_areas}")

        if j == "Triangulo Isoseles":
            sumador_de_areas = suma_perimetros(j)
            print(f"Para {j} su suma de perimetros es igual a {sumador_de_areas}")

        if j == "Triangulo Escaleno":
            sumador_de_areas = suma_perimetros(j)
            print(f"Para {j} su suma de perimetros es igual a {sumador_de_areas}")

        if j == "Circulo":
            sumador_de_areas = suma_perimetros(j)
            print(f"Para {j} su suma de perimetros es igual a {sumador_de_areas}")



while(op!=0):
    main()
    op=int(input("Escriba una opcion: "))
    
    if op==0:
        print("See you later")

    if op == 1:
        menu_figuras()
    if op == 2:
        print("----------------------------")
        print("Escriba el nombre de la figura que desea buscar")
        print("Notas: solo responderan a los siguientes nombres: ")
        print("Cuadrado, Triangulo Equilatero, Triangulo Isoseles,Triangulo Escaleno y Circulo")
        print("Si la lista esta vacia se brincara al siguiente bloque")
        print("----------------------------")
        clasificacion = input("Ahora si escriba: ")
        listar_clasificaciones(clasificacion)
        print("----------------------------")
    if op == 3:
        print("Ha seleccionado mostrar toda la lista")
        print("----------------------------")
        print(figuras)
        print("Ahora acomodado:")
        print("[")
        for i in figuras:
            print(i)
        print("]")
        print("----------------------------")

    if op == 4:
        print("----------------------------")
        print("Ha seleccionado sumar las areas por clasificacion")
        sumador_areas()
        print("----------------------------")

    if op == 5:
        print("----------------------------")
        print("Ha seleccionado sumar los perimetros por clasificacion")
        sumador_perimetros()
        print("----------------------------")

    #####
    if op == 6:
        print("----------------------------")
        print("Ha decidido borrar la lista")
        figuras = []
        print("Lista vaciada con exito")
        print("----------------------------")
    

# agregamos diccionario a la lista figura con apped
