from Producto import Producto
from Bodega import Bodega
from Sucursal import Sucursal
from Usuario import Usuario
from DAO import DAO
from tkinter import messagebox, ttk
import tkinter as tk
from Tipo import Tipo
from Editorial import Editorial
from Autor import Autor

def buscarTipo(nombre):
    d = DAO()
    c = d.recuperarTipo(nombre)
    if c != None:
        k = c[0]
        return k
    else:
        print("No se encontro el tipo")
        return None
    

def buscarTipo2(nombre):
    d = DAO()
    c = d.recuperarTipo2(nombre)
    return c

def buscarTipo3(c):
    d = DAO()
    l = d.recuperarTipo3(c)
    return l

def buscarEditorial(nombre):
    d = DAO()
    c = d.recuperarEditorial(nombre)
    if c != None:
        k = c[0]
        return k
    else:
        print("No se encontro el Editorial")
        return None
    

def buscarEditorial2(nombre):
    d = DAO()
    c = d.recuperarEditorial2(nombre)
    return c


def buscarEditorial3(c):
    d = DAO()
    l = d.recuperarEditorial3(c)
    return l


def buscarEditorial4(id_producto):
    d = DAO()
    c = d.recuperarEditorial4(id_producto)
    j = buscarEditorial3(c[0])
    return j





def buscarproducto(nombre):
    d = DAO()
    c = d.recuperar_pro(nombre)
    return c

def buscarproducto1(nombre):
    d = DAO()
    c = d.recuperar_producto(nombre)
    return c

def buscarAutor(nombre,apellido):
    d = DAO()
    c = d.recuperarAutor(nombre,apellido)
    if c != None:
        return c
    else:
        print("No se encontro el Autor")
        a = [" "," "," "," "]
        return a

def buscarAutor2(nombre,apellido):
    d = DAO()
    c = d.recuperarAutor2(nombre,apellido)
    return c


def buscarAutor3(c):
    d = DAO()
    l = d.recuperarAutor3(c)
    return l


def buscarAutor4(id_producto):
    d = DAO()
    c = d.recuperarAutor4(id_producto)
    j = buscarAutor3(c[0])
    return j


def cambiar_campo(nombre:str,campo):
    opcion = input(f"Desea modificar el {nombre} (s/n): ")
    if opcion.lower() =="s":
        valor = input(f"Ingrese el nuevo {nombre}: ")
        return valor
    else : return campo



class delete_prod():
    def __init__(self):
        self.dao = DAO()
        self.root = tk.Tk()
        self.root.title("Eliminar Producto")

        self.label = tk.Label(self.root, text="ID del Producto:")
        self.label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.button = tk.Button(self.root, text="Eliminar", command=self.delete)
        self.button.pack()

    def delete(self):
        id_producto = self.name_entry.get()
        if id_producto:
            self.dao.eliminar_has_prod(id_producto)
            self.dao.eliminar_producto(id_producto)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese el ID del producto.")
        self.button.pack()




def buscarBodega(codigo):
    d = DAO()
    c = d.recuperarBodega(codigo)
    if c != None:
        k = c[1]
        return k
    else:
        print("No se encontro la bodega")
        return None


def buscarBodega2(nombre):
    d = DAO()
    c = d.recuperarBodega2(nombre)
    return c

def buscarBodega3():
    d = DAO()
    c = d.recuperarBodega3()
    return c


