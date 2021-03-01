from tkinter import *
import pandas as pd
import urllib
from urllib.request import urlopen

# in/output paths
rawPath = r'C:\Users\jethr\Desktop\UMuse\raw.txt'
processPath = r"C:\Users\jethr\Desktop\UMuse\process.txt"
picPath = r'C:\Users\jethr\Desktop\UMuse\icon.png'

# window settings
window = Tk()
window.title('宇宙訊息讀取程式')
window.geometry("500x700")
window.resizable(False, False)
window.configure(background="#3c3f41")


# main window code
# refresh button
refreshButton = Button(window, text='按我手動刷新\n\n5分鐘自動刷新一次', height=10, width=15)
refreshButton.place(x=500-125, y=700-175)


# input window
inputWindow = Text(window, height=8, width=50)
inputWindow.insert(END, '不讓你輸入文字啦！')
inputWindow.tag_add('color', '1.0', '12.0')
inputWindow.tag_configure('color', foreground='white')
inputWindow.configure(background='#2b2b2b')
inputWindow.place(x=10, y=700-125)
inputWindow.configure(state=DISABLED)

# text window
textWindow = Text(window, height=38, width=65)
textWindow.configure(background='#2b2b2b')
textWindow.place(x=10, y=10)

# scrollbar
scrollbar = Scrollbar(window, width=15)
scrollbar.pack(side="left", fill=BOTH, expand=True)
scrollbar.place(x=478, y=10)
scrollbar.configure(command=textWindow.yview())
textWindow.config(yscrollcommand=scrollbar.set)

# message process
sheet_url = "https://docs.google.com/spreadsheets/d/1FdA46JHfMpNizZLqsEPUNgsNQSu5zJo89AuXnzAiz5k/edit#gid=463395130"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
pd.read_csv(url_1, skiprows=1).to_csv(rawPath, header=False, index=False)
with open(rawPath, encoding="utf-8") as raw:
    with open(processPath, 'w+', encoding="utf-8") as process:
        for line in raw:
            a = line.split(',')
            b = a[1].split('_$_')

            try:
                time = a[0]
            except:
                time = ' '
            try:
                playerId = b[1]
            except:
                playerId = ' '
            try:
                msg = b[2]
            except:
                msg = ' '
            try:
                version = a[3]
            except:
                version = ' '

            process.write(str(time) + '$' + str(playerId) + '$' + str(msg) + '$' + str(version))
            break

# player profile process
with open(processPath, 'r', encoding="utf-8") as process:
    for line in process:
        c = line.split('$')
        messageTime = c[0]
        playerId = c[1]
        message = c[2]
        uuidPage = "https://api.mojang.com/users/profiles/minecraft/" + playerId
        uuidhtml = urlopen(uuidPage)
        d = uuidhtml.read()
        e = str(d).split('"')
        uuid = e[7]
        profilePage = "https://minotar.net/avatar/" + uuid + '/25.png'
        try:
            profilehtml = urlopen(profilePage)
        except:
            profilehtml = urlopen("https://minotar.net/avatar/c06f8906-4c8a-4911-9c29-ea1dbd1aab82/50.png")

        with open(picPath, 'w+') as pic:
            urllib.request.urlretrieve(profilePage, picPath)

        picProcess = tkinter.PhotoImage(file = picPath)
        textWindow.insert(INSERT, pic)
        textWindow.configure(state=DISABLED)




# start window
window.mainloop()
