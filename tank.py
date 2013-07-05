from game import Game

from Tkinter import *



class Shell(object):
    g = 9.8

    def __init__(self, start_x, start_y,
        speed_x, speed_y):
        self.x = start_x
        self.y = start_y
        self.speed_x = speed_x
        # never changes
        self.speed_y = speed_y

    def position_at_time(t):
        return (0.5 * self.g * t**2
            + self.initial_speed
            + self.start_y)

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

    def fire(self, angle):
        pass


class GameLoop(object):
    def tick(self):
        self.game.draw(self.canvas,
                       self.t1.x, self.t1.y,
                       self.t2.x, self.t2.y,
                       0, 0)
        self.t += 1
        self.root.after(20, self.tick)

    def __init__(self):
        self.t = 0
        self.root = Tk()

        self.canvas = Canvas(self.root, bg="blue", width=800, height=600)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.key)
        self.canvas.pack()

        self.game = Game(800, 600)

        self.t1 = Tank(100)
        self.t2 = Tank(700)

        self.root.after(200, self.tick)
        self.root.mainloop()

    def key(self, event):
        print repr(event.char)
        if event.char == "j":
            self.t1.turret_left()
        elif event.char == "k":
            self.t1.turret_right()
        elif event.char == " ":
            self.t1.fire()

def main():
    GameLoop()

if __name__ == '__main__':
    main()
