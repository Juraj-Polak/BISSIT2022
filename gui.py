# Imports
import tkinter as tk
from turtle import window_height, window_width
# import fr_modul


main = tk.Tk()
main.title('Gangsta attendance manager')

# Centering window at screen
# Set window dimensions
window_width = 700
window_height = 400

# Get screen dimensions
screen_width = main.winfo_screenwidth()
screen_hight = main.winfo_screenheight()

# Find screen center
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_hight/2 - window_height/2)

main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

main.resizable(0,0)

webcam = tk.Button(main, font='arial', text='Webcam input').place(relx=0.07, rely=0.5, relheight=0.2, relwidth=0.35)
file = tk.Button(main, font= 'arial', text='File input').place(relx=0.57, rely=0.5, relheight=0.2, relwidth=0.35)

main.mainloop()