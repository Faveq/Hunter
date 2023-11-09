import tkinter as tk


def validate_input(P):
    if P == "" or P.isdigit():
        return True
    else:
        return False


def generate_window():
    root = tk.Tk()
    root.title("Hunter")
    root.geometry("450x300")
    root['padx'] = 10
    validate = root.register(validate_input)

    spacers1 = tk.Label(root, text="")
    spacers2 = tk.Label(root, text="")
    spacers3 = tk.Label(root, text="")
    spacers4 = tk.Label(root, text="")

    label1 = tk.Label(root, text="Item to hunt", font=24)
    input1 = tk.Entry(root, width=25)

    header1 = tk.Label(root, text="Black list: ", font=24)
    input2 = tk.Entry(root, width=25)

    header2 = tk.Label(root, text="Price range: ", font=24)
    label2 = tk.Label(root, text="Min price:", anchor="w", justify="left")
    input3 = tk.Entry(root, width=25, validate="key", validatecommand=(validate, "%P"))

    label3 = tk.Label(root, text="Max price:", anchor="w", justify="left")
    input4 = tk.Entry(root, width=25, validate="key", validatecommand=(validate, "%P"))

    button = tk.Button(text="Hunt")

    text = tk.Text(root, height=15, width=33)

    label1.grid(row=0, column=0)
    input1.grid(row=1, column=0)

    spacers1.grid(row=2, column=0)

    header1.grid(row=3, column=0)
    input2.grid(row=4, column=0)

    spacers2.grid(row=5, column=0)

    header2.grid(row=6, column=0)
    label2.grid(row=7, column=0)
    input3.grid(row=8, column=0)
    label3.grid(row=9, column=0)
    input4.grid(row=10, column=0)

    spacers3.grid(row=11, column=0)

    button.grid(row=12, column=0)

    spacers4.grid(row=0, column=1)
    text.grid(row=0, column=2, rowspan=12)

    root.mainloop()



