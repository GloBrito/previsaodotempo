import requests
import tkinter as tk
from tkinter import messagebox

api_key = '41086682a7303f3dfa5d1c44ea2fec98'

def get_weather(city_name, api_key):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Para obter a temperatura em Celsius
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_weather_button_click():
    city_name = city_entry.get()
    weather_data = get_weather(city_name, api_key)

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
