from tkinter import *

root = Tk()
root.title('Когнитивная карта для проблемы неуплаты налогов')
root.geometry('800x600')
root.resizable(width=False, height=False)



canvas = Canvas(root, bg='white', width=800, height=600)

#целевая вершина
canvas.create_oval(600,100,650,150, fill="#cd3838")
canvas.create_text(625,75,text="Налоговые поступления", fill="black", font="15")

#стрелка неплатежи нал. - ЦВ
canvas.create_line(350,125,600,125, arrow=LAST)
canvas.create_text(470,110,text="-", fill="black", font=("bold", 30))

#неплатежи налогов
canvas.create_oval(300,100,350,150, fill="#1f1b1b")
canvas.create_text(325,75,text="Неплатежи налогов", fill="black", font="15")

#стрелка доходы - неплатежи нал. 
canvas.create_line(175,250,315,145, arrow=LAST)
canvas.create_text(250,175,text="+", fill="black", font=("bold", 20))

#доходы
canvas.create_oval(150,250,200,300, fill="#1f1b1b")
canvas.create_text(150,225,text="Доходы", fill="black", font="15")

#стрелка расходы - неплатежи нал. 
canvas.create_line(325,250,315,145, arrow=LAST)
canvas.create_text(300,210,text="-", fill="black", font=("bold", 30))

#расходы
canvas.create_oval(300,250,350,300, fill="#1f1b1b")
canvas.create_text(360,225,text="Расходы", fill="black", font="15")

#стрелка финансовая стабильность - доходы 
canvas.create_line(125,400,175,300, arrow=LAST)
canvas.create_text(140,325,text="+", fill="black", font=("bold", 20))

#стрелка финансовая стабильность - расходы 
canvas.create_line(125,400,325,300, arrow=LAST)
canvas.create_text(200,375,text="-", fill="black", font=("bold", 30))

#финансовая стабильность
canvas.create_oval(100,400,150,450, fill="#4d913e")
canvas.create_text(100,475,text="Финансовая стабильность", fill="black", font="15")

#стрелка уровень налогового бремени - доходы 
canvas.create_line(375,400,175,300, arrow=LAST)
canvas.create_text(295,375,text="-", fill="black", font=("bold", 30))

#стрелка уровень налогового бремени - расходы 
canvas.create_line(375,400,325,300, arrow=LAST)
canvas.create_text(360,325,text="+", fill="black", font=("bold", 20))

#стрелка уровень налогового бремени - расходы 
canvas.create_line(375,400,625,150, arrow=LAST)
canvas.create_text(515,280,text="+", fill="black", font=("bold", 20))

#уровень налогового бремени
canvas.create_oval(350,400,400,450, fill="#4d913e")
canvas.create_text(365,475,text="Уровень налогового бремени", fill="black", font="15")


canvas.pack()



root.mainloop()