import sqlite3


def dataCollect():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute("select * from CSE470")
    data = cursor.fetchall()
    ndata = []
    for i in data:
        ndata.append(i[0])
    rdata = {
        'heading': "Some architectures",
        'list': ndata
        }
    return rdata
