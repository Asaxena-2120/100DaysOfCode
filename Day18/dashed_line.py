import turtle as t

tim = t.Turtle()

########### Draw a Dashed Line ########\
for _ in range(2):
  for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
  for _ in range(10):
    tim.forward(100)

