from palabras import palabras
import random
import string 
from diagrama_ahorcado import visualizacion_vidas
import tkinter as tk
from tkinter import messagebox

class AhorcadoApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Juego del Ahorcado')
        self.font = ('Helvetica', 20, 'bold')

        self.menu = tk.Menu(self.root)

        self.root.config(menu = self.menu)

        self.juego_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Juego', menu=self.juego_menu)
        self.juego_menu.add_command(label='Reiniciar', command=self.reiniciar_juego)
        
        self.iniciar_juego()

    def iniciar_juego(self):
        self.palabra = obtener_palabra(palabras)
        self.palabra_oculta = ['_']*len(self.palabra)
        self.vidas = 7

        self.palabra_label = tk.Label(self.root, text=' '.join(self.palabra_oculta), font=self.font, bg='yellow')
        self.palabra_label.pack(pady=20)

        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        self.letra_entry = tk.Entry(self.frame_entrada,font=self.font)
        self.letra_entry.grid(row=0, column=0, padx=10)

        self.adivinar_btn = tk.Button(self.frame_entrada, font=self.font, text='Adivinar', command=self.adivinar_letra, bg='red')
        self.adivinar_btn.grid(row=0, column=1, padx=10)

        self.dibujo_canvas = tk.Canvas(self.root, width=300, height=300)
        self.dibujo_canvas.pack(pady=20)
        self.actualizar_dibujo()  

    def adivinar_letra(self):
        if self.vidas >=0: 
            letra = self.letra_entry.get().upper()
            self.letra_entry.delete(0, tk.END)

            if letra in self.palabra:
                for i, l in enumerate(self.palabra):
                    if l == letra:
                        self.palabra_oculta[i] = letra
                self.palabra_label.config(text="".join(self.palabra_oculta))
            else:
                self.vidas -=1
                self.actualizar_dibujo()

            if self.vidas ==0:
                messagebox.showinfo('Juego terminado', f'Has perdido :(!, la palabra era {self.palabra}')
                self.reiniciar_juego()

            elif "_" not in self.palabra_oculta:
                messagebox.showinfo('Juego terminado', f'Felicidades has ganado el juego, adivinaste la palabra {self.palabra}')

    def actualizar_dibujo(self):
        self.dibujo_canvas.delete('all')
        dibujo = visualizacion_vidas[self.vidas]
        self.dibujo_canvas.create_text(150, 150, text=dibujo, font=('Courier', 14), anchor=tk.CENTER)

    def reiniciar_juego(self):
        self.palabra_label.destroy()
        self.frame_entrada.destroy()
        self.dibujo_canvas.destroy()

        self.iniciar_juego()

    



def obtener_palabra(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


if __name__ == "__main__":
    root = tk.Tk()
    app = AhorcadoApp(root)
    root.mainloop()

        








