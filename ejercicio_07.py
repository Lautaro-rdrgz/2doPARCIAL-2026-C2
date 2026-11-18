
def busqueda_lineal(pokemones, campo, valor):
    resultado = []

    for p in pokemones:
        if campo == "nombre":
            if p.nombre == valor:
                resultado.append(p)
        elif campo == "tipo":
            if p.tipo1 == valor or p.tipo2 == valor:
                resultado.append(p)
        elif campo == "nro":
            if p.id == valor:
                resultado.append(p)
    return resultado        




# TEORIA
# No, porque la búsqueda binaria descarta la mitad de la lista suponiendo que está ordenada por nombre, y si está ordenada por ataque puede descartar justo la mitad donde estaba el que busco.