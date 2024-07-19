class Bodega:
    def __init__(self,codigo:str,ubicacion:str,id_bodega=0):
        self.__id_bodega = id_bodega
        self.__ubicacion = ubicacion
        self.__codigo = codigo

    def get_id_bodega(self):
        return self.__id_bodega
    def set_id_ubicacion(self,id_bodega):
        self.__id_bodega = id_bodega
    
    def get_ubicacion(self):
        return self.__ubicacion
    def set_ubicacion(self,ubicacion):
        self.__ubicacion = ubicacion

    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,codigo):
        self.__codigo = codigo

    
    def __str__(self):
        txt = f"El id es {self.__id_bodega}"
        txt += f"\nEL codigo es {self.__codigo}"
        txt += f"\nLa ubicacion es {self.__ubicacion}"
        return txt