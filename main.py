import tkinter as tk
from tkinter import messagebox

API_KEY = '41086682a7303f3dfa5d1c44ea2fec98'

def get_weather_button_click():
    city_name = city_entry.get()
    weather_data = get_weather(city_name, API_KEY)

    if weather_data.get("cod") == 200:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        message = f"Temperatura: {temperature}°C\nCondição: {weather_description}"
        messagebox.showinfo("Previsão do Tempo", message)
    else:
        messagebox.showerror("Erro", "Cidade não encontrada. Verifique o nome e tente novamente.")

app = tk.Tk()
app.title("Previsão do Tempo")

city_label = tk.Label(app, text="Digite o nome da cidade:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Obter Previsão", command=get_weather_button_click)
get_weather_button.pack()

app.mainloop()
