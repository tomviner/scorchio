#from game import draw_world

from Tkinter import *

class Tank(object):

    def __init__(self, start_x, start_y=100, angle=0):
        self.x = start_x
        self.y = start_y
        self.angle = angle

    def turret_left(self):
        self.angle -= 1
        print self.angle

    def turret_right(self):
        self.angle += 1
        print self.angle

    @property
    def coords(self):
        return (self.x, self.y)


class GameLoop(object):
    def tick(self):

        draw_world(
            tank_1=t1.coords,
            tank_2=t2.coords,
        )

        self.t += 1
        self.root.after(20, self.tick)


    def __init__(self):
        self.t = 0
        self.root = Tk()

        self.canvas = Canvas(self.root, bg="blue", width=800, height=600)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.key)
        self.canvas.pack()

        self.t1 = Tank(100)
        self.t2 = Tank(700)

        self.root.after(200, self.tick)
        self.root.mainloop()

    def key(self, event):
        if event.char == "j":
            self.t1.turret_left()
        elif event.char == "k":
            self.t1.turret_right()

def main():
    GameLoop()

if __name__ == '__main__':
    main()

