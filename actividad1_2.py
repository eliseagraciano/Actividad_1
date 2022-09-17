import os

class Paquete:
    Id=0
    Origen=0
    Destino=0
    Peso=0
    def __init__(self,id,origen,destino,peso):
        self.Id=id
        self.Origen=origen
        self.Destino=destino
        self.Peso=peso

    def getter_Id(self):
        return self.Id

    def getter_Origen(self):
        return self.Origen

    def getter_Destino(self):
        return self.Destino
    
    def getter_Peso(self):
        return self.Peso
    
class nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class Paqueteria: 
    def __init__(self):
        self.head = None
    
    def Insertar(self, data):
        self.head = nodo(data=data, next=self.head)  

    # Método para eleminar nodos
    def Eliminar(self):
        if self.head is None:
            print("No hay paquetes disponibles....")
        else:
            curr = self.head
            self.head = curr.next

    # Método para imprimir la lista de nodos
    def Mostrar( self ):
        node = self.head
        if self.head is None:
            print("No hay paquetes disponibles....")
        else:
            while node != None:
                print("Paquete: "+str(node.data.getter_Id()), end ="\n")
                print("Origen: "+str(node.data.getter_Origen()), end ="\n")
                print("Destino: "+str(node.data.getter_Destino()), end ="\n")
                print("Peso: "+str(node.data.getter_Peso()), end ="\n\n")
                node = node.next
    
    def guardar(self):
        Archivo_deco = open("Archivo_paqueteria.txt", "a")  # escritura
        node = self.head
        while node != None:
            Archivo_deco.write(str(node.data.getter_Id())+",")
            Archivo_deco.write(node.data.getter_Origen()+",")
            Archivo_deco.write(node.data.getter_Destino()+",")
            Archivo_deco.write(str(node.data.getter_Peso())+"\n")
            node = node.next
        print("Guardado concluido\n")
        Archivo_deco.close()

    def recuperar(self,New_paqueteria):
        Archivo = open("Archivo_paqueteria.txt","r") #Modo lectura 
        node = self.head
        for linea in Archivo.readlines():
            lista = linea.split(',')
            id, origen, destino, peso = lista[0], lista[1], lista[2], lista[3]
            new_paquete=Paquete(id,origen,destino,peso)
            New_paqueteria.Insertar(new_paquete)
        print("Recuperación concluida\n")
        Archivo.close()
        

def borrar():
    os.system("cls")    

def pedir_datos():
    id=int(input("Ingrese el id del paquete..."))
    origen=str(input("Ingrese el origen del paquete..."))
    destino=str(input("Ingrese el destino del paquete..."))
    peso=float(input("Ingrese el peso del paquete en kilos..."))
    new_paquete=Paquete(id,origen,destino,peso)
    return new_paquete


def Menu():
    New_paqueteria=Paqueteria()
    
    while True:
        print("Paqueteria...\n")
        print("1)Agregar paquete...\n")
        print("2)Eliminar paquete...\n")
        print("3)Mostrar paquetes...\n")
        print("4)Guardar paquetes...\n")
        print("5)Recuperar paquetes...\n")
        opcion=int(input("Ingrese una opcion...."))
        if opcion == 1:
            borrar()
            auxiliar_almacenapaquete=pedir_datos()
            New_paqueteria.Insertar(auxiliar_almacenapaquete)
            
        elif opcion ==2:
            borrar()
            New_paqueteria.Eliminar()
            
        elif opcion ==3:
            borrar()
            New_paqueteria.Mostrar()
            
        elif opcion ==4:
            borrar()
            New_paqueteria.guardar()
            
        elif opcion ==5:
            borrar()
            New_paqueteria.recuperar(New_paqueteria)
            
        else:
            print("Gracias por su visita...")
            exit()
Menu();