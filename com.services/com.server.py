import tkinter as tk

root = tk.Tk()
root.title("com.services --- trying to connect to a server")
root.geometry("900x900")

label = tk.Label(root, text="Your build is unsupported. you have may tampered with the files. Error Code: 234")
label.pack(pady=20)


status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
