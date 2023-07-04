import tkinter as tk
import webbrowser as wb
name = tk.Tk(className="search movies and series")
n = tk.Label(name, text="Enter movie or series name: ", font=("Times New Roman", 15))
n.grid()
input = tk.Entry(name,font=("Times New Roman",15))
input.grid()
def display():
    a = input.get()
    print(a)
    wb.open("https://www.justwatch.com/in/search?q="+a)

g = tk.Button(name,text="search",font=("Times New Roman",15),command=display,bg="red",activebackground="blue")
g.grid(row=2,column=0)
name.mainloop()