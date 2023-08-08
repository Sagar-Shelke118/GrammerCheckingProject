from tkinter import *
from textblob import TextBlob


def check_spellings():
    a = TextBlob(spell_check.get())
    spell = Label(window,text='The correct spelling is :',font=('Arial',30,'bold'),bg='gray')
    spell.pack()
    correct_text = Label(window,text=str(a.correct()),font=('Arial',30,'bold'),bg='lightpink')
    correct_text.pack()

window = Tk()
window.title("spelling checker")
window.geometry("800x600")
window.config(background='lightgreen')

text_heading = Label(window,text='spelling check',font=('Arial',50,'bold'),bg='black',fg='lightpink')
text_heading.pack()

text_check = Label(window,text='Enter the text',font=('Arial',35,'bold'),bg='yellow',fg='red')
text_check.pack()

spell_check = Entry(window,font=("Arial",45,'bold'),width=500,bg='lightblue')
spell_check.pack()

check_button = Button(window,text='check',font=("Arial",30,'bold'),fg='white',bg='red',command=check_spellings)
check_button.pack()

window.mainloop()