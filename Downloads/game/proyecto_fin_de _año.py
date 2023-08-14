import tkinter as tk
import random
from PIL import ImageTk

class PreguntadosGame:
    def __init__(self, vent):
         # Lista de preguntas, cada pregunta es un diccionario con "question", "options" y "answer"]    
        self.pregunta = []
            

        self.current_pregunta_index = -1
        self.correct_respuesta = 0
        self.total_pregunta = len(self.pregunta)

        self.pregunta_label = tk.Label(vent, text="", font=("Helvetica", 16))
        self.pregunta_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(vent, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            button.pack(fill=tk.BOTH, padx=10, pady=5)
            self.option_buttons.append(button)

        self.next_pregunta()

    def next_pregunta(self):
        self.current_pregunta_index += 1
        if self.current_pregunta_index < self.total_pregunta:
            self.current_pregunta = self.pregunta[self.current_pregunta_index]
            self.pregunta_label.config(text=self.current_pregunta["pregunta"])

            random.shuffle(self.current_pregunta["options"])   #devuelve la secuencia x pasada como argumento desordenada.
            for i in range(4):
                self.option_buttons[i].config(text=self.current_pregunta["options"][i])

    def check_answer(self, selected_option):
        if selected_option == self.current_pregunta["answer"]:
            self.correct_respuesta += 1
            print("¡Respuesta correcta!")
        else:
            print("Respuesta incorrecta. La respuesta correcta es:", self.current_pregunta["options"][self.current_pregunta["answer"]])

        self.next_pregunta()

vent = tk.Tk()
vent = vent
vent.title("MundiPreguntas")
vent.geometry("300x200")
game = PreguntadosGame(vent)

def mostrar_imagen():

    img = tk.PhotoImage(file = "img/binomo.png")
    img = tk.Label(vent,image = img)
    img.pack()
    
vent.mainloop()