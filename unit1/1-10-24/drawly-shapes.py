import drawly

drawly.start("My Drawing Program", background="grey")

drawly.set_speed(3)

drawly.circle(300, 300, 150)
drawly.set_color("blue")
drawly.circle(600, 200, 100)
drawly.draw()

drawly.set_color("black")
drawly.circle(600, 200, 100, 10)
drawly.draw()

drawly.done()
