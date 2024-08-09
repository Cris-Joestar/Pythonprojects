
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
victorias_usuario = 0
victorias_computadora = 0
ronda = 0  

def iniciar_juego():
    global victorias_usuario, victorias_computadora, ronda
    victorias_usuario = 0
    victorias_computadora = 0
    ronda = 0
    resultado_label.config(text='')
    actualizar_victorias()

def jugar():
    global victorias_usuario, victorias_computadora, ronda
    if ronda < 3:
        usuario = seleccion_usuario.get().lower()
        computadora = random.choice(['piedra', 'papel', 'tijera'])
        resultado = ""
        if usuario == computadora:
            resultado = 'Empate'
        
        elif gana_usuario(usuario, computadora):
            resultado = 'Ganaste! Bien hecho'
            victorias_usuario += 1
        else:
            resultado = 'Perdiste :('
            victorias_computadora += 1
        resultado_label.config(text=f'La computadora saca {computadora} \nRonda {ronda + 1}: {resultado}')

        actualizar_victorias()

        ronda += 1
        if ronda == 3:
            finalizar_juego()


def gana_usuario(usuario, computadora):
    if usuario == 'piedra' and computadora == 'tijera':
        return True
    elif usuario == 'papel' and computadora == 'piedra':
        return True
    elif usuario == 'tijera' and computadora == 'papel':
        return True
    else:
        return False
    
def actualizar_victorias():
    victorias_usuario_label.config(text=f'El número de victorias que tienes es: {victorias_usuario}')
    victorias_computadora_label.config(text=f'El número de victorias de la computadora es: {victorias_computadora}')
    
def finalizar_juego():
    mensaje = ""
    if victorias_usuario > victorias_computadora:
        mensaje = 'Ganaste el juego!!!!!!!'
    elif victorias_computadora > victorias_usuario:
        mensaje = 'Ganó la computadora :|'
    else:
        mensaje = 'Es un empate :O'
    
    messagebox.showinfo('Fin del juego', mensaje)
    iniciar_juego()

def instrucciones():
    instruccion = """
                  El juego consta de 3 rondas tienes que escoger
                  Piedra, Papel o Tijera
                  si ganas más que la 
                  computadora ganarás el juego
                  Buena suerte :)!
                  """
    messagebox.showinfo('Instrucciones', instruccion)

# Configuracion de la interfaz gráfica

root = tk.Tk()
root.title('Piedra, Papel o Tijera')
root.geometry('600x400')

# Colores y fuentes
bg_color = '#00913f'
fg_color = '#333333'
font = ('Arial', 12, 'bold')

root.configure(bg=bg_color)

# Variable para guardar la seleccion del usuario
seleccion_usuario = tk.StringVar(value='piedra')

# Labels para mostrar los resultados y las victorias
resultado_label = tk.Label(root, text='', bg='#FFD300', font=font, fg=fg_color)
resultado_label.pack(pady=10)

victorias_usuario_label = tk.Label(root, text='Victorias del usuario: 0',bg='orange', font=font, fg='blue')
victorias_usuario_label.pack()

victorias_computadora_label = tk.Label(root, text='Victorias de la computadora: 0',bg='orange', font=font, fg='blue')
victorias_computadora_label.pack()

# Botones para escoger una opción ( Piedra, Papel o Tijera )

imagen_piedra = ImageTk.PhotoImage(Image.open(r'C:\Users\CRISTIAN\Documents\Documents\CV\Proyectos\Pythonprojects\Piedra papel o tijera\Imagenes\Piedra.jpg').resize((50, 50)))
imagen_papel = ImageTk.PhotoImage(Image.open(r'C:\Users\CRISTIAN\Documents\Documents\CV\Proyectos\Pythonprojects\Piedra papel o tijera\Imagenes\Papel.jpg').resize((50, 50)))
imagen_tijera = ImageTk.PhotoImage(Image.open(r'C:\Users\CRISTIAN\Documents\Documents\CV\Proyectos\Pythonprojects\Piedra papel o tijera\Imagenes\Tijera.jpg').resize((50, 50)))



frame_opciones = tk.Frame(root, bg=bg_color)
frame_opciones.pack(pady=20)

boton_piedra = tk.Radiobutton(frame_opciones, text='Piedra', variable=seleccion_usuario, value='piedra', image=imagen_piedra)
boton_piedra.grid(row=0, column=0, padx=10)

boton_papel = tk.Radiobutton(frame_opciones, text='Papel', variable=seleccion_usuario, value='papel', image=imagen_papel)
boton_papel.grid(row=0, column=1, padx=10)

boton_tijera = tk.Radiobutton(frame_opciones, text='Tijera', variable=seleccion_usuario, value='tijera', image=imagen_tijera)
boton_tijera.grid(row=0, column=2, padx=0)

# Frame para los botones de jugar y reiniciar
frame_botones = tk.Frame(root, bg=bg_color)
frame_botones.pack(pady=20)

#Boton para leer las instrucciones
boton_instrucciones = tk.Button(frame_botones, text='Instrucciones', command=instrucciones, background='blue', fg='white', font=font)
boton_instrucciones.grid(row=0, column=0, padx=10)

# Boton para iniciar el juego
boton_jugar = tk.Button(frame_botones, text='Jugar', command=jugar, background='red', fg='white', font=font)
boton_jugar.grid(row=0, column=1, padx=10)

# Boton reiniciar el juego

boton_reiniciar = tk.Button(frame_botones, text='Reiniciar', command=iniciar_juego, background='brown', fg='white', font=font)
boton_reiniciar.grid(row=0, column=2, padx=10)
root.mainloop()