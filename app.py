import tkinter as tk
from tkinter import ttk, Text

def button_clicked():
    print('Button clicked')


root = tk.Tk()
root.title("JdseEdit-py-tkinter")

#message = tk.Label(root, text="Hello")
#message.pack()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo')

window_width = 300
window_height = 200
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#root.iconbitmap("./JdseEdit.ico")
# above didn't work, "bitmap "./JdseEdit.ico" not defined"

# leaving commented out to figure out what to do with the png file
#root.iconphoto(False, tk.PhotoImage(file='JdseEdit.png'))

root.mainloop()