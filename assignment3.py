import matplotlib.pyplot as plt
import random
import tkinter as tk
from tkinter.font import Font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# set the size of canvas
canvas_width = 800
canvas_height = 600

# square size
square_size = 50

# color of red yellow and blue
colors = ["#FF0000", "#FFFF00", "#0000FF"]

squares = []

root = tk.Tk()

#title
custom_font = Font(family="Helvetica", size=14, weight="bold")

label = tk.Label(root, text="Click to generate Mondrian's Boogie Woogie.", font=custom_font, fg="#333333", bg="#f0f0f0", padx=10, pady=5, relief="ridge")
label.pack()


fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, canvas_width)
ax.set_ylim(0, canvas_height)
ax.set_facecolor("#FFFFFF")
ax.set_xticks([])
ax.set_yticks([])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def handle_click(event):
    x = event.xdata
    y = event.ydata
    if x is not None and y is not None:
        # make sure squares are within the canvas
        if 0 <= x <= canvas_width and 0 <= y <= canvas_height:
            # generate ramdom color
            color = random.choice(colors)
            # add the generated square
            squares.append({"x": x, "y": y, "color": color, "direction": random.choice(["up", "down", "left", "right"]), "trajectory": [(x, y)]})

def update_canvas():
    ax.clear()
    ax.set_xlim(0, canvas_width)
    ax.set_ylim(0, canvas_height)
    ax.set_facecolor("#FFFFFF")
    ax.set_xticks([])
    ax.set_yticks([])
    for square in squares:
        x = square["x"]
        y = square["y"]
        color = square["color"]
        square_patch = plt.Rectangle((x, y), square_size, square_size, fc=color)
        ax.add_patch(square_patch)
        # square moving in random directions
        if square["direction"] == "up":
            square["y"] = min(canvas_height - square_size, y + 5)
        elif square["direction"] == "down":
            square["y"] = max(0, y - 5)
        elif square["direction"] == "left":
            square["x"] = max(0, x - 5)
        elif square["direction"] == "right":
            square["x"] = min(canvas_width - square_size, x + 5)
        square["trajectory"].append((square["x"], square["y"]))
        for point in square["trajectory"]:
            trajectory_patch = plt.Rectangle(point, square_size, square_size, fc=color)
            ax.add_patch(trajectory_patch)
    canvas.draw()
    root.after(100, update_canvas)

cid = fig.canvas.mpl_connect('button_press_event', handle_click)

update_canvas()

root.mainloop()