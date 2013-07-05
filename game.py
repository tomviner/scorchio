from Tkinter import *


class Game:
    def __init__(self, width, height):
        self.TANK_IMAGE = PhotoImage(file="graphics/tank.gif")
        self.height = height
        self.width = width
        self.old_px = 0
        self.old_py = 0

    def draw_tank(self, canvas, x1, y1):
        canvas.create_image(x1, y1, image=self.TANK_IMAGE, state="normal")

    def draw_proj(self, canvas, x1, y1, bg="red"):
        canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill=bg, width=0)

    def draw_setup(self, canvas, t1_x, t1_y, t2_x, t2_y):
        self.draw_tank(canvas, t1_x, t1_y)
        self.draw_tank(canvas, t2_x, t2_y)

    def draw_projectile(self, canvas, p_x, p_y):
        self.draw_proj(canvas, self.old_px, self.old_py, bg="blue")

        self.draw_proj(canvas, p_x, p_y)
        self.old_px = p_x
        self.old_py = p_y



if __name__ == '__main__':
    HEIGHT = 600
    WIDTH = 800

    root = Tk()
    canvas = Canvas(root, bg="blue", height=HEIGHT, width=WIDTH)
    g = Game(WIDTH, HEIGHT)
    g.draw_setup(canvas, 50, HEIGHT-30, WIDTH-50, HEIGHT-30)
    canvas.pack()

    g.draw_projectile(canvas, 100, 100)
    g.draw_projectile(canvas, 100, 100)
    canvas.pack()
    root.mainloop()
