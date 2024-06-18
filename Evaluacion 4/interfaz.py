import tkinter as tk
from tkinter import scrolledtext
import metodos

def ejecutar_accion():
    texto = metodos.main()
    text_area.insert("1.0", texto)

ventana = tk.Tk()
ventana.title("Evaluacion 4")
ventana.configure(background='#aebfbc')  

ventana.geometry("400x350")

text_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
text_area.configure(background='#aebfbc')
text_area.pack(pady=10)

boton = tk.Button(ventana, text="Ejecutar Acción", command=ejecutar_accion,fg="#ebf2f1")
boton.configure(background="#27403b")
boton.pack(pady=5)

label = tk.Label(text='Integrantes \n Jose Olival 30281014 \n  Stalin Salazar 25107117 \n Samir Abder 30334483 \n  Flavio Franchich 30020789 \n Neil Rangel 30638786')
label.configure(background="#aebfbc")
label.pack(pady=1) 

ventana.mainloop()