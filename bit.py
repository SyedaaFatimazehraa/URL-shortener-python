import pyshorteners
import tkinter as tk

obj = pyshorteners.Shortener(api_key="78e2e16fe7e4f4ed7586a3d66ef49f3b2574526d")

root = tk.Tk()
root.title("Simple URL Shortener")
root.geometry("400x200")
root.configure(bg='black')

long_entry = tk.Entry(root)
long_entry.pack()

def short():
    long_url = long_entry.get()
    short_link = obj.bitly.short(long_url)
    result_label.config(text="Result: " + str(short_link))

gen_button = tk.Button(root, text="Generate", command=short)
gen_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
