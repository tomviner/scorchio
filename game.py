from Tkinter import *

root = Tk()


TANK_IMAGE = PhotoImage(file="graphics/tank.gif")
HEIGHT = 500
WIDTH = 600


def draw_tank(x1, y1):
    canvas.create_image(x1, y1, image=TANK_IMAGE, state="normal")


def draw_projectile(x1, y1):
    canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="red", width=1)


canvas = Canvas(root, bg="blue", height=HEIGHT, width=WIDTH)

draw_tank(50, HEIGHT-30)
draw_tank(WIDTH-50, HEIGHT-30)

draw_projectile(200, 200)

canvas.pack()

root.mainloop()
