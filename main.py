import tkinter as tk
from tkinter import messagebox,ttk
import json as js
import set_up

window = set_up.Set_up()
window.create_labels()
window.adding_canvas()
window.create_buttons()
window.create_entry()
window.website_entry.focus()

window.window_loop()