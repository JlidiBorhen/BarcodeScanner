import MySQLdb


def connectDB():
            global dbcon
            dbcon = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="dietpi",
                     db="test_db")
            global cur
            cur =dbcon.cursor()
