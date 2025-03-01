import tkinter as tk
from tkinter import ttk, messagebox
import requests

# OpenWeatherMap API Key (Apni API Key yahan dalein)
API_KEY = "b0f3c653ebb5b266e4317c466c3ebb23"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# India ke sabhi rajyo ke naam
cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad",
    "Ahmedabad", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur",
    "Indore", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot",
    "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Allahabad"
]

# Function to get weather data
def get_weather():
    city = city_dropdown.get()
    if not city:
        messagebox.showerror("Error", "Please select a city")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("cod") != 200:
        messagebox.showerror("Error", f"City not found: {city}")
        return

    # Extract weather details
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    pressure = data["main"]["pressure"]

    # Update Labels
    weather_label1.config(text=weather)
    desc_label1.config(text=description)
    temp_label1.config(text=f"{temp}°C")
    pressure_label1.config(text=f"{pressure} hPa")

# Tkinter GUI Setup
win = tk.Tk()
win.title("Weather App")
win.geometry("500x550")
win.configure(bg="skyblue")

# Title
title_label = tk.Label(win, text="Python Weather App", font=("Times New Roman", 24, "bold"), bg="skyblue")
title_label.pack(pady=20)

# Dropdown for city selection
city_label = tk.Label(win, text="Select City:", font=("Times New Roman", 18), bg="skyblue")
city_label.pack()

city_dropdown = ttk.Combobox(win, values=cities, font=("Times New Roman", 16))
city_dropdown.pack(pady=5)
city_dropdown.set("Select City")  # Default text

# Button
fetch_button = tk.Button(win, text="Get Weather", font=("Times New Roman", 16, "bold"), command=get_weather)
fetch_button.pack(pady=10)

# Weather Info Labels
weather_label = tk.Label(win, text="Weather:", font=("Times New Roman", 18), bg="skyblue")
weather_label.pack()
weather_label1 = tk.Label(win, text="...", font=("Times New Roman", 18), bg="white")
weather_label1.pack(pady=2)

desc_label = tk.Label(win, text="Description:", font=("Times New Roman", 18), bg="skyblue")
desc_label.pack()
desc_label1 = tk.Label(win, text="...", font=("Times New Roman", 18), bg="white")
desc_label1.pack(pady=2)

temp_label = tk.Label(win, text="Temperature:", font=("Times New Roman", 18), bg="skyblue")
temp_label.pack()
temp_label1 = tk.Label(win, text="...", font=("Times New Roman", 18), bg="white")
temp_label1.pack(pady=2)

pressure_label = tk.Label(win, text="Pressure:", font=("Times New Roman", 18), bg="skyblue")
pressure_label.pack()
pressure_label1 = tk.Label(win, text="...", font=("Times New Roman", 18), bg="white")
pressure_label1.pack(pady=2)

# Run App
win.mainloop()
