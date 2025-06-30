import tkinter as tk
from tkinter import ttk
import requests

def data_get():
    city= city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=16bda0c12b52656d1eb2f703aa3f22d8").json()
    

root = tk.Tk()
root.title("🌤️ WEATHER APPLICATION")
root.geometry("500x500")
root.config(bg="#2657a0")
#Label for asking to enter the city name 
label_city_name= tk.Label(root, text="Enter your city name", font =("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#00008b")
label_city_name.pack(pady=20)

# Frame for search functionality
search_frame = tk.Frame(root, bg="#2657a0")
search_frame.pack(fill=tk.BOTH, expand=True)

#Creating a combo box
city_name = tk.StringVar()
# List of Indian states and union territories for the combo box
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(search_frame, font=("Helvetica", 16), width=20, values=list_names, textvariable=city_name)
com.grid(row=0, column=0, padx=20, pady=20)

#search button
def search_fnc():
    pass
search_button = ttk.Button(search_frame, text="Search", command= search_fnc, width= 15 )
search_button.grid(row=0, column=1, padx=20, pady=20)
#weather information display
label_city_name= tk.Label(root, text="Weather", font =("Times New Roman", 20, "bold"), bg="#f0f8ff", fg="#00008b")
label_city_name.pack(pady=20)

root.mainloop()
