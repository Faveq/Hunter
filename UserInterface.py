import tkinter as tk
import Functions as Fn
import webbrowser

def validate_input(p):
    if p == "" or p.isdigit():
        return True
    else:
        return False


def generate_window():
    def start_hunt():

        if input3.get() and input4.get() and input1.get() is not None:
            price_range = [int(input3.get()), int(input4.get())]
            hunted_item = input1.get()
            black_list = input2.get().split(",")
            found_links = Fn.find(hunted_item, black_list, price_range)
            links_list.delete(0, tk.END)
            if len(found_links) == 0:
                links_list.insert(tk.END, "Nothing was hunted")
            for link in found_links:
                links_list.insert(tk.END, link)

    def open_link(event):
        selected_index = links_list.nearest(event.y)
        selected_link = links_list.get(selected_index)
        webbrowser.open(selected_link)

    default_min = 0
    default_max = 9999
    root = tk.Tk()
    root.title("Hunter")
    root.geometry("700x300")
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
    input3.insert(0, str(default_min))

    label3 = tk.Label(root, text="Max price:", anchor="w", justify="left")
    input4 = tk.Entry(root, width=25, validate="key", validatecommand=(validate, "%P"))
    input4.insert(0, str(default_max))
    button = tk.Button(text="Hunt", command=start_hunt)

    links_list = tk.Listbox(root, height=15, width=80)

    links_list.bind("<Button-1>", open_link)

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
    links_list.grid(row=0, column=2, rowspan=12)

    root.mainloop()



