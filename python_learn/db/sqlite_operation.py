import sqlite3

con = sqlite3.connect('D:/system/SQLite/scores.db')
cur = con.cursor()

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

