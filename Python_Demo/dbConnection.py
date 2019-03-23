import MySQLdb as mysqldb

mydb = mysqldb.connect(
    host="localhost",
    user="root",
    passwd="pradnya7",
    database="EARS"
)
mycursor = mydb.cursor()


def fetchVideoNames():
    list1 = [];
    mycursor.execute("SELECT videoName FROM SavedVideos order by SrNo desc;")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        list1.append(x[0])
    return list1


def insertVideoName(newVidName):
    query = "INSERT INTO SavedVideos(videoName) VALUES(%s)"
    args = (newVidName)
    mycursor.execute(query, [newVidName])
    mydb.commit()


if __name__ == '__main__':
    fetchVideoNames()
    # insertVideoName("new my.mp4")