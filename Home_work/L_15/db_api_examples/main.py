
import sqlite3

conn = sqlite3.connect("db_api_bd_example.db")

print(type(conn))

cursor = conn.cursor()
print(type(conn))

cursor.execute("""CREATE TABLE IF NOT EXISTS user (
u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
u_name TEXT NOT NULL,
u_surname TEXT NOT NULL
);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS task (
t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
t_name TEXT NOT NULL,
t_priority INTEGER NOT NULL,
u_id_fk INTEGER NOT NULL,
FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
);
""")

conn.commit()

# user_data1 = ("Petia","Petrov")

# cursor.execute("""insert into user (u_name, u_surname) values (?, ?);""" , user_data1)
# cursor.execute("""insert into user (u_name, u_surname) values (?, ?);""", ("Vasia","Petrov"))
# cursor.execute("""insert into user (u_name, u_surname) values (?, ?);""",  ("Sam","Petrov"))

# conn.commit()

# cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?,?,?);""", ("run",3,1))
# cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?,?,?);""",  ("sleep",1,2))
# cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?,?,?);""",  ("swim",4,3))

# conn.commit()



# read
for record in cursor.execute("""select * from user;"""):
    print(record)
    #print(record[0],record[2])


cursor.execute("""select * from task;""")
result = cursor.fetchall()
print(result)
print()

for i in result:
    print(i)


# delete
cursor.execute("""delete from task where t_id=?;""",(5,))
cursor.execute("""delete from task where t_id=?;""",(4,))
conn.commit()
conn.commit()

cursor.execute("""select * from task;""")
result = cursor.fetchall()
print(result)
print()

# update
tp=("Denis", "Greg", 1)
cursor.execute("""update user set u_name=?,u_surname=? where u_id=?;""", tp)
conn.commit()


cursor.execute("""select * from user;""")
result = cursor.fetchall()
print(result)
print()

for i in result:
    print(i)

