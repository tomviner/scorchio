from Tkinter import *

root = Tk()

canvas = Canvas(root, bg="blue", height=250, width=250)

arc = canvas.create_arc(10,50,240,210, start=0, extent=150, fill="red")
# w = Label(root, text="Hello, world!")
# w.pack()

tank_image = PhotoImage(file="graphics/tank.gif")
panel = Label(root, image=tank_image)
panel.pack(side="bottom", fill = "both", expand="no")


canvas.pack()

root.mainloop()
