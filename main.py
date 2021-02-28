from tkinter import *

# window settings
window = Tk()
window.title('abc')
window.geometry("500x700")
window.resizable(False, False)
window.configure(background="#3c3f41")


# main window code
# refresh button
refreshButton = Button(window, text='刷新', height=10, width=15)
refreshButton.place(x=500-125, y=700-175)

# text window
textWindow = Text(window, height=38, width=68, state=DISABLED)
textWindow.configure(background='#2b2b2b')
textWindow.place(x=10, y=10)

#input window
inputWindow = Text(window, height=8, width=50, state=DISABLED)
inputWindow.insert(END, '請輸入文字')
inputWindow.tag_configure("white")
inputWindow.configure(background='#2b2b2b')
inputWindow.place(x=10, y=700-125)

# start window
window.mainloop()
