from Usuario import Usuario
from DAO import DAO
from tkinter import messagebox, ttk
import tkinter as tk

from Comandos import registrar_producto, editar_producto, all_prod, buscar_producto, registrar_bodega, delete_prod, delete_bodega, registrar_u, editar_bodega, transferir_p, all_usuarios, all_bodegas, informe_movimiento

usuario_global = None

def volver_al_menu(current_window, menu_window):
    current_window.withdraw()
    menu_window.deiconify()


def iniciar_sesion():
    id_usuario = entry_login_ID_usuario.get()
    contraseña = entry_login_contraseña.get()
    d = DAO()
    usuario = d.validar_usuario(id_usuario, contraseña)
    id = d.recuperar_cargo(id_usuario)
    if usuario:
        global usuario_global
        usuario_global = usuario
        messagebox.showinfo("Éxito", f"Bienvenido")
        
        if id == 1:
            mostrar_menu_admin()
            login_window.withdraw()
        elif id == 2:
            mostrar_menu_Jbodega()
            login_window.withdraw()
        elif id == 3:
            mostrar_menu_bodeguero()
        
    else:
        messagebox.showerror("Error", "ID de usuario o contraseña incorrectos") 

def editar_p(menu_window):
    menu_window.withdraw()
    j = editar_producto()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)


def registrar_p(menu_window):
    menu_window.withdraw()
    j = registrar_producto()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def mostrar_p(menu_window):
    menu_window.withdraw()
    j = all_prod()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def buscar_p1(menu_window):
    menu_window.withdraw()
    j = buscar_producto()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def registrar_b(menu_window):
    menu_window.withdraw()
    j = registrar_bodega()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def eliminar_p(menu_window):
    menu_window.withdraw()
    j = delete_prod()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def eliminar_b(menu_window):
    menu_window.withdraw()
    j = delete_bodega()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def mostrar_bodegas(menu_window):
    menu_window.withdraw()
    j = all_bodegas()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def informe_mov(menu_window):
    menu_window.withdraw()
    j = informe_movimiento()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def mostrar_registro_usuario(menu_window):
    menu_window.withdraw()
    j = registrar_u()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def modif_bodega(menu_window):
    menu_window.withdraw()
    j = editar_bodega()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def mover_p(menu_window):
    menu_window.withdraw()
    j = transferir_p()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def all_usuario(menu_window):
    menu_window.withdraw()
    j = all_usuarios()
    j.root.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(j.root, menu_window))
    tk.Button(j.root, text="Volver", command=lambda: volver_al_menu(j.root, menu_window)).pack(pady=5)

