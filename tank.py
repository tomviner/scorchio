import math

from game import Game

from Tkinter import *



class Shell(object):
    g = -9.8

    def __init__(self, start_x, start_y,
        speed_x, speed_y, start_t):
        self.start_x = start_x
        self.start_y = start_y
        self.initial_speed_x = speed_x
        self.initial_speed_y = speed_y
        self.start_t = start_t

    def position_at_time(self, t):
        t = t - self.start_t
        t = t / 20.
        xy = (self.start_x + self.initial_speed_x * t,
            600-(0.5 * self.g * t**2
            + self.initial_speed_y * t
            + self.start_y))
        print xy
        return xy

class Tank(object):

    def __init__(self, start_x, start_y=550, angle=0):
        self.x = start_x
        self.y = start_y
        self.angle = angle

    def turret_left(self):
        self.angle -= 1
        print self.angle

    def turret_right(self):
        self.angle += 1
        print self.angle

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    @property
    def coords(self):
        return (self.x, self.y)

    def fire(self, t):
        print self.x, self.y, math.sin(self.angle), math.cos(self.angle)

        def rad(deg):
            return math.pi * deg / 180.
        MUZ_VEL = 80
        return Shell(self.x, self.y-200, math.sin(rad(self.angle))*MUZ_VEL, math.cos(rad(self.angle))*MUZ_VEL, t)



class GameLoop(object):
    def tick(self):
        self.game.draw_setup(self.canvas,
                       self.t1.x, self.t1.y,
                       self.t2.x, self.t2.y)
        if self.projectile:
            x, y = self.projectile.position_at_time(self.t)
            if y > 570:
                self.projectile = None
            else:
                self.game.draw_projectile(self.canvas, x, y)
        self.t += 1
        self.root.after(20, self.tick)

    def __init__(self):
        self.t = 0
        self.root = Tk()
        self.projectile = None

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
        if event.char == "a":
            self.t1.move_left()
        elif event.char == "d":
            self.t1.move_right()
        elif event.char == " ":
            proj = self.t1.fire(self.t)
            self.projectile = proj

def main():
    GameLoop()

if __name__ == '__main__':
    main()
