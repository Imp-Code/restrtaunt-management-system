import sqlite3 as sql 

def sqlchange(query):
    con = sql.connect("DataBase")
    cursor = con.cursor()
    cursor.executescript(query)
    con.commit()

def sqlchangetwo(query):
    con = sql.connect("DataBase")
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()

def sqlchangethree(query):
    con = sql.connect("DataBase")
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    return cursor.fetchall()

def CreateTables():
    con = sql.connect("DataBase")
    cursor = con.cursor()
    query = """
    create table stock(id integer primary key autoincrement, item varchar, quantity int, status varchar);
    create table forms(tablenumber int primary key, details varchar, priority varchar);
    """
    cursor.executescript(query)
    con.commit()

def addstock(item,quantity,status):
    query = f"""
    update stock set quantity = quantity+{quantity}, status = "{status}"
    """
    query1 = f"""
    insert into stock(item,quantity,status) values("{item}",{quantity},"{status}")
    """
    query2 = f"""
    select * from stock where item = "{item}"
    """

    result = sqlchangethree(query2)
    if result == []:
        sqlchangetwo(query1)
    else:
        sqlchangetwo(query)

def removestock(id):
    query = f"""
    delete from stock where id = {id}
    """
    sqlchangetwo(query)

def allstock():
    query = f"""
    select * from stock
    """
    return sqlchangethree(query)

def addWaiterForm(tablenumber,orderdetails,priority):
    query = f"""
    insert into forms values({tablenumber},"{orderdetails}","{priority}")
    """
    sqlchangetwo(query)

def allorders():
    query = f"""
    select * from forms order by priority desc
    """
    return sqlchangethree(query)

def removeorder(tno):
    query = f"""
    delete from forms where tablenumber = {tno}
    """
    sqlchangetwo(query)

    