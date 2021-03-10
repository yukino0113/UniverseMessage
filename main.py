from tkinter import *
import pandas as pd
import urllib
from urllib.request import urlopen

# in/output paths
rawPath = r'C:\Users\jethr\Desktop\UMuse\raw.txt'
processPath = r"C:\Users\jethr\Desktop\UMuse\process.txt"

# window settings
window = Tk()
window.title('宇宙訊息讀取程式')
window.geometry("500x700")
window.resizable(False, False)
window.configure(background="#3c3f41")


# main window code

# input window
inputWindow = Text(window, height=8, width=50)
inputWindow.insert(END, '不讓你輸入文字啦！')
inputWindow.tag_add('color', '1.0', '12.0')
inputWindow.tag_configure('color', foreground='white')
inputWindow.configure(background='#2b2b2b')
inputWindow.place(x=10, y=700-125)
inputWindow.configure(state=DISABLED)

# text window
textWindow = Text(window, height=38, width=68)
textWindow.configure(background='#2b2b2b')
textWindow.place(x=10, y=10)

initMessageCount = 0
showMessageCount = 0


# message process
def messageInit():
    global initMessageCount
    sheet_url = "https://docs.google.com/spreadsheets/d/1FdA46JHfMpNizZLqsEPUNgsNQSu5zJo89AuXnzAiz5k/edit#gid=463395130"
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    pd.read_csv(url_1, skiprows=1).to_csv(rawPath, header=False, index=False)
    with open(rawPath, encoding="utf-8") as raw:
        with open(processPath, 'w+', encoding="utf-8") as process:
            for line in raw:
                initMessageCount += 1
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

                if initMessageCount > 2:
                    break


def showMessage():
    global showMessageCount
    imageIndex = []
    playerIndex = []
    # player profile process
    M3author = ['dragon060810']
    M3manage = ['ivy60627', 'yozora900308', 'nicosand', 'yukino0113']
    with open(processPath, 'r', encoding="utf-8") as process:
        for line in process:
            showMessageCount += 1
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
            picPath = r'C:\Users\jethr\Desktop\UMuse\\' + playerId + ".png"
            if playerId not in playerIndex:
                try:
                    profilehtml = urlopen(profilePage)
                except:
                    profilehtml = urlopen("https://minotar.net/avatar/c06f89064c8a49119c29ea1dbd1aab82/50.png")

            with open(picPath, 'w+') as pic:
                urllib.request.urlretrieve(profilePage, picPath)

            imageIndex.append(PhotoImage(file=picPath))

            textWindow.tag_add('white', '1.0', '100.0')
            textWindow.tag_configure('white', foreground='white')
            textWindow.insert(INSERT, "\n ")
            textWindow.image_create(INSERT, image=imageIndex[showMessageCount - 1])
            if playerId == M3author:
                textWindow.insert(INSERT, " " + playerId + "  " + messageTime + "  (開發者)\n\n ")
            elif playerId == M3manage:
                textWindow.insert(INSERT, " " + playerId + "  " + messageTime + "  (管理員)\n\n ")
            else:
                textWindow.insert(INSERT, " " + playerId + "  " + messageTime + "\n\n ")
            textWindow.insert(INSERT, message + "\n ")


def refresh(args):
    pass



refreshButton = Button(window, text='按我手動刷新\n\n5分鐘自動刷新一次', height=10, width=15, command=refresh)
refreshButton.place(x=500-125, y=700-175)

messageInit()
showMessage()

# start window
textWindow.configure(state=DISABLED)
window.mainloop()
