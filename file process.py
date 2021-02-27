import pandas as pd

rawPath = r'C:\Users\jethr\Desktop\UMuse\raw.txt'
processPath = r"C:\Users\jethr\Desktop\UMuse\process.txt"

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
                id = b[1]
            except:
                id = ' '
            try:
                msg = b[2]
            except:
                msg = ' '
            try:
                version = a[3]
            except:
                version = ' '

            process.write(str(time) + '$' + str(id) + '$' + str(msg) + '$' + str(version))