class registrar_producto:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de Gestión de Productos y Bodegas")
            
        

        # Crear pestañas para diferentes funciones
        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_bodega = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_producto, text='Producto')
        
        self.tab_control.pack(expand=1, fill="both")

        # Widgets para la pestaña de productos
        self.lbl_nombre_producto = tk.Label(self.tab_producto, text="Nombre del producto:")
        self.lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre_producto = tk.Entry(self.tab_producto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_descripcion = tk.Label(self.tab_producto, text="Descripción:")
        self.lbl_descripcion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_descripcion = tk.Entry(self.tab_producto)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_cantidad = tk.Label(self.tab_producto, text="Cantidad:")
        self.lbl_cantidad.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_cantidad = tk.Entry(self.tab_producto)
        self.entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

        
        self.lbl_Rol = tk.Label(self.tab_producto, text="Tipo:")
        self.lbl_Rol.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.rol_var = tk.StringVar()
        self.entry_Rol = tk.OptionMenu(self.tab_producto, self.rol_var, "Libro", "Revista", "Enciclopedia")
        self.entry_Rol.grid(row=3, column=1, padx=10, pady=5)



        self.lbl_editorial = tk.Label(self.tab_producto, text="Editorial:")
        self.lbl_editorial.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_editorial = tk.Entry(self.tab_producto)
        self.entry_editorial.grid(row=7, column=1, padx=10, pady=5)

        self.lbl_autor = tk.Label(self.tab_producto, text="Nombre y Apellido del Autor:")
        self.lbl_autor.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_autor = tk.Entry(self.tab_producto)
        self.entry_autor.grid(row=8, column=1, padx=10, pady=5)

        self.btn_registrar_producto = tk.Button(self.tab_producto, text="Registrar Producto", command=self.registrar_producto)
        self.btn_registrar_producto.grid(row=9, column=0, columnspan=2, pady=10)


        self.dao = DAO()

    def registrar_producto(self):
        nombre = self.entry_nombre_producto.get().capitalize().strip()
        descripcion = self.entry_descripcion.get().capitalize()
        cantidad = self.entry_cantidad.get().capitalize().strip()
        tipo = self.rol_var.get()
        print(tipo)
        tipo_prueba = buscarTipo(tipo)
        print(tipo_prueba)
        d = DAO()

        if tipo != tipo_prueba:
            self.agregar_pestana_tipo(tipo)
            d.registrarTipo(tipo)
        id_tipo = buscarTipo2(tipo)[0]
        p = Producto(nombre,descripcion,id_tipo,cantidad)
        d.registrar_producto(p)
        

        editorial = self.entry_editorial.get().capitalize()
        editorial_prueba = buscarEditorial(editorial)
        if editorial != editorial_prueba:
            self.agregar_pestana_tipo(editorial)
            d.registrarEditorial(editorial)
        id_editorial = buscarEditorial2(editorial)[0]
        id_producto = buscarproducto(nombre)[0]

        d.registareditorial_has_producto(id_editorial,id_producto)
        autor = self.entry_autor.get().capitalize()
        autor1 = autor.lower()
        x = autor1.split()
        nAutor= x[0]
        aAutor = x[1]
        autor_prueba = buscarAutor(nAutor,aAutor)
        a = []
        a.append(autor_prueba[1].lower())
        a.append(autor_prueba[2].lower())
        if x != a:
            print("El autor no existe")
            new_window = tk.Toplevel(self.root)
            new_window.title("Registrar Nuevo Autor")

            lbl_edad_Autor = tk.Label(new_window, text="Edad del autor:")
            lbl_edad_Autor.pack(pady=10)
            entry_edad_Autor = tk.Entry(new_window)
            entry_edad_Autor.pack(pady=5)

            def save_Autor():
                edad = entry_edad_Autor.get()
                h = Autor(nAutor,aAutor,edad)
                d = DAO()
                d.registrarAutor(h)
                messagebox.showinfo("Registro", "Autor registrada exitosamente!")
                new_window.destroy()
            btn_guardar_Autor = tk.Button(new_window, text="Guardar Autor", command=save_Autor)
            btn_guardar_Autor.pack(pady=10)
            new_window.wait_window()  
        id_producto = buscarproducto(nombre)[0]
        id_autor = buscarAutor2(nAutor,aAutor)[0]

        d.registarProducto_has_autor(id_autor,id_producto)
        messagebox.showinfo("Exito",f"Éxito Al registrar {nombre}")


        new_window = tk.Toplevel(self.root)
        new_window.title("Registrar Codigo bodega")

        new_window.protocol("WM_DELETE_WINDOW", lambda: None)

        lbl_nombre_codigo = tk.Label(new_window, text="Ingrese el codigo de la bodega:")
        lbl_nombre_codigo.pack(pady=10)
        entry_nombre_codigo = tk.Entry(new_window)
        entry_nombre_codigo.pack(pady=5)

        def save_bodega_producto():
            bodega = entry_nombre_codigo.get().capitalize()
            bodega_prueba = buscarBodega(bodega)
            if bodega != bodega_prueba:
                messagebox.showinfo("Bodega", "Debe ingresar un codigo de bodega valido")
                

            else: 
                id_bodega = buscarBodega2(bodega)[0]
                id_producto = buscarproducto(nombre)[0]

                d.registarBodega_has_producto(id_bodega,id_producto)
                messagebox.showinfo("Registro", "codigo registrada exitosamente!")
                new_window.destroy()


        btn_guardar_codigo = tk.Button(new_window, text="Guardar codigo", command=save_bodega_producto)
        btn_guardar_codigo.pack(pady=10)

        new_window.grab_set() 


    def agregar_pestana_tipo(self, tipo):

            new_tab = ttk.Frame(self.tab_control)
            self.tab_control.add(new_tab, text=f'Agregar "{tipo}"')

            lbl_nuevo_tipo = tk.Label(new_tab, text=f'Ingrese detalles para "{tipo}":')
            lbl_nuevo_tipo.pack(padx=10, pady=10)




class editar_producto:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de edición de Productos")
            
        


        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_producto, text='Producto')
        
        self.tab_control.pack(expand=1, fill="both")


        self.lbl_nombre_producto = tk.Label(self.tab_producto, text="ID del producto:")
        self.lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre_producto = tk.Entry(self.tab_producto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=5)

        

        self.btn_registrar_producto = tk.Button(self.tab_producto, text="Modificar Producto", command=self.validar_P)
        self.btn_registrar_producto.grid(row=6, column=0, columnspan=2, pady=10)

    
    def validar_P(self):
        d = DAO()
        c = d.recuperar_producto(self.entry_nombre_producto.get())
        if c != None:
            self.lbl_nombre_producto = tk.Label(self.tab_producto, text="Nombre del producto:")
            self.lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_nombre_producto = tk.Entry(self.tab_producto)
            self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=5)
            self.entry_nombre_producto.insert(0, c.get_nombre())


            self.lbl_descripcion = tk.Label(self.tab_producto, text="Descripción:")
            self.lbl_descripcion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_descripcion = tk.Entry(self.tab_producto)
            self.entry_descripcion.grid(row=1, column=1, padx=10, pady=5)
            self.entry_descripcion.insert(0, c.get_descripcion())

            self.lbl_cantidad = tk.Label(self.tab_producto, text="Cantidad:")
            self.lbl_cantidad.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_cantidad = tk.Entry(self.tab_producto)
            self.entry_cantidad.grid(row=2, column=1, padx=10, pady=5)
            self.entry_cantidad.insert(0, c.get_cantidad())

            self.lbl_tipo = tk.Label(self.tab_producto, text="Tipo de producto:")
            self.lbl_tipo.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_tipo = tk.Entry(self.tab_producto)
            self.entry_tipo.grid(row=3, column=1, padx=10, pady=5)
            o = buscarTipo3(c.get_tipo_id_tipo())
            self.entry_tipo.insert(0, o)

            self.lbl_editorial = tk.Label(self.tab_producto, text="Editorial:")
            self.lbl_editorial.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_editorial = tk.Entry(self.tab_producto)
            self.entry_editorial.grid(row=4, column=1, padx=10, pady=5)
            d = buscarEditorial4(c.get_id_producto())
            self.entry_editorial.insert(0, d)

            self.lbl_autor = tk.Label(self.tab_producto, text="Nombre y Apellido del Autor:")
            self.lbl_autor.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_autor = tk.Entry(self.tab_producto)
            self.entry_autor.grid(row=5, column=1, padx=10, pady=5)
            x = buscarAutor4(c.get_id_producto())
            self.entry_autor.insert(0, x)


            def modificar():
                h = c
                if h !=None:
                    nombre = self.entry_nombre_producto.get()
                    h.set_nombre(nombre)
                    descripcion = self.entry_descripcion.get()
                    h.set_descripcion(descripcion)
                    tipo_id_tipo = self.entry_tipo.get()
                    a = buscarTipo2(tipo_id_tipo)[0]
                    h.set_tipo_id_tipo(a)
                    cantidad = self.entry_cantidad.get()
                    h.set_cantidad(cantidad)
                    d = DAO()
                    d.modificar_producto(h)
                    #editorial
                    e = buscarEditorial2(self.entry_editorial.get())[0]
                    i = buscarproducto(nombre)[0]
                    d.modificarEditorial_has_producto(e,i)
                    #autor
                    autor = self.entry_autor.get()
                    print(autor)
                    p = autor.split()
                    nAutor= p[0]
                    aAutor = p[1]
                    print(f"nombre:{nAutor} apelllido:{aAutor}")
                    #id autor
                    ñ = buscarAutor2(nAutor,aAutor)[0]
                    print(ñ)
                    d.modificarProducto_has_autor(ñ,i)

                    messagebox.showinfo("Modificación", "Producto modificado exitosamente!")
                    self.root.destroy()


            

            self.btn_registrar_producto = tk.Button(self.tab_producto, text="Modificar Producto", command=modificar)
            self.btn_registrar_producto.grid(row=6, column=0, columnspan=2, pady=10)
            







