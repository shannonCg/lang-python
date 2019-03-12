import sqlite3

def menu():
    print("學生資料編輯")
    print("----------------------------------------------")
    print("1. 新增")
    print("2. 編輯")
    print("3. 刪除")
    print("4. 顯示所有學生")
    print("0. 結束")
    print("-----------------------------------------------")

def append_data():
    while True:
        no = int(input("請輸入學生座號(-1 停止輸入):"))
        if -1 == no:
            break
        name = input("請輸入學生姓名:")
        existed_student = conn.execute('select * from student where stdno = :stdno', {'stdno':no}).fetchall()
        if len(existed_student) > 0:
            print("您輸入的座號已經有資料了")
        else:
            conn.execute('insert into student values (?,?)', (no, name))
            conn.commit()

def edit_data():
    no = int(input("請輸入要編輯的學生座號:"))
    existed_student = conn.execute('select * from student where stdno = :stdno', {'stdno': no}).fetchall()
    if len(existed_student) > 0:
        print("目前的學生姓名:", existed_student[0][1])
        name = input("請輸入學生姓名:")
        conn.execute('update student set name = :name where stdno = :stdno', {'stdno': no, 'name': name})
        conn.commit()
    else:
        print("找不到要編輯的學生座號")

def del_data():
    no = int(input("請輸入要刪除的學生座號:"))
    existed_student = conn.execute('select * from student where stdno = :stdno', {'stdno': no}).fetchall()
    if len(existed_student) > 0:
        print("你目前要刪除的是座號 {} 的 {}".format(existed_student[0][0], existed_student[0][1]))
        answer = input('確定要刪除嗎? (y/n)')
        if 'y' == answer.lower():
            conn.execute('delete from student where stdno = :stdno', {'stdno': no})
            conn.commit()
            print("已刪除指定的學生...")
    else:
        print("找不到要刪除的學生座號")

def disp_data():
    existed_student = conn.execute('select * from student').fetchall()
    for student in existed_student:
        print('No {}: {}'.format(student[0], student[1]))


conn = sqlite3.connect('D:/system/SQLite/scores.db')

while True:
    menu()
    user_choice = int(input("請輸入您的選擇:"))
    if user_choice == 1:
        append_data()
    elif user_choice == 2:
        edit_data()
    elif user_choice == 3:
        del_data()
    elif user_choice == 4:
        disp_data()
    elif user_choice == 0:
        break
    else:
        break
    x = input("請按Enter鍵回主選單")
print("謝謝您的使用,再見!")