def mostrar_menu_admin():
    menu_window = tk.Toplevel(root) 
    menu_window.title("Menú Principal")
    menu_window.geometry("300x600")
    menu_window.resizable(False,False)

    tk.Frame(menu_window, bg="#4e8889", height=50, width=400).place(x=0,y=0)
    tk.Label(menu_window, text=f"Bienvenido admin", font=("Arial", 20), bg="#4E8889", fg="#FFFFFF").pack(pady=10)
  
    tk.Label(menu_window, text=f"Usuario", font=("Arial", 15), fg="#4E8889").place(x=115,y=50)
    tk.Button(menu_window, text="Registrar Usuario", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: mostrar_registro_usuario(menu_window), padx=40).place(x=55,y=75)
    tk.Button(menu_window, text="Mostrar Todos los usuarios", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: all_usuario(menu_window), padx=43).place(x=20,y=105)
  
    tk.Frame(menu_window, bg="#4e8889", height=180, width=400).place(x=0,y=140)
    tk.Label(menu_window, text=f"Productos", font=("Arial", 15), bg="#4E8889", fg="#FFFFFF").place(x=110,y=140)
    tk.Button(menu_window, text="Registrar Producto", font=("Arial", 10), command=lambda: registrar_p(menu_window), padx=40).place(x=55,y=175)

    tk.Button(menu_window, text="Buscar Producto", font=("Arial", 10),command=lambda: buscar_p1(menu_window), padx=8).place(x=20,y=210)
    tk.Button(menu_window, text="Eliminar Producto", font=("Arial", 10), command=lambda: eliminar_p(menu_window), padx=5).place(x=160,y=210)

    tk.Button(menu_window, text="Modificar Producto", font=("Arial", 10), command=lambda: editar_p(menu_window), padx=9).place(x=20,y=245)
    tk.Button(menu_window, text="Mover Producto", font=("Arial", 10), command=lambda: mover_p(menu_window), padx=9).place(x=165,y=245)
    tk.Button(menu_window, text="Mostrar Todos los Productos", font=("Arial", 10), command=lambda:mostrar_p(menu_window), padx=43).place(x=20,y=285)

    tk.Label(menu_window, text=f"Bodegas", font=("Arial", 15), fg="#4E8889").place(x=110,y=325)
    tk.Button(menu_window, text="Registrar Bodega", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF", command=lambda: registrar_b(menu_window), padx=5).place(x=20,y=360)
    tk.Button(menu_window, text="Modificar Bodega", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: modif_bodega(menu_window), padx=5).place(x=160,y=360)
    tk.Button(menu_window, text="Eliminar Bodega", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: eliminar_b(menu_window), padx=77).place(x=20,y=395)
    tk.Button(menu_window, text="Mostrar Todas las Bodegas", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: mostrar_bodegas(menu_window), padx=45).place(x=20,y=430)
    tk.Button(menu_window, text="Mostrar informe de movimiento", font=("Arial", 10), bg="#4E8889", fg="#FFFFFF",command=lambda: informe_mov(menu_window), padx=45).place(x=12,y=460)

    tk.Frame(menu_window, bg="#4e8889", height=90, width=400).place(x=0,y=550)
    tk.Button(menu_window, text="Cerrar Sesión", font=("Arial", 12), command=lambda: cerrar_sesion(menu_window)).place(x=100,y=510)
    tk.Label(menu_window, text="Libreria El poeta - @copyright 2024", font=("Arial", 10), bg="#4e8889", fg="#FFFFFF").place(x=55,y=570)


def mostrar_menu_Jbodega():
    root.withdraw()
    menu_jefe = tk.Toplevel(root)
    menu_jefe.title("Menu Jefe de Bodega")
    menu_jefe.geometry("300x400")
    menu_jefe.resizable(False,False)

    tk.Frame(menu_jefe, bg="#4e8889", height=300, width=400).place(x=0,y=0)

    tk.Label(menu_jefe, text="Gestion Jefe de Bodega", font=("Arial", 20), bg="#4e8889", fg="#FFFFFF").pack(pady=10)

    tk.Label(menu_jefe, text="Productos", font=("Arial", 12), bg="#4e8889", fg="#FFFFFF").place(x=120,y=50)
    tk.Button(menu_jefe, text="Registrar Producto", command=lambda: registrar_p(menu_jefe), padx=10).place(x=25,y=80)
    tk.Button(menu_jefe, text="Eliminar Producto", command=lambda: eliminar_p(menu_jefe), padx=10).place(x=155,y=80)#############
    tk.Button(menu_jefe, text="Modificar Producto", command=lambda: editar_p(menu_jefe), padx=40).place(x=60,y=110)#############
    tk.Button(menu_jefe, text="Mostrar todos los Productos", command=lambda:mostrar_p(menu_jefe), padx=40).place(x=40,y=140)

    tk.Label(menu_jefe, text="Bodega", font=("Arial", 12), bg="#4e8889", fg="#FFFFFF").place(x=120,y=175)
    tk.Button(menu_jefe, text="Registrar bodega", command=lambda: registrar_b(menu_jefe), padx=10).place(x=30,y=205)
    tk.Button(menu_jefe, text="Eliminar bodega", command=lambda: eliminar_b(menu_jefe), padx=10).place(x=150,y=205)
    tk.Button(menu_jefe, text="Modificar bodega", command=lambda: modif_bodega(menu_jefe), padx=10).place(x=10,y=235)
    tk.Button(menu_jefe, text="Informe de movimiento", command=lambda: informe_mov(menu_jefe), padx=10).place(x=135,y=235)
    tk.Button(menu_jefe, text="Mostrar todas las bodegas", command=lambda:mostrar_bodegas(menu_jefe), padx=40).place(x=40,y=265)

    tk.Button(menu_jefe, text="CERRAR SESION",command=lambda: cerrar_sesion(menu_jefe), bg="#4E8889", fg="black", padx=18, pady=2).place(x=90,y=310)

    tk.Frame(menu_jefe, bg="#4e8889", height=50, width=400).place(x=0,y=350)
    tk.Label(menu_jefe, text="Libreria Gran poeta - @copyright 2024", font=("Arial", 10), bg="#4e8889", fg="#FFFFFF").place(x=55,y=365)

def mostrar_menu_bodeguero():
    root.withdraw()
    menu_bodega = tk.Toplevel(root)
    menu_bodega.title("Menu Bodeguero")
    menu_bodega.geometry("300x320")
    menu_bodega.resizable(False,False)

    tk.Frame(menu_bodega, bg="#4e8889", height=240, width=400).place(x=0,y=0)

    tk.Label(menu_bodega, text="Gestion Bodeguero", font=("Arial", 20), bg="#4e8889", fg="#FFFFFF").pack(pady=10)

    tk.Label(menu_bodega, text="Bodega", font=("Arial", 12), bg="#4e8889", fg="#FFFFFF").place(x=115,y=50)
    tk.Button(menu_bodega, text="Mostrar todos las bodegas", command=lambda:mostrar_bodegas(menu_bodega), padx=20).place(x=55,y=80)
    tk.Button(menu_bodega, text="Informe de movimiento", command=lambda: informe_mov(menu_bodega), padx=20).place(x=61,y=110)

    tk.Label(menu_bodega, text="Productos", font=("Arial", 12), bg="#4e8889", fg="#FFFFFF").place(x=115,y=140)
    tk.Button(menu_bodega, text="Mover Producto de bodega", command=lambda: mover_p(menu_bodega), padx=20).place(x=55,y=170)
    tk.Button(menu_bodega, text="Mostrar todos los productos", command=lambda:mostrar_p(menu_bodega), padx=19).place(x=54,y=200)

    tk.Button(menu_bodega, text="Cerrar sesion", command=lambda: cerrar_sesion(menu_bodega), bg="#4E8889", fg="black", padx=18, pady=2).place(x=100,y=245)

    tk.Frame(menu_bodega, bg="#4e8889", height=50, width=400).place(x=0,y=280)
    tk.Label(menu_bodega, text="Libreria Gran poeta - @copyright 2024", font=("Arial", 10), bg="#4e8889", fg="#FFFFFF").place(x=50,y=290)



def cerrar_sesion(menu_window):
    menu_window.destroy()
    login_window.deiconify()


root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

login_window = tk.Toplevel(root)
login_window.title("El Gran Poeta - Inicio de Sesión")
login_window.geometry("300x350")
login_window.resizable(False, False)
login_window.configure(bg='#4d7b82')
login_window.protocol("WM_DELETE_WINDOW", root.quit)

tk.Frame(login_window, bg="#4d7b82", height=400, width=300).place(x=0, y=0)
tk.Label(login_window, text="El Gran Poeta", font=("Arial", 20), bg="#4d7b82", fg="white").pack(pady=1)
tk.Label(login_window, text="--------------------------------------------- Libreria ---------------------------------------------", font=("Arial",10), bg="#4d7b82", fg="white").pack(pady=1)

tk.Label(login_window, text="ID de Usuario", font=("Arial", 10), bg="#4d7b82", fg="white").pack(pady=5)
entry_login_ID_usuario = tk.Entry(login_window, bg="white", fg="black")
entry_login_ID_usuario.pack(pady=5)

tk.Label(login_window, text="Contraseña", font=("Arial", 10), bg="#4d7b82", fg="white").pack(pady=5)
entry_login_contraseña = tk.Entry(login_window, show="*", bg="white", fg="black")
entry_login_contraseña.pack(pady=5)

tk.Button(login_window, text="Iniciar Sesión", command=iniciar_sesion, bg="#819fa1", fg="black", font=("Arial", 10)).pack(pady=10)
tk.Button(login_window, text="Salir", command=root.quit, bg="#819fa1", fg="black", font=("Arial", 10)).pack(pady=10)

tk.Label(login_window, text="Libreria Gran poeta - ©copyright 2024", font=("Arial", 10), bg="#4d7b82", fg="white").pack(side="bottom", pady=10)


root.withdraw()
root.mainloop()