class buscar_producto:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de busqueda de Productos")
            
        


        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_producto, text='Producto')
        
        self.tab_control.pack(expand=1, fill="both")

        # Widgets para la pestaña de productos
        self.lbl_nombre_producto = tk.Label(self.tab_producto, text="nombre del producto:")
        self.lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre_producto = tk.Entry(self.tab_producto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=5)

        

        self.btn_registrar_producto = tk.Button(self.tab_producto, text="Buscar Producto", command=self.buscar_P)
        self.btn_registrar_producto.grid(row=6, column=0, columnspan=2, pady=10)

    
    def buscar_P(self):
        d = DAO()
        nombre = self.entry_nombre_producto.get()
        a = d.recuperar_producto5(nombre)
        print(nombre)
        print(a)



        producto = a
        if producto is None:
            print("Producto no encontrado")
            return
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Descripcion", "Id tipo", "Cantidad"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Nombre")
        self.tree.heading("#2", text="Descripcion")
        self.tree.heading("#3", text="Id tipo")
        self.tree.heading("#4", text="Cantidad")

        self.tree.insert("", "end", text=str(producto[0]), values=producto[1:])

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.column("#0", width=50)

        


class registrar_bodega:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de Gestión de Productos y Bodegas")
            
        


        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_bodega = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_bodega, text='Bodegas')
        
        self.tab_control.pack(expand=1, fill="both")


        self.lbl_codigo_bodega = tk.Label(self.tab_bodega, text="Código de la bodega:")
        self.lbl_codigo_bodega.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_codigo_bodega = tk.Entry(self.tab_bodega)
        self.entry_codigo_bodega.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_ubicacion = tk.Label(self.tab_bodega, text="Ubicación:")
        self.lbl_ubicacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_ubicacion = tk.Entry(self.tab_bodega)
        self.entry_ubicacion.grid(row=1, column=1, padx=10, pady=5)

        self.btn_registrar_bodega = tk.Button(self.tab_bodega, text="Registrar Bodega", command=self.registrar_bod)
        self.btn_registrar_bodega.grid(row=2, column=0, columnspan=2, pady=10)


        self.dao = DAO()
    def registrar_bod(self):
        codigo = self.entry_codigo_bodega.get()
        ubicacion = self.entry_ubicacion.get()
        bodega_prueba = buscarBodega(codigo)
        if codigo != bodega_prueba:
            p = Bodega(codigo,ubicacion)
            d = DAO()
            d.registrar_bodega(p)
            messagebox.showinfo("Registro Bodega", "La bodega se ha registrado exitosamente!")
        else:messagebox.showinfo("Bodega", "La bodega ya existe!")

