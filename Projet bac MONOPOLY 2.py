# Créé par Clément, le 24/03/2020 en Python 3.4
from tkinter import*

fenetre = Tk()

#canvas
canvas = Canvas(fenetre, width=1450, height=700,background='black')
canvas.pack()

for ligne in range(1, 13):
  if ligne % 2 == 0:
    coul = 'yellow'
  else:
    coul = 'blue'
  canvas.create_rectangle(100*ligne, 0, 100*ligne+100, 100,fill=coul)

for ligne in range(1, 13):
  if ligne % 2 == 0:
    coul = 'yellow'
  else:
    coul = 'blue'
  canvas.create_rectangle(100*ligne, 600, 100*ligne+100, 700,fill=coul)

for colonne in range(1, 6):
  if colonne % 2 == 0:
    coul = 'red'
  else:
    coul = 'green'
  canvas.create_rectangle(100, 100*colonne, 200, 100*colonne+100,fill=coul)

for colonne in range(1, 6):
  if colonne % 2 == 0:
    coul = 'red'
  else:
    coul = 'green'
  canvas.create_rectangle(1200, 100*colonne, 1300, 100*colonne+100,fill=coul)

canvas.create_text(700, 350, text="MONOPOLY", font="Arial 70 italic", fill="white")



fenetre.mainloop()