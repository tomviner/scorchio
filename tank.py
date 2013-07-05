from game import Game

from Tkinter import *


class Tank(object):

    def __init__(self, start_x, start_y=100):
        self.x = start_x
        self.y = start_y

    @property
    def coords(self):
        return (self.x, self.y)


class GameLoop(object):
    def tick():
        game.draw(t1.coords, t2.coords)
        game.draw(t1.coords, t2.coords)
        self.root.after(20, self.tick)

    def __init__():
        self.root = Tk()
        t1 = Tank(100)
        t2 = Tank(700)

        self.root.after(2000, self.tick)
        self.root.mainloop()

def main():
    g = Game()
    g.run()

if __name__ == '__main__':
    main()

