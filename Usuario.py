class Usuario:
    def __init__(self,nombre:str,apellido:str,contraseña:str,rol:int,id_usuario=int):
        self.__id_usuario = id_usuario
        self.__rol = rol
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contraseña = contraseña

    def get_id_usuario(self):
        return self.__id_usuario
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
    
    def get_rol(self):
        return self.__rol
    def set_rol(self, rol):
        self.__rol = rol
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña

    
    def __str__(self):
        txt = f"El ID de usuario es {self.__id_usuario}"
        txt += f"\nEl rol es {self.__rol}"
        txt += f"\nEl nombre es {self.__nombre}"
        txt += f"\nEl apellido es {self.__apellido}"
        txt += f"\nLa contraseña es {self.__contraseña}"
        return txt