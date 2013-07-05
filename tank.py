from game import draw_world

from Tkinter import *

class Tank(object):

    def __init__(self, start_x, start_y=100):
        self.x = start_x
        self.y = start_y

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

        self.canvas = Canvas(self.root, width=200, height=100)
        self.canvas.pack()

        t1 = Tank(100)
        t2 = Tank(700)

        self.root.after(2000, self.tick)
        self.root.mainloop()


def main():
    g = GameLoop()


if __name__ == '__main__':
    main()
