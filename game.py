from Tkinter import *


class Game:
    def __init__(self, width, height):
        self.TANK_IMAGE = PhotoImage(file="graphics/tank.gif")
        self.height = height
        self.width = width

    def draw_tank(self, canvas, x1, y1):
        canvas.create_image(x1, y1, image=self.TANK_IMAGE, state="normal")

    def draw_projectile(self, canvas, x1, y1):
        canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="red", width=1)

    def draw(self, canvas, t1_x, t1_y, t2_x, t2_y, p_x, p_y):
        self.draw_tank(canvas, t1_x, t1_y)
        self.draw_tank(canvas, t2_x, t2_y)
        self.draw_projectile(canvas, p_x, p_y)




if __name__ == '__main__':
    HEIGHT = 600
    WIDTH = 800

    root = Tk()
    canvas = Canvas(root, bg="blue", height=HEIGHT, width=WIDTH)
    g = Game(WIDTH, HEIGHT)
    g.draw(canvas, 50, HEIGHT-30, WIDTH-50, HEIGHT-30, 200, 200)
    canvas.pack()
    root.mainloop()
