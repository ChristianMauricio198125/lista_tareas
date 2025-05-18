import tkinter as tk 
from tkinter import messagebox
import sys

tareas=[]
estado = {}


def actualizarTareas():
    borrarLista()
    for tarea in tareas:
        list_box.insert(tk.END,tarea)

def agregarTarea():
    listaTarea = entrada.get().strip()
    if listaTarea:
        tareas.append(listaTarea)
        actualizarTareas()
        entrada.delete(0,tk.END)
    else:
        actualizarTareas()
        #messagebox.showerror('Atencion', 'Debe ingresar una tarea')


def tareaCompletada():
    seleccionada = list_box.curselection()
    if seleccionada:
        indice = seleccionada[0]
        tareaSeleccionada = list_box.get(indice)
        list_box.delete(indice)
        list_box.insert(indice,"~~" + tareaSeleccionada + "~~")
        tareas.pop(indice)
    else:
        messagebox.showerror('Atencion','Debe seleccionar una tarea para completar')

def guardarTarea():
    tareas = list_box.get(0, tk.END)
    with open('tareas.txt','w') as archivo:
        for tarea in tareas:
            archivo.write(tarea + '\n')
        messagebox.showinfo('Informacion','Tarea guardada')
def cargarTareas():
    try:
        with open('tareas.txt','r') as archivo:
            global tareas
            tareas = [tarea.strip() for tarea in archivo.readlines()]
    except FileNotFoundError:
        pass


def borrarLista():
    if list_box:
        list_box.delete(0,tk.END)

def borrarTodo():
    global tareas
    tareas =[]
    actualizarTareas()

def borrarUno():
    seleccionada = list_box.curselection()
    if seleccionada:
        indice = seleccionada[0]
        list_box.delete(indice)
    else:
        messagebox.showerror('Atencion','Debe seleccionar una tarea para borrar')

def ordenarAscendente():
    tareas.sort()
    actualizarTareas()

def ordenarDescendente():
    tareas.sort()
    tareas.reverse()
    actualizarTareas()

def seleccionAleatoria():
    pass

def numeroTareas():
    pass

def salir():
    respuesta = messagebox.askyesno('Salir', ' Esta seguro de Salir')
    if respuesta:
        guardarTarea()
        ventana.destroy()
        SystemExit()




#----------------------------- creamos la ventana  ----------------------
ventana = tk.Tk()
ventana.title('Tareas Pendientes')
#----------------------------- cargamos el metodo cargar tareas ---------
cargarTareas()

#----------------------------- creamos el titulo  -----------------------
titulo = tk.Label(ventana,text='Listado de Tareas')
titulo.pack(pady=5)
#----------------------------- creamos el input  -----------------------
entrada = tk.Entry(ventana,width=50)
entrada.pack(pady=5, padx=20)
#----------------------------- creamos el boton agregar tarea -----------------------
btn_agregar_tarea = tk.Button(ventana,text='Cargar y Agregar',fg='white', bg='green', command=agregarTarea)
btn_agregar_tarea.pack(pady=5)
#----------------------------- creamos el boton completar tarea -----------------------
btn_completar_tarea = tk.Button(ventana,text='Tarea Completada',fg='white', bg='green', command=tareaCompletada)
btn_completar_tarea.pack(pady=5)
#----------------------------- creamos el boton guardar tarea -----------------------
btn_guardar_tarea = tk.Button(ventana,text='Guardar Tarea',fg='white', bg='blue', command=guardarTarea)
btn_guardar_tarea.pack(pady=5)
#----------------------------- creamos el boton borrar todo -----------------------
btn_borrar_todo = tk.Button(ventana,text='Borrar Todo',fg='white', bg='green', command=borrarTodo)
btn_borrar_todo.pack(pady=5)
#----------------------------- creamos el boton borrar uno -----------------------
btn_borrar_uno = tk.Button(ventana,text='Borrar Uno',fg='white', bg='green', command=borrarUno)
btn_borrar_uno.pack(pady=5)
#----------------------------- creamos el boton ordenar ascendente -----------------------
btn_ordenar_ascendente = tk.Button(ventana,text='Ordenar Ascendente',fg='white', bg='green', command=ordenarAscendente)
btn_ordenar_ascendente.pack(pady=5)
#----------------------------- creamos el boton  ordenar descendente -----------------------
btn_ordenar_descendente = tk.Button(ventana,text='Ordenar Descendente',fg='white', bg='green', command=ordenarDescendente)
btn_ordenar_descendente.pack(pady=5)
#----------------------------- creamos el listbox -----------------------
list_box = tk.Listbox(ventana,width=50,height=20 )
list_box.pack(pady=20)
#----------------------------- creamos el label tareas totales -----------------------
label_tarea_totales = tk.Label(ventana,text='Tareas Totales : ')
label_tarea_totales.pack()
#----------------------------- creamos el label tareas realizadas -----------------------
label_tarea_realizada = tk.Label(ventana,text='Tareas Realizadas : ')
label_tarea_realizada.pack()
#----------------------------- creamos el label tareas pendientes -----------------------
label_tarea_pendiente = tk.Label(ventana,text='Tareas Pendientes : ')
label_tarea_pendiente.pack()

#----------------------------- creamos el boton salir -----------------------
btn_salir = tk.Button(ventana,text='Salir',fg='white', bg='blue', command=salir)
btn_salir.pack(pady=20)
#






ventana.mainloop()
