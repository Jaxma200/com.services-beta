import tkinter as tk

root = tk.Tk()
root.title("com.services-waterfall-modified --- trying to connect to a server")
root.geometry("900x900")

label = tk.Label(root, text="enter key to start using waterfall")
label.pack(pady=20)

instruction_label = tk.Label(root, text="enter key")
instruction_label.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

def open_new_window():
    new_root = tk.Tk()
    new_root.title("com.services -- Debug")
    new_root.geometry("1000x2000")

    new_label = tk.Label(new_root, text="com.services -- Debug Version (For Developers) is running.")
    new_label.place(relx=0.0, rely=0.0, anchor="nw", x=20, y=20)

    new_root.mainloop()


def check_key():
    if entry.get() == "WATERFALL_FREE_W24JF84JD389EJFD4D029_FIRST":
        status_label.config(text="Key accepted.")
        root.destroy()
        open_new_window()
    else:
        status_label.config(text="Incorrect key. Please type a correct key.")

check_button = tk.Button(root, text="Submit", command=check_key)
check_button.pack(pady=10)

root.mainloop()