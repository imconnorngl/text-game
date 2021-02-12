import tkinter as tk

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]

def gridConstructor(root, position):
    raw = root.winfo_geometry().split("+")[0].split("x")
    dimensions = { "x": int(int(raw[0])/41), "y": int(int(raw[1])/68) }

    grid = "\n\n"
    for y in range(dimensions["y"], -1, -1):
        lines = { 1: "    ", 2: "    ", 3: "    ", 4: "    " }
        for x in range(0, dimensions["x"]):
            for line in lines:
                lines[line] += ("@@@@@" if x == position["x"] and y == position["y"] else "#####")
        for line in lines:
            grid += lines[line] + "\n"

    text = tk.Text(master=root, bg="black", fg="white")
    text.pack(expand=True, fill='both')
    text.insert(tk.END, grid)