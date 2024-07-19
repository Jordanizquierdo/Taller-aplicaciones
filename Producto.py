class Producto:
    def __init__(self,nombre:str,descripcion:str,tipo_id_tipo:str,cantidad:int,id_producto=0):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__tipo_id_tipo = tipo_id_tipo
        self.__cantidad = cantidad
        self.__id_producto = id_producto

    def get_id_producto(self):
        return self.__id_producto
    def set_id_producto(self,id_producto):
        self.__id_producto = id_producto
    
    def get_tipo_id_tipo(self):
        return self.__tipo_id_tipo
    def set_tipo_id_tipo(self,tipo_id_tipo):
        self.__tipo_id_tipo = tipo_id_tipo
    
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre


    def __str__(self):
        txt = f"El nombre es {self.__nombre}"
        txt += f"\nEl id de tipo es {self.__tipo_id_tipo}"
        txt += f"\nLa descripcion es {self.__descripcion}"
        txt += f"\nLa cantidad es {self.__cantidad}"
        txt += f"\nEl id es {self.__id_producto}"
        return txt