class delete_bodega():
    def __init__(self):
        self.dao = DAO()
        self.root = tk.Tk()
        self.root.title("Eliminar Bodega")

        self.label = tk.Label(self.root, text="ID Bodega:")
        self.label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.button = tk.Button(self.root, text="Eliminar", command=self.delete)
        self.button.pack()

    def delete(self):
        try:
            id_producto = self.name_entry.get()
            if id_producto:
                self.dao.eliminar_bodega(id_producto)
                self.dao.eliminar_producto(id_producto)
                messagebox.showinfo("Éxito", "Bodega eliminada correctamente.")
            else:
                messagebox.showwarning("Advertencia", "Por favor ingrese el ID de la bodega.")
            self.button.pack()
        except:
             messagebox.showwarning("Advertencia", "La bodega contiene Productos!.")


    
    
class all_prod():
    def __init__(self,):
        a = DAO().recuperar_all_pro()
        list_prod = []
        for i in a:
                list_prod.append(i)
        if a:
            root = tk.Tk()
            self.root = root
            self.root.title("Productos")
            
            self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Descripcion", "Cantidad"))
            self.tree.heading("#0", text="ID")
            self.tree.heading("#1", text="Nombre")
            self.tree.heading("#2", text="Descripcion")
            self.tree.heading("#3", text="Id tipo")
            self.tree.heading("#4", text="Cantidad")

            for i, dato in enumerate(list_prod, start=1):
                self.tree.insert("", "end", text=str(dato[0]), values=dato[1:])

            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree.column("#0", width=50)
        else:
            messagebox.showinfo("Información", "No hay productos registrados.")

