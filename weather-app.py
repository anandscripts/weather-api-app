
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def weather_info(name):
    api_key = "4bcb0fa521bbabf1f76493a45a1891b8"

    url = "https://api.openweathermap.org/data/2.5/weather?q="

    link = url+name+"&appid="+api_key+"&units=metric"
    response = requests.get(link)

    if response.status_code == 200:
        output = response.json()
        return output
    else:
        messagebox.showerror('Error! Enter the Correct City or Try Again after sometime')
        return None

def result():
    name = city_name.get()
    info = weather_info(name)
    if info is None:
        return
    
    icon_id = info['weather'][0]['icon']
    temperature = info['main']['temp']
    windspeed = info['wind']['speed']
    description = info['weather'][0]['description']

    icon_link = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"

    city.configure(text=name)
    image = Image.open(requests.get(icon_link, stream=True).raw)
    icon_img = ImageTk.PhotoImage(image)
    icon.configure(image=icon_img)
    icon.image = icon_img

    temp.configure(text=f"Temperature: {temperature}°C")
    wind.configure(text=f"Wind Speed: {windspeed}m/s")
    desc.configure(text=f"Description: {description}")
    

root = ttkbootstrap.Window(themename="morph") 
root.title("Weather App")
root.geometry("500x500")

city_name = ttkbootstrap.Entry(root, font="Helvetica, 18") 
city_name.pack(pady=10)

search_b = ttkbootstrap.Button(root, text='Search', command=result, bootstyle="warning")
search_b.pack(pady=10)

city = tk.Label(root,font="Helvetica, 18")
city.pack(pady=20)

icon = tk.Label(root)
icon.pack()

temp = tk.Label(root,font="Helvetica, 17")
temp.pack()

wind = tk.Label(root,font="Helvetica, 17")
wind.pack()

desc = tk.Label(root,font="Helvetica, 16")
desc.pack()

root.mainloop()
