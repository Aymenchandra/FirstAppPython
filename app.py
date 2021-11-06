import sqlite3

def not_existe_id(num):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"select * from user where id = {num} ")
    if(len(cr.fetchall())>0):
        db.close()
        return False
    else:
        db.close()
        return True 

def not_existe_name(n):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute(f"select * from user where name = '{n}' ")
    if(len(cr.fetchall())>0):
        db.close()
        return False
    else:
        db.close()
        return True 

def add_user(user_id,name):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    if(not_existe_id(user_id)):
        cr.execute(f"insert into user values({user_id},'{name}')")    
        db.commit()
        print("successful insertion ")
        db.close()
    else:
        print("Sorry id already used ")
        db.close()

def update_user(user_id):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    if(not not_existe_id(user_id)):
        newname = input("Set your new name: ")
        cr.execute(f"update user set name = '{newname}' where id = {user_id} ")
        db.commit()
        print("Successful modification")
        db.close()
    else:
        print("inexistent user")    
        db.close()

def delete_user(user_id):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    if(not not_existe_id(user_id)):
        cr.execute(f"delete from user where id = {user_id} ")
        db.commit()
        print("Successful suppression")
        db.close()
    else:
        print("inexistent user")    
        db.close()

def show_user1(info):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    if(not not_existe_id(info)):
        cr.execute(f"select * from user where id = {info} ")
        table = cr.fetchall()
        for rows in table:
            print(f"Your id => {rows[0]}",end=" ")
            print(f"| Your name => {rows[1]} ")
        print("Successful selection")
        db.close()
    else:
        print("inexistent id")
        db.close()

def show_user2(info):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    if(not not_existe_name(info)):
        cr.execute(f"select * from user where name = '{info}' ")
        table = cr.fetchall()
        for rows in table:
            print(f"Your id => {rows[0]} ",end=" ")
            print(f"| Your name => {rows[1]} ")
        print("Successful selection")
        db.close()
    else:
        print("inexistent name")
        db.close()    

msg = True
message = """


What do you want? Press
A => to add user
U => to update user
D => to delete user
S => to show information 
E => to exit
Choose One:
"""
while(msg):
    m = input(message)
    if (m.capitalize()=="A"):
        print("Register:")
        num=input("\t Enter id: ")
        name=input("\t What's your name? ")
        add_user(num,name)
    elif (m.capitalize()=="U"):
        print("Edit:")
        num=input("\tPut your id: ")
        update_user(num)
    elif (m.capitalize()=="D"):
        print("Remove:")
        num=input("\tPut your id: ")
        delete_user(num)
    elif(m.capitalize()=="S"):
        print("Display:")
        btn=input("""\tWhich information do you want?")
                  I => ID
                  N => Name""")
        if(btn.capitalize()=="I"):
            info=input("Put your id: ")
            show_user1(info)
        elif(btn.capitalize()=="N"):
            info=input("Put your name: ")
            show_user2(info)
        else:
            print("Sorry it's wrong key")        
    elif(m.capitalize()=="E"):
        print("GoodBye")
        msg=False
        break
    else:    
        print("You put the wrong key try again")