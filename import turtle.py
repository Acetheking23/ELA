import turtle
tartaruga = turtle.Turtle()
tartaruga.pencolor("blue")
def fazer_curva():
    for i in range(200):
     tartaruga.right(1)
     tartaruga.forward(1)
def    desenhar_coracao():
    tartaruga.fillcolor('blue')
    tartaruga.begin_fill()
    tartaruga.left(140)
    tartaruga.forward(113)
    fazer_curva()
    tartaruga.left(120)
    fazer_curva()
    tartaruga.forward(112)
    tartaruga.end_fill()
def inserir_texto():
  tartaruga.up()
  tartaruga.setpos(-80, 95) 
  tartaruga.down()
  tartaruga.color("black")
  tartaruga.write("PARABÉNS...", font=("verdana", 10, "bold"))

desenhar_coracao()
inserir_texto()

tartaruga.ht()
tartaruga.screen.mainloop()