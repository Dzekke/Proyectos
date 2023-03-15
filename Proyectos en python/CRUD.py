"""
CREAR UN CRUD 
CON MENU SUPERIOR 
OPCIONES DEL MENU:
OPCION1:

CONECTAR:
CONECTAR Y SALIR 
CONECTAR CREA LA BASE SI NO ESTA CREADA EN CASO CONTRARIO MUESTRA 
UNA EXEPCION DE QUE YA ESTA CREADA

OPCION2:
BORRAR TXTBOX 

OPCION3:
CRUD,SE PUEDE EJECUTAR EL COMANDO DESDE EL MENU O DESDE UNOS BUTTONS DE LA 
PARTE INFERIOR 

OPCION 4 BOTON DE AYUDA Y ACERCA DE 
"""

from tkinter import *
from tkinter import messagebox
import sqlite3


mostrarID=False
raiz=Tk()


 
barraMenu=Menu(raiz)
identificador=StringVar()
nombre=StringVar()
paterno=StringVar()
materno=StringVar()
peso=StringVar()
imc=StringVar()
grasa=StringVar()
musculo=StringVar()
calorias=StringVar()
edad=StringVar()
grasaV=StringVar()

#-------------ConvertVars--------------------------

#Ventanas emergentes
def ventanaEmergente():
	messagebox.showinfo("Registro de peso","App en python de control de peso")

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia")

def finalizarApp():
	valor=messagebox.askquestion("Salir","¿Deseas salir del programa?")
   #valor=messagebox.askokcancel("Salir","¿Deseas salir del programa?")
   #okcancel devuelve True or False
	if valor=="yes":
		#cierra
		raiz.destroy()


#NOTA LA PALABRA RESERVADA REAL==FLOAT
def conectarDB():
	try:
		miConexion=sqlite3.connect("RegistrosPesoKg")
		miCursor=miConexion.cursor()
		miCursor.execute('''
			CREATE TABLE PESO(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PATERNO VARCHAR(20),
			MATERNO VARCHAR(20),
			PESO REAL,
			IMC REAL,
			GRASA REAL,
			MUSCULO REAL,
			CALORIAS INTEGER,
			EDADC INTEGER,
			GRASAV INTEGER)
			''')
		miConexion.close()
		messagebox.showinfo("Base de datos","Base de datos creada con éxito")
		mostrarID=True
	except: #sqlite3.OperationalError
		 messagebox.showwarning("Estado de la base de datos","Conexión en curso ,ya se encuentra conectado a la base de datos")
		 mostrarID=True

#----------ETIQUETA DONDE SE MUESTRA EL ULTIMO IDENTIFICADOR CREADO---------------
tituloID=Label(raiz,text="Ultimo ID")
tituloID.grid(row=0,column=3,sticky="w")
tituloDelID=Label(raiz,text="registrado")
tituloDelID.grid(row=1,column=3,sticky="w")
UltimoID=Label(raiz)
UltimoID.grid(row=2,column=3,sticky="w")

def buscarUltimoID():
	try:
		ultimoIdentificadorCreado=""
		miConexion=sqlite3.connect("RegistrosPesoKg")
		miCursor=miConexion.cursor()
		miCursor.execute("SELECT MAX(ID) FROM PESO")
		ultimoIdentificadorCreado=miCursor.fetchall()
		UltimoID.config(text=ultimoIdentificadorCreado)
		miConexion.close()
	except sqlite3.OperationalError:
		 messagebox.showinfo("Estado de la conexión","Establezca la conexión para Visualizar los datos")

buscarUltimoID()

