class Tipo:
    def __init__(self,nombre,id_tipo=0):
        self.__id_tipo = id_tipo
        self.__nombre = nombre



    def get_id_tipo(self):
        return self.__id_tipo
    def set_id_tipo(self,id_tipo):
        self.__id_tipo = id_tipo
    


    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    
    def __str__(self):
        txt = f"El id es {self.__id_tipo}"
        txt += f"\nEl nombre es {self.__nombre}"
        return txt