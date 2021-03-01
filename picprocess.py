from urllib.request import urlopen
id = "yukino0113"
uuidPage = "https://api.mojang.com/users/profiles/minecraft/" + id
uuidhtml = urlopen(uuidPage)
a = uuidhtml.read()
b = str(a).split('"')
uuid = b[7]
profilePage = "https://minotar.net/avatar/" + uuid + '/25.png'
try:
    profilehtml = urlopen(profilePage)
except:
    profilehtml = urlopen("https://minotar.net/avatar/c06f8906-4c8a-4911-9c29-ea1dbd1aab82/50.png")
#print(profilehtml.read())

picPath = r'C:\Users\jethr\Desktop\UMuse\icon.png'
with open(picPath, 'w+') as pic:
    #pic.write(profilehtml.read())
    #urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
    urllib.request.urlretrieve(profilePage, picPath)