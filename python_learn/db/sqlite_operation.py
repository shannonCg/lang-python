import sqlite3

#connect to the database;if the database not existed, the new one will be created
con = sqlite3.connect('scores.db')
cur = con.cursor()

# cur.execute('CREATE TABLE student (stdno integer, name text, PRIMARY KEY(''stdno''))')
# con.commit()

stdno = 1
name = '王小明'

#qmark style
# cur.execute("insert into student values (?,?);", (stdno, name))

#named style
stdno = 2
name = '王大明'
# cur.execute("insert into student values (:stdno, :name)", {"stdno": stdno, "name": name})

#insert multiple datas
students = [(3, '美美'),
            (4, '胖胖')]
# cur.executemany("insert into student values (?,?);", students)

# con.commit()

#search data
results = cur.execute("select * from student;")
print("return type of the execute function", type(results))

for row in results:
    print('No {}: {}'.format(row[0], row[1]))
print("----------------")

results = cur.execute("select * from student;")
print(results.fetchone())
print(results.fetchall())

con.close()