#-------------------------SQL QUERYS--------------------------
def insertar():
		if  cuadroID.get()!="":
				identificador.set("")
		
		if (nombres.get()=="" or apellidopa.get()=="" or apellidoma.get()=="" or
		   cuadroPeso.get()=="" or 	cuadroIMC.get()=="" or cuadroGrasa.get()=="" or
		   cuadroMusculo.get()=="" or cuadroCalorias.get()=="" or cuadroEdadC.get()=="" or
		   cuadroGrasaV.get()==""):
		   messagebox.showinfo("Acción invalida","Campos en blanco , compruebe los datos")
		   permitirInsert=False
		else:
			permitirInsert=True
			try:
				pesoConvert = float(cuadroPeso.get())
			except ValueError:

				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de peso debe ser decimal.")    
			
			try:
				
				imcConvert=float(cuadroIMC.get())
			
			except ValueError:
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de IMC debe ser decimal.")

			try:
				
				grasaConvert=float(cuadroGrasa.get())
			except ValueError:
				
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de debe ser decimal.")
			
			try:
				
				musculoConvert=float(cuadroMusculo.get())
			except ValueError:
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de debe ser decimal.")
		    
		
			try:
				caloriasConvert=int(cuadroCalorias.get())
			except ValueError:
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de calorias no es un número válido.")
			
			try:
				edadConvert=int(cuadroEdadC.get())
			except ValueError:
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de edad no es un número válido.")
			
			try:
				grasaVConvert=int(cuadroGrasaV.get())
			except ValueError:
				messagebox.showinfo("Error verifique el formato","El valor ingresado en el campo de grasa no es un número válido.")

		if permitirInsert==True:
			try:
				miConexion=sqlite3.connect("RegistrosPesoKg")
				miCursor=miConexion.cursor()
				"""(nombres.get(),apellidopa.get(),apellidoma.get(),float(cuadroPeso.get()),float(cuadroIMC.get()),
				float(cuadroGrasa.get()),float(cuadroMusculo.get()),int(cuadroCalorias.get()),int(cuadroEdadC.get()),int(cuadroGrasaV.get())))"""
				datos=nombres.get(),apellidopa.get(),apellidoma.get(),cuadroPeso.get(),cuadroIMC.get(),cuadroGrasa.get(),cuadroMusculo.get(),cuadroCalorias.get(),cuadroEdadC.get(),cuadroGrasaV.get()
				miCursor.execute("INSERT INTO PESO(ID,NOMBRE,PATERNO,MATERNO,PESO,IMC,GRASA,MUSCULO,CALORIAS,EDADC,GRASAV) VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(datos))
				messagebox.showinfo("Alta de usuarios","Usuario registrado con éxito")
				miConexion.commit()
				miConexion.close()
				buscarUltimoID()
				limpiarCuadros()
			except:
				messagebox.showwarning("Error!!","Verifique la conexión a la base de datos")
			#miConexion.commit()

def leer():
	if cuadroID.get()=="":
		messagebox.showinfo("Error!","Ingrese un identificador a buscar")
	else:
		try:
			miConexion=sqlite3.connect("RegistrosPesoKg")
			miCursor=miConexion.cursor()
			#miCursor.execute("SELECT * FROM PESO WHERE ID = ?", (int(cuadroID.get()),))
			miCursor.execute("SELECT * FROM PESO WHERE ID = " + cuadroID.get())
			consulta=miCursor.fetchall() #retorna todas las filas como una lista de tuplas  

			#print(variosRegistros)

			for datos in consulta:
				nombre.set(datos[1])
				paterno.set(datos[2])
				materno.set(datos[3])
				peso.set(datos[4])
				imc.set(datos[5])
				grasa.set(datos[6])
				musculo.set(datos[7])
				calorias.set(datos[8])
				edad.set(datos[9])
				grasaV.set(datos[10])
			miConexion.commit()
			miConexion.close()
			blockIDentry()
		except:
			messagebox.showwarning("Error!!","Verifique la conexión a la base de datos")

#nombres.get(),apellidopa.get(),apellidoma.get(),float(cuadroPeso.get()),float(cuadroIMC.get()),float(cuadroGrasa.get()),float(cuadroMusculo.get()),int(cuadroCalorias.get()),int(cuadroEdadC.get()),int(cuadroGrasaV.get()))
#miCursor.execute("UPDATE PESO SET NOMBRE=nombres.get(),PATERNO=apellidopa.get(),MATERNO=apellidoma.get(),PESO=float(cuadroPeso.get()),IMC=float(cuadroIMC.get()),GRASA=float(cuadroGrasa.get()),MUSCULO=float(cuadroMusculo.get()),CALORIAS=int(cuadroCalorias.get()),EDADC=int(cuadroEdadC.get()),GRASAV=int(cuadroGrasaV.get())  WHERE ID = ?", (int(cuadroID.get()),))

def actualizar():
		
		if (cuadroID.get()=="" or nombres.get()=="" or apellidopa.get()=="" or apellidoma.get()=="" or
		   cuadroPeso.get()=="" or 	cuadroIMC.get()=="" or cuadroGrasa.get()=="" or
		   cuadroMusculo.get()=="" or cuadroCalorias.get()=="" or cuadroEdadC.get()=="" or
		   cuadroGrasaV.get()==""):
		   messagebox.showinfo("Error!","Visualize los datos del usuario a actualizar")
		else:
			respuesta=messagebox.askquestion("Actualización de datos","¿Desea actualizar los datos de forma permanente?")
			if respuesta=="yes":
				try:
					miConexion=sqlite3.connect("RegistrosPesoKg")
					miCursor=miConexion.cursor()
					datos=nombres.get(),apellidopa.get(),apellidoma.get(),cuadroPeso.get(),cuadroIMC.get(),cuadroGrasa.get(),cuadroMusculo.get(),cuadroCalorias.get(),cuadroEdadC.get(),cuadroGrasaV.get()
					miCursor.execute("UPDATE PESO  SET NOMBRE=?,PATERNO=?,MATERNO=?,PESO=?,IMC=?,GRASA=?,MUSCULO=?,CALORIAS=?,EDADC=?,GRASAV=?" +
					"WHERE ID = " + cuadroID.get(),(datos))
					messagebox.showinfo("Datos del usuario","Datos actualizados con éxito")
					miConexion.commit()
					miConexion.close()
					limpiarCuadros()
					unblockIDentry()
				except:
					messagebox.showwarning("Estado de la conexión","Verifique la conexión a la base de datos")

def borrar():
	if (cuadroID.get()=="" or nombres.get()=="" or apellidopa.get()=="" or apellidoma.get()=="" or
		cuadroPeso.get()=="" or	cuadroIMC.get()=="" or cuadroGrasa.get()=="" or
	    cuadroMusculo.get()=="" or cuadroCalorias.get()=="" or cuadroEdadC.get()=="" or
	    cuadroGrasaV.get()==""):
			messagebox.showinfo("Error!","Visualize los datos del usuario a eliminar")
	else:
		respuesta=messagebox.askquestion("Eliminación de datos","¿Desea eleiminar los datos de forma permanente?")
		if respuesta=="yes":
			try:
				miConexion=sqlite3.connect("RegistrosPesoKg")
				miCursor=miConexion.cursor()
				miCursor.execute("DELETE FROM PESO WHERE ID= " + cuadroID.get())
				miConexion.commit()
				limpiarCuadros()
				messagebox.showinfo("Eliminar","Datos eliminados")
				unblockIDentry()
				buscarUltimoID()
			except:
				messagebox.showwarning("Estado de la conexión","Verifique la conexión a la base de datos")
def limpiarCuadros():
	cuadroID.delete(0,END)
	nombres.delete(0,END)
	apellidopa.delete(0,END)
	apellidoma.delete(0,END)
	cuadroPeso.delete(0,END)
	cuadroIMC.delete(0,END)
	cuadroGrasa.delete(0,END)
	cuadroMusculo.delete(0,END)
	cuadroCalorias.delete(0,END)
	cuadroEdadC.delete(0,END)
	cuadroGrasaV.delete(0,END)
	unblockIDentry()

raiz.config(menu=barraMenu,width=250,height=300)
#-------------encabezado 1 del menu--------------
ConectarMenu=Menu(barraMenu,tearoff=0)
#------------SubMenuConection---------------------
ConectarMenu.add_command(label="Conectar",command=conectarDB)
ConectarMenu.add_separator()
ConectarMenu.add_command(label="Salir",command=finalizarApp)

#------------encabezado 2 del menu-------------
BorrarMenu=Menu(barraMenu,tearoff=0)
#------------SubMenuBorrar---------------------
BorrarMenu.add_command(label="Limpiar campos",command=limpiarCuadros)
#----------encabezado 3 del menu-------------
CRUDMenu=Menu(barraMenu,tearoff=0)
#------------SubMenuCRUD---------------------
CRUDMenu.add_command(label="Nuevo",command=insertar)
CRUDMenu.add_command(label="Visualizar",command=leer)
CRUDMenu.add_command(label="Actualizar",command=actualizar)
CRUDMenu.add_command(label="Borrar",command=borrar)
#--------------encabezado 4 del menu---------
AyudaMenu=Menu(barraMenu,tearoff=0)
AyudaMenu.add_command(label="Ayuda",command=ventanaEmergente)
AyudaMenu.add_command(label="Acerca de....",command=avisoLicencia)
#------------SubMenuAyuda---------------------

barraMenu.add_cascade(label="BBDD",menu=ConectarMenu)#opcion 1 del menu
barraMenu.add_cascade(label="Limpiar",menu=BorrarMenu)#opcion 2 del menu
barraMenu.add_cascade(label="CRUD",menu=CRUDMenu)#opcion 3 del menu
barraMenu.add_cascade(label="Ayuda",menu=AyudaMenu)#opcion 4 del menu



#----------------------------TXTBOXES------------------------------

#cuadro de texto
cuadroID=Entry(raiz,textvariable=identificador)#auto
cuadroID.grid(row=0,column=1,padx=10,pady=10)
nombres=Entry(raiz,textvariable=nombre)
nombres.grid(row=1,column=1,padx=10,pady=10)
apellidopa=Entry(raiz,textvariable=paterno)
apellidopa.grid(row=2,column=1,padx=10,pady=10	) 
apellidoma=Entry(raiz,textvariable=materno)
apellidoma.grid(row=3,column=1,padx=10,pady=10) 
cuadroPeso=Entry(raiz,textvariable=peso)
cuadroPeso.grid(row=4,column=1,padx=10,pady=10)
cuadroIMC=Entry(raiz,textvariable=imc)
cuadroIMC.grid(row=5,column=1,padx=10,pady=10)
cuadroGrasa=Entry(raiz,textvariable=grasa)
cuadroGrasa.grid(row=6,column=1,padx=10,pady=10)
cuadroMusculo=Entry(raiz,textvariable=musculo)
cuadroMusculo.grid(row=7,column=1,padx=10,pady=10)
cuadroMusculo.config(justify="center",fg="blue")
cuadroCalorias=Entry(raiz,textvariable=calorias)
cuadroCalorias.grid(row=8,column=1,padx=10,pady=10)
cuadroEdadC=Entry(raiz,textvariable=edad)
cuadroEdadC.grid(row=9,column=1,padx=10,pady=10)
cuadroGrasaV=Entry(raiz,textvariable=grasaV)
cuadroGrasaV.grid(row=10,column=1,padx=10,pady=10)


#---------------Deshabilitar entry ------------

def blockIDentry():
	cuadroID.config(state="disabled")

def unblockIDentry():
	cuadroID.config(state="normal")


#-----------------------Labels----------------------------------

#Labels
IDLabel=Label(raiz,text="ID")
IDLabel.grid(row=0,column=0,sticky="w",padx=10,pady=10)
nombreLabel=Label(raiz,text="Nombre(s)")
nombreLabel.grid(row=1,column=0,sticky="w",padx=10,pady=10)
paternoLabel=Label(raiz,text="Paterno")
paternoLabel.grid(row=2,column=0,sticky="w",padx=10,pady=10)
maternoLabel=Label(raiz,text="Materno")
maternoLabel.grid(row=3,column=0,sticky="w",padx=10,pady=10)
pesoLabel=Label(raiz,text="Peso")
pesoLabel.grid(row=4,column=0,sticky="w",padx=10,pady=10) 
IMCLabel=Label(raiz,text="IMC")
IMCLabel.grid(row=5,column=0,sticky="w",padx=10,pady=10)
grasaLabel=Label(raiz,text="Grasa")
grasaLabel.grid(row=6,column=0,sticky="w",padx=10,pady=10)
musculoLabel=Label(raiz,text="Musculo")
musculoLabel.grid(row=7,column=0,sticky="w",padx=10,pady=10)
caloriasLabel=Label(raiz,text="Calorias")
caloriasLabel.grid(row=8,column=0,sticky="w",padx=10,pady=10)
edadLabel=Label(raiz,text="Edad corporal")
edadLabel.grid(row=9,column=0,sticky="w",padx=10,pady=10)
grasaLabel=Label(raiz,text="Grasa")
grasaLabel.grid(row=10,column=0,sticky="w",padx=10,pady=10)

#-------------------------------botones------------------------

botonC=Button(raiz,widt=7,height=2,text="Crear",command=insertar)
botonC.grid(row=12,column=0,sticky="e",padx=10,pady=10)

botonR=Button(raiz,widt=7,height=2,text="Visualizar",command=leer)
botonR.grid(row=12,column=1,sticky="e",padx=10,pady=10)

botonU=Button(raiz,widt=7,height=2,text="Actualizar",command=actualizar)
botonU.grid(row=12,column=2,sticky="e",padx=10,pady=10)

botonD=Button(raiz,widt=7,height=2,text="Borrar",command=borrar)
botonD.grid(row=12,column=3,sticky="e",padx=10,pady=10)








raiz.mainloop()