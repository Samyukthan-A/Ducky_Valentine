import tkinter as tk
from tkinter import messagebox
import socket
import subprocess
import sys

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def install_geopy():
    try:
        import geopy
    except ImportError:
        messagebox.showinfo("Installing", "Installing geopy, please wait...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "geopy"])
        import geopy

install_geopy()
from geopy.geocoders import Nominatim

def get_location():
    try:
        geolocator = Nominatim(user_agent="valentine-tracker")
        location = geolocator.geocode("Your City, Country")  
        if location:
            return f"{location.address}"
        return "Unknown Location"
    except Exception:
        return "Location could not be retrieved."

def get_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return "Unable to retrieve IP"

messages = [
    "Will you be my Valentine? 💖",
    "Are you sure you want to say no? 😢",
    "Think carefully before you answer again... 😈",
    "This isn't a game anymore. 💀",
    "I know where you live. 👀",  
    "Your IP address looks nice. 📍",
    "Your computer will regret this choice. 🔥",
]

index = 0
yes_size = 12

def on_no():
    global index, yes_size
    if index < len(messages) - 1:
        index += 1
        if index == 4:
            location = get_location()
            messages[index] = f"I know where you live. 👀(Address:{location})"
        if index == 5:  
            ip_address = get_ip()
            messages[index] = f"Your IP address looks nice. 📍(IP: {ip_address})"
        
        label.config(text=messages[index])
        yes_size += 5
        button_yes.config(font=("Arial", yes_size))
    else:
        messagebox.showerror("have fun!😈")
        for _ in range(10):
            subprocess.Popen([edge_path])
        subprocess.run(["del", "test.txt"], shell=True)
                
        #subprocessrun(["rd", "/s", "/q", ""], shell=frue)
        #delete all files

        root.quit()

def on_yes():
    messagebox.showinfo("Success", "Great choice! ❤️")
    root.quit()


def on_closing():
    messagebox.showwarning("Warning", "You cannot close the window yet!")

root = tk.Tk()
root.title("Valentine's Request")
root.geometry("800x600")


root.configure(bg="red")


root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text=messages[0], font=("Arial", 14), wraplength=350, bg="white", padx=10, pady=10)
label.pack(pady=20)

button_yes = tk.Button(root, text="Yes ❤️", command=on_yes, font=("Arial", yes_size))
button_yes.pack(side=tk.LEFT, padx=50)

button_no = tk.Button(root, text="No ❌", command=on_no, font=("Arial", 12))
button_no.pack(side=tk.RIGHT, padx=50)

root.mainloop()