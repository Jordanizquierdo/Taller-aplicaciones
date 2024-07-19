from Producto import Producto
from Bodega import Bodega
from Sucursal import Sucursal
from Usuario import Usuario
import mysql.connector
import Credenciales
from Tipo import Tipo
from Editorial import Editorial
from Autor import Autor
from Informe_Movimiento import Informe_Movimiento
class DAO:
    def __init__(self):
        self.conectar()
    
    def conectar(self):
        self.__conexion = mysql.connector.connect(**Credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()
    
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def test(self):
        self.conectar()
        sql = "INSERT INTO Rol (Nombre) VALUES ('Administrador')"
        self.__cursor.execute(sql)
        self.cerrar()



    def eliminar_bodega(self,id_bodega):
        self.conectar()
        sql = "DELETE FROM Bodega WHERE id_bodega = %s"
        values = (id_bodega, )
        self.__cursor.execute(sql,values)

        sql = "DELETE FROM Bodega_has_Producto WHERE Bodega_ID_bodega = %s"
        values = (id_bodega, )
        self.__cursor.execute(sql,values)

        self.cerrar()
 
    
    def registrar_usuario(self, usuario:Usuario):
        print(usuario)
        sql = "INSERT INTO usuario (Rol_ID_rol, Nombre, Apellido, Contraseña) VALUES (%s, %s, %s, %s)"
        val = (usuario.get_rol(), usuario.get_nombre(), usuario.get_apellido(), usuario.get_contraseña())
        self.__cursor.execute(sql, val)
        self.cerrar()

    def validar_usuario(self, id_usuario, contraseña):
        sql = "SELECT * FROM usuario WHERE id_usuario = %s AND contraseña = %s"
        val = (id_usuario, contraseña)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchone()
        if result:
            return True
        return False
    
    def recuperar_cargo(self, id_usuario):
        sql = "SELECT Rol_ID_rol FROM usuario WHERE id_usuario = %s"
        val = (id_usuario,)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchone()
        self.cerrar()
        
        if result:
            return result[0]
        else:
            return None
        
    

    def registrar_producto(self,c:Producto):
        self.conectar()
        sql = "INSERT INTO Producto (nombre, Descripcion, Tipo_ID_tipo, cantidad) VALUES (%s, %s, %s,%s)"
        values = (c.get_nombre(),c.get_descripcion(),c.get_tipo_id_tipo(),c.get_cantidad())
        self.__cursor.execute(sql,values)
        self.cerrar()

    def recuperar_pro(self,nombre:str):
        self.conectar()
        sql = "SELECT ID_producto FROM Producto WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
        
    def recuperar_all_pro(self):
        self.conectar()
        sql = "SELECT * FROM Producto"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        p = []
        for a in registros:
            p.append(a)
        return p
    
    def recuperar_producto5(self,nombre:str):
        self.conectar()
        sql = "SELECT * FROM Producto WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registros = self.__cursor.fetchone()
        p=[]
        for a in registros:
            p.append(a)
        return p

    def registrarTipo(self,tipo):
        self.conectar()
        sql= "INSERT INTO Tipo (Nombre) VALUES (%s)"
        values = (tipo,)
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def recuperarTipo(self,nombre:str)-> Tipo:
        self.conectar()
        sql = "SELECT Nombre FROM Tipo WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None

    def recuperarTipo2(self,nombre:str)-> Tipo:
        self.conectar()
        sql = "SELECT ID_tipo FROM Tipo WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None

    def recuperarTipo3(self,id):
        self.conectar()
        sql = "SELECT Nombre FROM Tipo WHERE ID_tipo = %s"
        values = (id,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None

    def registrarEditorial(self,editorial):
        self.conectar()
        sql= "INSERT INTO Editorial ( Nombre) VALUES (%s)"
        values = (editorial,)
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def recuperarEditorial(self,nombre:str)-> Editorial:
        self.conectar()
        sql = "SELECT Nombre FROM Editorial WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
        
    def recuperarEditorial2(self,nombre:str)-> Editorial:
        self.conectar()
        sql = "SELECT ID_editorial FROM Editorial WHERE nombre = %s"
        values = (nombre,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
    def recuperarEditorial3(self,id):
        self.conectar()
        sql = "SELECT Nombre FROM Editorial WHERE ID_editorial = %s"
        values = (id,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
    def recuperarEditorial4(self,id_producto):
        self.conectar()
        sql = "SELECT Editorial_ID_editorial FROM Editorial_has_Producto WHERE Producto_ID_producto = %s"
        values = (id_producto,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None

    def registrarAutor(self,c:Autor):
        self.conectar()
        sql= "INSERT INTO Autor ( Nombre,Apellido,Edad) VALUES (%s,%s,%s)"
        values = (c.get_nombre(),c.get_apellido(),c.get_edad())
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def recuperarAutor(self,nombre:str,apellido:str)-> Autor:
        self.conectar()
        sql = "SELECT * FROM Autor WHERE Nombre = %s and Apellido = %s"
        values = (nombre,apellido)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
        
    def recuperarAutor2(self,nombre:str,apellido:str)-> Autor:
        self.conectar()
        sql = "SELECT ID_autor FROM Autor WHERE Nombre = %s and Apellido = %s"
        values = (nombre,apellido)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
    
    def recuperarAutor3(self,id):
        self.conectar()
        sql = "SELECT Nombre,Apellido FROM Autor WHERE ID_Autor = %s"
        values = (id,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
    def recuperarAutor4(self,id_producto):
        self.conectar()
        sql = "SELECT Autor_ID_autor FROM Producto_has_Autor WHERE Producto_ID_producto = %s"
        values = (id_producto,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None

    def registarProducto_has_autor(self,id_autor,id_producto):
        self.conectar()
        sql= "INSERT INTO Producto_has_Autor (Producto_ID_producto,Autor_ID_autor ) VALUES (%s, %s)"
        values = (id_producto,id_autor)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def modificarProducto_has_autor(self,id_autor,id_producto):
        self.conectar()
        sql= "UPDATE Producto_has_Autor SET Autor_ID_autor = %s Where producto_ID_producto = %s"
        values = (id_autor,id_producto)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def registarBodega_has_producto(self,id_bodega,id_producto):
        self.conectar()
        sql= "INSERT INTO Bodega_has_Producto (bodega_ID_bodega,producto_ID_producto ) VALUES (%s, %s)"
        values = (id_bodega,id_producto)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def registareditorial_has_producto(self,id_editorial,id_producto):
        self.conectar()
        sql= "INSERT INTO Editorial_has_Producto (Editorial_ID_editorial,producto_ID_producto ) VALUES (%s, %s)"
        values = (id_editorial,id_producto)
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def modificarEditorial_has_producto(self,id_editorial,id_producto):
        self.conectar()
        sql= "UPDATE Editorial_has_Producto SET Editorial_ID_editorial = %s Where producto_ID_producto = %s"
        values = (id_editorial,id_producto)
        self.__cursor.execute(sql,values)
        self.cerrar()


    def recuperar_producto(self,id_producto:str)-> Producto:
        self.conectar()
        sql = "SELECT * FROM Producto WHERE ID_producto = %s"
        values = (id_producto,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = Producto(registro[1], registro[2],registro[3],registro[4],registro[0])
            return h
        else:
            return None

    def modificar_producto(self,c:Producto):
        self.conectar()
        sql = "UPDATE Producto SET nombre = %s, Descripcion = %s, Tipo_ID_tipo = %s, cantidad = %s Where id_producto = %s"
        values = (c.get_nombre(),c.get_descripcion(),c.get_tipo_id_tipo(),c.get_cantidad(),c.get_id_producto())
        self.__cursor.execute(sql,values)
        self.cerrar()

    def eliminar_producto(self,id_producto):
        self.conectar()
        sql = "DELETE FROM Producto WHERE id_producto = %s"
        values = (id_producto, )
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def eliminar_has_prod(self, id):
        self.conectar()
        sql = "DELETE FROM Bodega_has_Producto WHERE Producto_ID_producto = %s"
        values = (id, )
        self.__cursor.execute(sql,values)

        sql = "DELETE FROM Editorial_has_Producto WHERE Producto_ID_producto = %s"
        values = (id, )
        self.__cursor.execute(sql,values)

        sql = "DELETE FROM Producto_has_Autor WHERE Producto_ID_producto = %s"
        values = (id, )
        self.__cursor.execute(sql,values)

        sql = "DELETE FROM Producto_has_Informe_movimiento WHERE Producto_ID_producto = %s"
        values = (id, )
        self.__cursor.execute(sql,values)

        self.cerrar()
    

    def registrar_bodega(self,c:Bodega):
        self.conectar()
        sql = "Insert into Bodega (codigo,ubicacion) VALUES (%s, %s)"
        values = (c.get_codigo(),c.get_ubicacion())
        self.__cursor.execute(sql,values)
        self.cerrar()

    def modificar_bodega(self,c:Bodega):
        self.conectar()
        sql = "UPDATE Bodega SET ubicacion = %s Where id_bodega = %s"
        values = (c.get_ubicacion(),c.get_id_bodega())
        self.__cursor.execute(sql,values)
        self.cerrar()


    def recuperarBodega5(self,codigo:str)-> Bodega:
        self.conectar()
        sql = "SELECT * FROM Bodega WHERE codigo = %s"
        values = (codigo,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            a = Bodega(registro[1], registro[2], registro[0])
            return a
        else:
            return None
        
    def recuperarBodega(self,codigo:str)-> Bodega:
        self.conectar()
        sql = "SELECT * FROM Bodega WHERE codigo = %s"
        values = (codigo,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            
            return registro
        else:
            return None

        
    def recuperarBodega2(self,codigo:str)-> Bodega:
        self.conectar()
        sql = "SELECT ID_bodega FROM Bodega WHERE codigo = %s"
        values = (codigo,)
        self.__cursor.execute(sql,values)
        registro = self.__cursor.fetchone()
        if registro !=None:
            h = registro
            return h
        else:
            return None
    
    def recuperarBodega3(self):
        self.conectar()
        sql = "SELECT * FROM Bodega"
        self.__cursor.execute(sql)
        registro = self.__cursor.fetchone()
        lista_bodegas = []

        for tupla in registro:

            bodega = Bodega(tupla[1], tupla[2]) 
            lista_bodegas.append(bodega)

        return lista_bodegas


    def recuperar_todas_las_bodegas(self):
        self.conectar()
        sql = "SELECT id_bodega, codigo, ubicacion FROM Bodega"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        p = []
        for a in registros:
            p.append(a)
        return p


    def recuperar_all_usuarios(self):
        self.conectar()
        sql = "SELECT id_usuario, Rol_ID_rol, Nombre, Apellido, Contraseña FROM usuario"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        p = []
        for a in registros:
            p.append(a)
        return p
    
    def recuperar_movimiento(self):
        self.conectar()
        sql = "SELECT * FROM Informe_movimiento"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        p = []
        for a in registros:
            p.append(a)
        return p





    def insertar_movimiento(self,fecha,usuario):
        self.conectar()
        sql = "Insert into Informe_movimiento (Fecha,usuario_ID_usuario) VALUES (%s, %s)"
        values = (fecha,usuario)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def obtener_ID_informe(self,fecha,usuario):
        self.conectar()
        sql = "SELECT ID_movimiento FROM Informe_movimiento WHERE Fecha=%s AND usuario_ID_usuario=%s"
        values = (fecha,usuario)
        self.__cursor.execute(sql,values)
        ID = self.__cursor.fetchone()
        self.cerrar()
        return ID

    def mover_producto(self,cantidad,producto_id,informe_id):
        self.conectar()
        sql= "INSERT INTO Producto_has_Informe_movimiento (cantidad,Producto_ID_producto,Informe_movimiento_ID_movimiento) VALUES (%s, %s, %s)"
        values = (cantidad,producto_id,informe_id)
        self.__cursor.execute(sql,values)
        self.cerrar()
    
    def bodega_movimiento(self,bodega_id_origen,bodega_id_destino,informe_id):
        self.conectar()
        sql= "INSERT INTO Bodega_has_Informe_movimiento (Bodega_ID_bodega,Bodega_ID_bodega2,Informe_movimiento_ID_movimiento) VALUES (%s, %s, %s)"
        values = (bodega_id_origen,bodega_id_destino,informe_id)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def bodega_producto(self,bodega_id_,producto_id):
        self.conectar()
        sql= "UPDATE Bodega_has_Producto SET Bodega_ID_bodega=%s WHERE Producto_ID_producto=%s"
        values = (bodega_id_,producto_id)
        self.__cursor.execute(sql,values)
        self.cerrar()

    def recuperar_movimiento(self):
        self.conectar()
        sql = "SELECT * FROM Informe_movimiento"
        self.__cursor.execute(sql)
        registros = self.__cursor.fetchall()
        self.cerrar()
    
        lista_informe = []
        for registro in registros:
            informe = Informe_Movimiento(registro[1], registro[2], registro[0])
            lista_informe.append(informe)
        return lista_informe

    def recuperar_bodega_movimiento(self,ID):
        self.conectar()
        sql = "SELECT Bodega_ID_bodega, Bodega_ID_bodega2 FROM Bodega_has_Informe_movimiento WHERE Informe_movimiento_ID_movimiento=%s"
        values = (ID,)
        self.__cursor.execute(sql,values)
        registros = self.__cursor.fetchone()
        self.cerrar()
        return registros























