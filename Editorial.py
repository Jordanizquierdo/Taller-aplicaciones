class Editorial:
    def __init__(self,nombre,id_editorial=0):
        self.__id_editorial = id_editorial
        self.__nombre = nombre



    def get_id_editorial(self):
        return self.__id_editorial
    def set_id_editorial(self,id_editorial):
        self.__id_editorial = id_editorial
    


    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    
    def __str__(self):
        txt = f"El id es {self.__id_editorial}"
        txt += f"\nEl nombre es {self.__nombre}"
        return txt