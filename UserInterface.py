from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Radiobutton, ttk, StringVar
from tkinter.ttk import Combobox
from Controller import run_search
def validate_input(p):
    if p == "" or p.isdigit():
        return True
    else:
        return False



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\batek\OneDrive\Pulpit\gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

validate = window.register(validate_input)
window.geometry("785x554")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 554,
    width = 785,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)

var = StringVar()
radio_1 = Radiobutton(text='Olx', variable=var, value='olx', font=("RobotoRoman Light", 12), background="white")
radio_1.place(
    x=35,
    y=68
)
radio_2 = Radiobutton(text='Allegro lokalnie', variable=var, value='allegro', font=("RobotoRoman Light", 12), background="white")
radio_2.place(
    x=95,
    y=68
)

var.set('olx')

canvas.create_text(
    38.0,
    105.0,
    anchor="nw",
    text="Poszukiwany przedmiot",
    fill="#000000",
    font=("RobotoRoman Light", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    178.0,
    144.5,
    image=entry_image_1
)
item_to_hunt_entry = Entry(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0,
    font=("RobotoRoman Light", 12 * -1)
)
item_to_hunt_entry.place(
    x=43.0,
    y=132.0,
    width=270.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    175.0,
    274.0,
    image=entry_image_2
)
blacklist_entry = Text(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0,
    font=("RobotoRoman Light", 12 * -1)
)
blacklist_entry.place(
    x=40.0,
    y=240.0,
    width=270.0,
    height=66.0
)

canvas.create_text(
    35.0,
    210.0,
    anchor="nw",
    text="Słowa do wykluczenia",
    fill="#000000",
    font=("RobotoRoman Light", 16 * -1)
)

canvas.create_rectangle(
    25.0,
    333.0,
    116.0,
    336.0,
    fill="#54A5F0",
    outline="")

canvas.create_rectangle(
    27.0,
    439.0,
    118.0,
    442.0,
    fill="#54A5F0",
    outline="")

canvas.create_rectangle(
    27.0,
    182.0,
    118.0,
    185.0,
    fill="#54A5F0",
    outline="")

canvas.create_text(
    38.0,
    355.0,
    anchor="nw",
    text="Cena",
    fill="#000000",
    font=("RobotoRoman Light", 16 * -1)
)

canvas.create_text(
    41.0,
    391.0,
    anchor="nw",
    text="Min: ",
    fill="#000000",
    font=("RobotoRoman Light", 14 * -1)
)
options = ["Domyślnie", "Cena malejąco", "Cena rosnąco", "Najnowsze"]

sort_combobox = Combobox(
    width=13,
    values = options
)
sort_combobox.place(
    x = 219.0,
    y = 355.0,
)
sort_combobox.current(0)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    103.5,
    401.5,
    image=entry_image_3
)
min_price_entry = Entry(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0,
    validate="key",
    validatecommand=(validate, "%P"),
    font=("RobotoRoman Light", 12 * -1)
)
min_price_entry.place(
    x=77.0,
    y=387.0,
    width=53.0,
    height=27.0
)
min_price_entry.insert(0, 0)


canvas.create_text(
    223.0,
    393.0,
    anchor="nw",
    text="Max:",
    fill="#000000",
    font=("RobotoRoman Light", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    287.5,
    401.5,
    image=entry_image_4
)

max_price_entry = Entry(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0,
    validate="key",
    validatecommand=(validate, "%P"),
    font=("RobotoRoman Light", 12 * -1)
)

max_price_entry.place(
    x=261.0,
    y=387.0,
    width=53.0,
    height=27.0
)
max_price_entry.insert(0,9999)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
hunt_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run_search(var.get(), item_to_hunt_entry.get(), blacklist_entry.get("1.0", "end-1c"), min_price_entry.get(), max_price_entry.get(), sort_combobox.current()),
    relief="flat"
)
hunt_button.place(
    x=116.0,
    y=485.0,
    width=124.0,
    height=36.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    387.0,
    23.0,
    image=image_image_1
)

canvas.create_text(
    358.0,
    10.0,
    anchor="nw",
    text="Hunter",
    fill="#000000",
    font=("RobotoRoman Light", 20 * -1)
)

canvas.create_rectangle(
    389.0,
    55.0,
    392.0,
    534.0,
    fill="#54A5F0",
    outline="")

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    605.5,
    291.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=445.0,
    y=61.0,
    width=321.0,
    height=458.0
)

window.resizable(False, False)
window.mainloop()




# import tkinter as tk
# import Functions as Fn
# import webbrowser
#
#
#
#
#
# def generate_window():
#
#     def start_hunt():
#
#         if input3.get() and input4.get() and input1.get() is not None:
#             price_range = [int(input3.get()), int(input4.get())]
#             hunted_item = input1.get()
#             black_list = input2.get().split(",")
#             found_links = Fn.find(hunted_item, black_list, price_range)
#             links_list.delete(0, tk.END)
#             if len(found_links) == 0:
#                 links_list.insert(tk.END, "Nothing was hunted")
#             for link, price in found_links.items():
#                 links_list.insert(tk.END, f"{price} zł => {link}")
#
#     def open_link(event):
#         selected_index = links_list.nearest(event.y)
#         selected_link = links_list.get(selected_index)
#         price, link = selected_link.split(" => ")
#         webbrowser.open(link)
#
#     default_min = 0
#     default_max = 9999
#     root = tk.Tk()
#     root.title("Hunter")
#     root.geometry("800x300")
#     root['padx'] = 10
#     validate = root.register(validate_input)
#
#     spacers1 = tk.Label(root, text="")
#     spacers2 = tk.Label(root, text="")
#     spacers3 = tk.Label(root, text="")
#     spacers4 = tk.Label(root, text="")
#
#     label1 = tk.Label(root, text="Item to hunt", font=24)
#     input1 = tk.Entry(root, width=25)
#
#     header1 = tk.Label(root, text="Black list: ", font=24)
#     input2 = tk.Entry(root, width=25)
#
#     header2 = tk.Label(root, text="Price range: ", font=24)
#     label2 = tk.Label(root, text="Min price:", anchor="w", justify="left")
#     input3 = tk.Entry(root, width=25, validate="key", validatecommand=(validate, "%P"))
#     input3.insert(0, str(default_min))
#
#     label3 = tk.Label(root, text="Max price:", anchor="w", justify="left")
#     input4 = tk.Entry(root, width=25, validate="key", validatecommand=(validate, "%P"))
#     input4.insert(0, str(default_max))
#     button = tk.Button(text="Hunt", command=start_hunt)
#
#     links_list = tk.Listbox(root, height=15, width=100)
#
#     links_list.bind("<Button-1>", open_link)
#
#     label1.grid(row=0, column=0)
#     input1.grid(row=1, column=0)
#
#     spacers1.grid(row=2, column=0)
#
#     header1.grid(row=3, column=0)
#     input2.grid(row=4, column=0)
#
#     spacers2.grid(row=5, column=0)
#
#     header2.grid(row=6, column=0)
#     label2.grid(row=7, column=0)
#     input3.grid(row=8, column=0)
#     label3.grid(row=9, column=0)
#     input4.grid(row=10, column=0)
#
#     spacers3.grid(row=11, column=0)
#
#     button.grid(row=12, column=0)
#
#     spacers4.grid(row=0, column=1)
#     links_list.grid(row=0, column=2, rowspan=12, sticky="nsew")
#
#     root.mainloop()
#
# def validate_input(p):
#     if p == "" or p.isdigit():
#         return True
#     else:
#         return False


