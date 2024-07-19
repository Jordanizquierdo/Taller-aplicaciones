class Informe_Movimiento:
    def __init__(self,fecha:str,usuario_ID_usuario:int,ID_movimiento=0):
        self.__fecha = fecha
        self.__usuario_ID_usuario = usuario_ID_usuario
        self.__ID_movimiento = ID_movimiento


    
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self,fecha):
        self.__fecha = fecha
    
    def get_usuario_ID_usuario(self):
        return self.__usuario_ID_usuario
    def set_usuario_ID_usuario(self,usuario_ID_usuario):
        self.__usuario_ID_usuario = usuario_ID_usuario

    def get_ID_movimiento(self):
        return self.__ID_movimiento
    def set_ID_movimiento(self,ID_movimiento):
        self.__ID_movimiento = ID_movimiento

    
    def __str__(self):
        txt = f"La fecha es {self.__fecha}"
        txt += f"\nEL id usuario es {self.__usuario_ID_usuario}"
        txt += f"\nEl id movimiento es {self.__ID_movimiento}"
        return txt