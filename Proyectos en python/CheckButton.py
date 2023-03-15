from tkinter import *

raiz=Tk()
anime=IntVar()
serie=IntVar()
pelis=IntVar()


def pasatiempoSeleccionado():
	opcionSeleccionada=" "

	if anime.get()==1:
		opcionSeleccionada+="Animes "
	if serie.get()==1:
		opcionSeleccionada+="Series "
	if pelis.get()==1:
		opcionSeleccionada+="peliculas "

	seleccionado.config(text=opcionSeleccionada)



foto=PhotoImage(file="entretenimiento.png")
Label(raiz,image=foto).pack()

frame=Frame(raiz)
frame.pack()

Label(frame,text="Elige tu pasatiempo",width=50).pack()

Checkbutton(frame,text="Animes",variable=anime,onvalue=1,offvalue=0,command=pasatiempoSeleccionado).pack()
Checkbutton(frame,text="Series",variable=serie,onvalue=1,offvalue=0,command=pasatiempoSeleccionado).pack()
Checkbutton(frame,text="Peliculas",variable=pelis,onvalue=1,offvalue=0,command=pasatiempoSeleccionado).pack()

seleccionado=Label(frame)
seleccionado.pack()



raiz.mainloop()  