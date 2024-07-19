class Autor:
    def __init__(self,nombre:str,apellido:str,edad:str,id_autor=0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__id_autor = id_autor

    def get_id_autor(self):
        return self.__id_autor
    def set_id_autor(self,id_autor):
        self.__id_autor = id_autor
    
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    
    def get_edad(self):
        return self.__edad
    def set_edad(self,edad):
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre


    def __str__(self):
        txt = f"El nombre es {self.__nombre}"
        txt = f"\nEl apellido es {self.__apellido}"
        txt += f"\nLa edad es {self.__edad}"
        txt += f"\nEl id es {self.__id_autor}"
        return txt