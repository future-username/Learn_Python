# class Box:
#     material = 'card'
#     amount = 0
#
#     def __init__(self):
#         self.width = 1
#         self.length = 2
#         self.height = 3
#
#
# Box.material = 'wood'
# box_1 = Box()
# box_1.width = 10
# print(box_1)
# print(box_1.__dict__)
# # box_1.material = 'wood'
# box_1.x = 11
# box_1.y = 11
# print(box_1.material)
# print(box_1.__dict__)
# print(box_1.__dir__())
# print()
#
# box_2 = Box()
# print(box_2)
# print(box_2.__dict__)
# print(box_2.material)
# print(box_2.__dict__)


# from tkinter import *
#
# root = Tk()
# c = Canvas(root, width=300, height=200, bg="white")
# c.pack()
#
# ball_1 = c.create_oval(0, 100, 40, 140, fill='green')
# ball_2 = c.create_oval(0, 50, 40, 90, fill='red')
#
#
# def motion(ball):
#     c.move(ball, 1, 0)
#     if c.coords(ball)[2] < 300:
#         root.after(20, lambda: motion(ball))
#
#
# motion(ball_1)
# motion(ball_2)
#
# root.mainloop()


# from tkinter import *
#
#
# class Ball:
#     def __init__(self, x0: int, y0: int, x1: int, y1: int, color: str):
#         self.ball = c.create_oval(x0, y0, x1, y1, fill=color)
#
#     @staticmethod
#     def motion(ball):
#         c.move(ball, 1, 0)
#         if c.coords(ball)[2] < 300:
#             root.after(20, lambda: Ball.motion(ball))
#
#
# root = Tk()
# c = Canvas(root, width=300, height=200, bg="white")
# c.pack()
#
# ball_1 = Ball(0, 100, 40, 140, 'green')
# ball_1.motion(ball_1.ball)
#
# ball_2 = Ball(0, 50, 40, 90, 'red')
# ball_2.motion(ball_2.ball)
#
# root.mainloop()


from tkinter import *


class Ball:
    def __init__(self, parent: Canvas, x0: int, y0: int, x1: int, y1: int, color: str):
        self.parent = parent
        self.ball = parent.create_oval(x0, y0, x1, y1, fill=color)

    def motion(self):
        self.parent.move(self.ball, 1, 0)
        if self.parent.coords(self.ball)[2] < 300:
            root.after(20, self.motion)


root = Tk()
canvas = Canvas(root, width=300, height=200, bg="white")
canvas.pack()

ball_1 = Ball(canvas, 0, 100, 40, 140, 'green')
ball_1.motion()

ball_2 = Ball(canvas, 0, 50, 40, 90, 'red')
ball_2.motion()

root.mainloop()
