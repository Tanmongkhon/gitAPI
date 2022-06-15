mycursor.execute(sql)
mydb.commit()
mycursor.close()
mydb.close()
ID = mycursor.lastrowid
return ID