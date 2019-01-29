def func(x, y):
    """Documentación de la función. Hace x * y - 5"""
    return x * y - 5


# Esta función no es importada, usando los _ al principio
def __func_oculta(a):
    print(a)


def hola_mundo(name):
    """Hola mundo!"""
    
    # Pero puedo usarla en las funciones importables
    __func_oculta("Hola " + name)