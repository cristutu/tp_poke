import requests  # Importa la biblioteca 'requests' para realizar solicitudes HTTP.
import tkinter as tk  # Importa la biblioteca 'tkinter' para la interfaz gráfica.

class Pokemon:
    def __init__(self, vent):
        # Inicializa la ventana principal con un título y un tamaño específico.
        self.vent = vent
        self.vent.title("Consulta de Pokémon")
        self.vent.geometry("300x300")

        # Crea una etiqueta para solicitar al usuario que ingrese el número del Pokémon.
        self.etiqueta = tk.Label(vent, text="Ingrese el número del Pokémon:")
        self.etiqueta.pack()

        # Crea un campo de entrada para que el usuario ingrese el número del Pokémon.
        self.entrada = tk.Entry(vent)
        self.entrada.pack()

        # Crea un botón que, al hacer clic en él, llamará al método 'obtener_info'.
        self.boton_obtener = tk.Button(vent, text="Obtener información", command=self.obtener_info)
        self.boton_obtener.pack()

        # Crea una etiqueta para mostrar la información del Pokémon obtenida de la API.
        self.informacion_pokemon = tk.Label(vent, text="")
        self.informacion_pokemon.pack()

    def obtener_info(self):
        # Obtiene el número del Pokémon ingresado por el usuario.
        numero_pokemon = self.entrada.get()
        # Construye la URL de la API usando el número del Pokémon.
        url = f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon}"
        # Realiza una solicitud GET a la API de Pokémon.
        respuesta = requests.get(url)

        # Comprueba si la solicitud fue exitosa (código de estado 200).
        if respuesta.status_code == 200:
            # Convierte la respuesta JSON en un diccionario de Python.
            datos_pokemon = respuesta.json()
            # Formatea los datos del Pokémon llamando al método 'datos_poke'.
            info = self.datos_poke(datos_pokemon)
            # Muestra la información del Pokémon llamando al método 'mostrar_informacion'.
            self.mostrar_informacion(info)
        else:
            # Imprime un mensaje de error si la solicitud no fue exitosa.
            print("Error al obtener información del Pokémon.")

    def datos_poke(self, datos_pokemon):
        # Extrae datos específicos del Pokémon como nombre, tipos, habilidades y estadísticas.
        nombre = datos_pokemon['name']
        tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]
        habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in datos_pokemon['stats']}

        # Formatea la información del Pokémon en una cadena de texto estructurada.
        info = f"Nombre: {nombre}\nTipos: {', '.join(tipos)}\nHabilidades: {', '.join(habilidades)}\n\nEstadísticas:\n"
        for stat, valor in stats.items():
            info += f"{stat.capitalize()}: {valor}\n"

        return info

    def mostrar_informacion(self, info):
        # Actualiza la etiqueta 'informacion_pokemon' en la interfaz con la información del Pokémon.
        self.informacion_pokemon.config(text=info)

# Crea la ventana principal de la aplicación.
root = tk.Tk()
app = Pokemon(root)
root.mainloop()