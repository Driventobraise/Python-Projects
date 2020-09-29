

import sqlite3

conn = sqlite3.connect('asng1.db')
# creates tbl_fileTxt database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileTxt( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtFile TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('asng1.db')
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg', \
            'World.txt','data.pdf','myPhotos.jpeg')

with conn:
    # parses list for .txt file and assigns them to the variable "value"
    for file in fileList:
        if file.endswith('.txt'):
            value = file
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileTxt(col_txtFile) VALUES (?)", (value,))
            conn.commit()
conn.close()

conn = sqlite3.connect('asng1.db')
# queries the db for our add files
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txtFile FROM tbl_fileTxt")
    varTxt = cur.fetchall()
    for item in varTxt:
        msg = "Our text files tha have been added to the database are: {}".format(item[0])
        print(msg)
        



