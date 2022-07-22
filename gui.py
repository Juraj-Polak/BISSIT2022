# Imports
import tkinter as tk
from turtle import window_height, window_width
from PIL import ImageTk, Image
import fr_modul

# Main window
main = tk.Tk()
main.title('Attendance manager')
main.resizable(0,0)
main.configure(bg='white')
main.iconbitmap('./assets/icon.ico')

# Centering window at screen
# Set window dimensions
window_width = 700
window_height = 400

# Get screen dimensions
screen_width = main.winfo_screenwidth()
screen_hight = main.winfo_screenheight()

# Find screen center
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_hight/2 - window_height/2) - 90

main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Logo
logo_frame = tk.Frame(main, width=200, height=200)
logo_frame.pack()
logo_frame.place(anchor='center', relx=0.5, rely=0.2)

logo = ImageTk.PhotoImage(Image.open('./assets/logo.png'))

logo_label = tk.Label(logo_frame, image = logo)
logo_label.pack()

# Buttons
webcam = tk.Button(main, font='arial', text='Webcam input', command=fr_modul.video_detection).place(relx=0.075, rely=0.53, relheight=0.2, relwidth=0.35)
file = tk.Button(main, font='arial', text='File input').place(relx=0.575, rely=0.53, relheight=0.2, relwidth=0.35)
help = tk.Button(main, font='arial', text='Help').place(relx=0.425, rely=0.78, relheight=0.12, relwidth=0.15)

main.mainloop()