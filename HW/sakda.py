def insert_data(name, hw_name, status,value):
    mydb = con()
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO hw (name, hw_name, status,value) VALUE ('{}','{}', '{}',{})".format(
        name, hw_name, status,value
    )
    mycursor.execute(sql)
    mydb.commit()
    ID = mycursor.fetchall()
    return ID
def delete_hw_maxData(data):
    mydb = con()
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM hw WHERE id = (SELECT {}(id) FROM hw)".format(
        data
    )
    mycursor.execute(sql)
    mydb.commit()