class all_usuarios():
    def __init__(self,):
        a = DAO().recuperar_all_usuarios()
        list_prod = []
        for i in a:
                list_prod.append(i)
        root = tk.Tk()
        self.root = root
        self.root.title("Usuarios")
            
        self.tree = ttk.Treeview(self.root, columns=("ID", "ID rol" , "Nombre", "apellido", "Contraseña"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="ID rol")
        self.tree.heading("#2", text="Nombre")
        self.tree.heading("#3", text="Apellido")
        self.tree.heading("#4", text="Contraseña")

        for i, dato in enumerate(list_prod, start=1):
            self.tree.insert("", "end", text=str(dato[0]), values=dato[1:])

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.column("#0", width=50)


class all_bodegas():
    def __init__(self,):
        a = DAO().recuperar_todas_las_bodegas()
        list_prod = []
        for i in a:
                list_prod.append(i)
        root = tk.Tk()
        self.root = root
        self.root.title("Usuarios")
            
        self.tree = ttk.Treeview(self.root, columns=("ID","Codigo","Ubicacion"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Codigo")
        self.tree.heading("#2", text="Ubicacion")
        
        for i, dato in enumerate(list_prod, start=1):
            self.tree.insert("", "end", text=str(dato[0]), values=dato[1:])

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.column("#0", width=50)

class informe_movimiento():
    def __init__(self):
        root = tk.Tk()
        d = DAO()
        bodegas = d.recuperar_movimiento()
        if bodegas:
            self.root = root
            self.root.title("Informe")

            for bodega in bodegas:
                h = d.recuperar_bodega_movimiento(bodega.get_ID_movimiento())
                print(h)
                tk.Label(self.root, text=f"Id usuario: {bodega.get_usuario_ID_usuario()}, Fecha: {bodega.get_fecha()}, Bodega de origen: {h[0]}, Bodega de destino: {h[1]}").pack(pady=5)
        else:
            messagebox.showinfo("Información", "No hay bodegas registradas.")



class registrar_u:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de Registro de usuarios")

        # Crear pestañas para diferentes funciones
        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_producto, text='Usuario')
        
        self.tab_control.pack(expand=1, fill="both")


        self.lbl_nombre = tk.Label(self.tab_producto, text="Nombre:")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre = tk.Entry(self.tab_producto)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_apellido = tk.Label(self.tab_producto, text="Apellido:")
        self.lbl_apellido.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_apellido = tk.Entry(self.tab_producto)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_Contraseña = tk.Label(self.tab_producto, text="Contraseña:")
        self.lbl_Contraseña.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_Contraseña = tk.Entry(self.tab_producto)
        self.entry_Contraseña.grid(row=2, column=1, padx=10, pady=5)


        self.lbl_Rol = tk.Label(self.tab_producto, text="Rol:")
        self.lbl_Rol.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.rol_var = tk.StringVar()
        self.entry_Rol = tk.OptionMenu(self.tab_producto, self.rol_var, "Administrador", "Jefe de Bodega", "Bodeguero")
        self.entry_Rol.grid(row=3, column=1, padx=10, pady=5)


        self.btn_registrar_usuario = tk.Button(self.tab_producto, text="Registrar Usuario", command=self.registrar_usuario1)
        self.btn_registrar_usuario.grid(row=7, column=0, columnspan=2, pady=10)
        
    def registrar_usuario1(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        contraseña = self.entry_Contraseña.get()
        rol = self.rol_var.get()
        if rol == "Administrador":
            id_rol = 1
        if rol == "Jefe de Bodega":
            id_rol = 2
        if rol == "Bodeguero":
            id_rol = 3
        if not contraseña or not nombre or not apellido or not rol:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        usuario = Usuario(nombre, apellido, contraseña, id_rol)
        d = DAO()
        d.registrar_usuario(usuario)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")


class editar_bodega:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Sistema de edición de Bodegas")
            
        self.tab_control = ttk.Notebook(self.root)
        
        self.tab_producto = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_producto, text='Bodegas')
        
        self.tab_control.pack(expand=1, fill="both")

        self.lbl_nombre_producto = tk.Label(self.tab_producto, text="codigo de la bodega:")
        self.lbl_nombre_producto.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre_producto = tk.Entry(self.tab_producto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=5)

        

        self.btn_registrar_producto = tk.Button(self.tab_producto, text="Modificar Bodega", command=self.validar_b)
        self.btn_registrar_producto.grid(row=6, column=0, columnspan=2, pady=10)

    
    def validar_b(self):
        d = DAO()
        y = d.recuperarBodega5(self.entry_nombre_producto.get().capitalize())
        self.entry_nombre_producto.config(state='disabled')
        print(y)
        if y != None:
            
            self.lbl_ubicacion = tk.Label(self.tab_producto, text="ubicacion:")
            self.lbl_ubicacion.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
            self.entry_ubicacion = tk.Entry(self.tab_producto)
            self.entry_ubicacion.grid(row=1, column=1, padx=10, pady=5)
            self.entry_ubicacion.insert(0, y.get_ubicacion())



            def modificar():
                
                h = y
                if h !=None:
                    nombre = self.entry_ubicacion.get()
                    h.set_ubicacion(nombre)
                    
                    d = DAO()
                    d.modificar_bodega(h)

                    messagebox.showinfo("Modificación", "bodega modificada exitosamente!")
                    self.root.destroy()
            self.btn_registrar_producto = tk.Button(self.tab_producto, text="Modificar bodega", command=modificar)
            self.btn_registrar_producto.grid(row=6, column=0, columnspan=2, pady=10)

        else:messagebox.showinfo("Error", "La bodega no existe!")
            

class transferir_p:
    def __init__(self):
        # Crear la interfaz
        self.root = tk.Tk()
        self.root.title("Transferencia de Productos entre Bodegas")
        
        # Crear pestañas para diferentes funciones
        self.tab_control = ttk.Notebook(self.root)
        self.tab_transferencia = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_transferencia, text='Transferencia')
        self.tab_control.pack(expand=1, fill="both")

        self.bodega_origen_label = tk.Label(self.tab_transferencia, text="Bodega Origen")
        self.bodega_origen_label.grid(row=0, column=0, padx=10, pady=10)
        self.bodega_origen_entry = tk.Entry(self.tab_transferencia)
        self.bodega_origen_entry.grid(row=0, column=1, padx=10, pady=10)

        self.bodega_destino_label = tk.Label(self.tab_transferencia, text="Bodega Destino")
        self.bodega_destino_label.grid(row=1, column=0, padx=10, pady=10)
        self.bodega_destino_entry = tk.Entry(self.tab_transferencia)
        self.bodega_destino_entry.grid(row=1, column=1, padx=10, pady=10)

        self.producto_label = tk.Label(self.tab_transferencia, text="Producto")
        self.producto_label.grid(row=2, column=0, padx=10, pady=10)
        self.producto_entry = tk.Entry(self.tab_transferencia)
        self.producto_entry.grid(row=2, column=1, padx=10, pady=10)

        self.cantidad_label = tk.Label(self.tab_transferencia, text="Cantidad")
        self.cantidad_label.grid(row=3, column=0, padx=10, pady=10)
        self.cantidad_entry = tk.Entry(self.tab_transferencia)
        self.cantidad_entry.grid(row=3, column=1, padx=10, pady=10)

        self.fecha_label = tk.Label(self.tab_transferencia, text="Fecha")
        self.fecha_label.grid(row=4, column=0, padx=10, pady=10)
        self.fecha_entry = tk.Entry(self.tab_transferencia)
        self.fecha_entry.grid(row=4, column=1, padx=10, pady=10)

        self.usuario_label = tk.Label(self.tab_transferencia, text="ID Usuario")
        self.usuario_label.grid(row=5, column=0, padx=10, pady=10)
        self.usuario_entry = tk.Entry(self.tab_transferencia)
        self.usuario_entry.grid(row=5, column=1, padx=10, pady=10)

        self.transferir_button = tk.Button(self.tab_transferencia, text="Transferir", command=self.transferir_producto)
        self.transferir_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def transferir_producto(self):
        bodega_origen_id = self.bodega_origen_entry.get()
        bodega_destino_id = self.bodega_destino_entry.get()
        producto_id = self.producto_entry.get()
        cantidad = self.cantidad_entry.get()
        fecha = self.fecha_entry.get()
        usuario = self.usuario_entry.get()

        d = DAO()
        #fecha = d.obtener_fecha_hora()
        print(fecha)
        d.insertar_movimiento(fecha,usuario)
        ID = d.obtener_ID_informe(fecha,usuario)[0]
        print(ID)


        if not bodega_origen_id or not bodega_destino_id or not producto_id or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            bodega_origen_id = int(bodega_origen_id)
            bodega_destino_id = int(bodega_destino_id)
            producto_id = int(producto_id)
            cantidad = int(cantidad)
            usuario = int(usuario)
        
        except ValueError:
            messagebox.showerror("Error", "Los IDs y la cantidad deben ser números enteros")
            return

        if bodega_origen_id == bodega_destino_id:
            messagebox.showerror("Error", "La bodega de origen y destino no pueden ser la misma.")
            return

        dao = DAO()
        try:
            dao.mover_producto(cantidad,producto_id,ID)
            dao.bodega_movimiento(bodega_origen_id,bodega_destino_id,ID)
            dao.bodega_producto(bodega_destino_id,producto_id)
            messagebox.showinfo("Éxito", "Producto transferido exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
     