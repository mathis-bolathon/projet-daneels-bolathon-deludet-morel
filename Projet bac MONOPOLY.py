from tkinter import*

fenetre = Tk()

#canvas
canvas = Canvas(fenetre, width=1450, height=700,background='black')
canvas.pack()
canvas.create_rectangle(100,0,200,100,fill='blue')
canvas.create_rectangle(200,0,300,100,fill='yellow')
canvas.create_rectangle(300,0,400,100,fill='blue')
canvas.create_rectangle(400,0,500,100,fill='yellow')
canvas.create_rectangle(500,0,600,100,fill='blue')
canvas.create_rectangle(600,0,700,100,fill='yellow')
canvas.create_rectangle(700,0,800,100,fill='blue')
canvas.create_rectangle(800,0,900,100,fill='yellow')
canvas.create_rectangle(900,0,1000,100,fill='blue')
canvas.create_rectangle(1000,0,1100,100,fill='yellow')
canvas.create_rectangle(1100,0,1200,100,fill='blue')
canvas.create_rectangle(1200,0,1300,100,fill='yellow')

canvas.create_rectangle(100,600,200,700,fill='yellow')
canvas.create_rectangle(200,600,300,700,fill='blue')
canvas.create_rectangle(300,600,400,700,fill='yellow')
canvas.create_rectangle(400,600,500,700,fill='blue')
canvas.create_rectangle(500,600,600,700,fill='yellow')
canvas.create_rectangle(600,600,700,700,fill='blue')
canvas.create_rectangle(700,600,800,700,fill='yellow')
canvas.create_rectangle(800,600,900,700,fill='blue')
canvas.create_rectangle(900,600,1000,700,fill='yellow')
canvas.create_rectangle(1000,600,1100,700,fill='blue')
canvas.create_rectangle(1100,600,1200,700,fill='yellow')
canvas.create_rectangle(1200,600,1300,700,fill='blue')

canvas.create_rectangle(100,100,200,200,fill='red')
canvas.create_rectangle(100,200,200,300,fill='green')
canvas.create_rectangle(100,300,200,400,fill='red')
canvas.create_rectangle(100,400,200,500,fill='green')
canvas.create_rectangle(100,500,200,600,fill='red')

canvas.create_rectangle(1200,100,1300,200,fill='green')
canvas.create_rectangle(1200,200,1300,300,fill='red')
canvas.create_rectangle(1200,300,1300,400,fill='green')
canvas.create_rectangle(1200,400,1300,500,fill='red')
canvas.create_rectangle(1200,500,1300,600,fill='green')

canvas.create_text(700, 350, text="MONOPOLY", font="Arial 70 italic", fill="white")

fenetre.mainloop()