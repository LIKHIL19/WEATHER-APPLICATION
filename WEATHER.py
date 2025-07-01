import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.api_key = "16bda0c12b52656d1eb2f703aa3f22d8"
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.root.title("🌤️ Weather Application")
        self.root.geometry("600x800")
        self.root.config(bg="#1e3c72")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"600x800+{x}+{y}")
        
    def create_widgets(self):
        # Create main container with padding
        main_container = tk.Frame(self.root, bg="#1e3c72")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header Section
        self.create_header(main_container)
        
        # Search Section
        self.create_search_section(main_container)
        
        # Weather Display Section
        self.create_weather_section(main_container)
        
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg="#1e3c72")
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        # App title
        title_label = tk.Label(
            header_frame, 
            text="🌤️ Weather Forecast", 
            font=("Arial", 28, "bold"),
            bg="#1e3c72", 
            fg="#ffffff"
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame, 
            text="Get real-time weather information", 
            font=("Arial", 12),
            bg="#1e3c72", 
            fg="#a8c8ec"
        )
        subtitle_label.pack(pady=(5, 0))
        
    def create_search_section(self, parent):
        # Search container with rounded appearance
        search_container = tk.Frame(parent, bg="#2a5298", relief="raised", bd=2)
        search_container.pack(fill=tk.X, pady=(0, 30))
        
        # Inner padding frame
        search_frame = tk.Frame(search_container, bg="#2a5298")
        search_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Search label
        search_label = tk.Label(
            search_frame, 
            text="Select Your City", 
            font=("Arial", 16, "bold"),
            bg="#2a5298", 
            fg="#ffffff"
        )
        search_label.pack(pady=(0, 15))
        
        # Search input frame
        input_frame = tk.Frame(search_frame, bg="#2a5298")
        input_frame.pack(fill=tk.X)
        
        # City selection
        self.city_var = tk.StringVar()
        self.city_list = [
            "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", 
            "Assam", "Bihar", "Chandigarh", "Chhattisgarh", 
            "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa", 
            "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
            "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep",
            "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
            "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab",
            "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", 
            "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ]
        
        self.city_combo = ttk.Combobox(
            input_frame, 
            textvariable=self.city_var,
            values=self.city_list,
            font=("Arial", 14),
            width=25,
            state="readonly"
        )
        self.city_combo.pack(side=tk.LEFT, padx=(0, 15))
        
        # Search button
        self.search_btn = tk.Button(
            input_frame,
            text=" Get Weather",
            command=self.get_weather_data,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.search_btn.pack(side=tk.LEFT)
        
        # Bind Enter key to search
        self.city_combo.bind('<Return>', lambda e: self.get_weather_data())
        
    def create_weather_section(self, parent):
        # Weather container
        self.weather_container = tk.Frame(parent, bg="#ffffff", relief="raised", bd=2)
        self.weather_container.pack(fill=tk.BOTH, expand=True)

        # Initially show welcome message
        self.show_welcome_message()
        
    def show_welcome_message(self):
        welcome_frame = tk.Frame(self.weather_container, bg="#ffffff")
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome icon and text
        welcome_label = tk.Label(
            welcome_frame,
            text="Select a city above to view\nweather information",
            font=("Arial", 16),
            bg="#ffffff",
            fg="#666666",
            justify=tk.CENTER
        )
        welcome_label.pack(expand=True)
        
    def clear_weather_display(self):
        for widget in self.weather_container.winfo_children():
            widget.destroy()
            
    def show_loading(self):
        self.clear_weather_display()
        loading_frame = tk.Frame(self.weather_container, bg="#ffffff")
        loading_frame.pack(fill=tk.BOTH, expand=True)
        
        loading_label = tk.Label(
            loading_frame,
            text="🔄\n\nFetching weather data...",
            font=("Arial", 16),
            bg="#ffffff",
            fg="#666666",
            justify=tk.CENTER
        )
        loading_label.pack(expand=True)
        
        # Update the display
        self.root.update()
        
    def display_weather_data(self, data):
        self.clear_weather_display()
        
        # Main weather frame with padding
        weather_frame = tk.Frame(self.weather_container, bg="#ffffff")
        weather_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Location header
        location_frame = tk.Frame(weather_frame, bg="#ffffff")
        location_frame.pack(fill=tk.X, pady=(0, 25))
        
        city_label = tk.Label(
            location_frame,
            text=f"📍 {data['name']}, {data['sys']['country']}",
            font=("Arial", 20, "bold"),
            bg="#ffffff",
            fg="#1e3c72"
        )
        city_label.pack()
        
        # Current time
        time_label = tk.Label(
            location_frame,
            text=datetime.now().strftime("Updated: %I:%M %p, %B %d"),
            font=("Arial", 10),
            bg="#ffffff",
            fg="#888888"
        )
        time_label.pack(pady=(5, 0))
        
        # Main temperature section
        temp_section = tk.Frame(weather_frame, bg="#f8f9fa", relief="flat", bd=1)
        temp_section.pack(fill=tk.X, pady=(0, 20))
        
        temp_frame = tk.Frame(temp_section, bg="#f8f9fa")
        temp_frame.pack(pady=20)
        
        # Current temperature
        current_temp = round(data['main']['temp'] - 273.15, 1)
        temp_label = tk.Label(
            temp_frame,
            text=f"{current_temp}°C",
            font=("Arial", 48, "bold"),
            bg="#f8f9fa",
            fg="#e74c3c"
        )
        temp_label.pack()
        
        # Weather description
        weather_desc = data['weather'][0]['description'].title()
        desc_label = tk.Label(
            temp_frame,
            text=f"☁️ {weather_desc}",
            font=("Arial", 16),
            bg="#f8f9fa",
            fg="#34495e"
        )
        desc_label.pack(pady=(5, 0))
        
        # Feels like temperature
        feels_like = round(data['main']['feels_like'] - 273.15, 1)
        feels_label = tk.Label(
            temp_frame,
            text=f"Feels like {feels_like}°C",
            font=("Arial", 12),
            bg="#f8f9fa",
            fg="#7f8c8d"
        )
        feels_label.pack()
        
        # Weather details grid
        details_frame = tk.Frame(weather_frame, bg="#ffffff")
        details_frame.pack(fill=tk.X, pady=(10, 0))
        details_frame.pack_propagate(False)
        details_frame.config(height=180)  # Optional fixed height

        
        # Create 2x3 grid of weather details
        details_data = [
            ("💧", "Humidity", f"{data['main']['humidity']}%"),
            ("🌪️", "Pressure", f"{data['main']['pressure']} hPa"),
            ("💨", "Wind Speed", f"{data['wind']['speed']} m/s"),
            ("🌡️", "Min Temp", f"{round(data['main']['temp_min'] - 273.15, 1)}°C"),
            ("🌡️", "Max Temp", f"{round(data['main']['temp_max'] - 273.15, 1)}°C"),
            ("👁️", "Visibility", f"{data.get('visibility', 0)/1000:.1f} km")
        ]
        
        for i, (icon, label, value) in enumerate(details_data):
            row = i // 2
            col = i % 2
            
            detail_card = tk.Frame(details_frame, bg="#ecf0f1", relief="flat", bd=1)
            detail_card.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            
            icon_label = tk.Label(detail_card, text=icon, font=("Arial", 20), bg="#ecf0f1")
            icon_label.pack(pady=(10, 0))
            
            label_widget = tk.Label(detail_card, text=label, font=("Arial", 10), 
                                   bg="#ecf0f1", fg="#7f8c8d")
            label_widget.pack()
            
            value_widget = tk.Label(detail_card, text=value, font=("Arial", 12, "bold"), 
                                   bg="#ecf0f1", fg="#2c3e50")
            value_widget.pack(pady=(0, 10))
        
        # Configure grid weights for responsive design
        details_frame.grid_columnconfigure(0, weight=1)
        details_frame.grid_columnconfigure(1, weight=1)
        
    def show_error(self, message):
        self.clear_weather_display()
        error_frame = tk.Frame(self.weather_container, bg="#ffffff")
        error_frame.pack(fill=tk.BOTH, expand=True)
        
        error_label = tk.Label(
            error_frame,
            text=f"❌\n\n{message}",
            font=("Arial", 16),
            bg="#ffffff",
            fg="#e74c3c",
            justify=tk.CENTER
        )
        error_label.pack(expand=True)
        
    def get_weather_data(self):
        city = self.city_var.get().strip()
        
        if not city:
            messagebox.showwarning("Input Required", "Please select a city!")
            return
            
        # Show loading
        self.show_loading()
        
        try:
            # API call
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get("cod") == 200:
                self.display_weather_data(data)
            else:
                error_msg = data.get("message", "City not found!")
                self.show_error(f"Error: {error_msg}")
                
        except requests.exceptions.Timeout:
            self.show_error("Request timeout. Please check your internet connection.")
        except requests.exceptions.ConnectionError:
            self.show_error("Connection error. Please check your internet connection.")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
