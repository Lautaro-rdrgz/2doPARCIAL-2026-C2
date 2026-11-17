from ejercicio_02 import PokemonNoEncontrado

class EquipoLlenoError(Exception):
    pass


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        

    def esta_vacia(self):
        return self.cabeza == None
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def insertar_al_inicio(self,dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self,dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo 
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo 

    def quitar_primero(self):
        actual = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return actual.dato

    def buscar(self, id):
        actual = self.cabeza

        while actual is not None:
            if id == actual.dato.id:
                return actual.dato
            else:
                actual = actual.siguiente
        
        return None

#  TEORIA
#  La referencia al penultimo esta en el siguiente del nodo anterior a el. los nodos no tienen referencia hacia atras por eso empezamos desde cabeza y sus siguientes