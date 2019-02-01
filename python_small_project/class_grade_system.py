import os

class_101 = dict()
chinese_score = dict()
math_score = dict()
english_score = dict()

subjects = ["國文","數學","英文"]
scores = [chinese_score, math_score, english_score]

def menu():
    os.system("cls")
    print("Class 101 班級成績管理系統")
    print("----------------------------------------------")
    print("1. 輸入學生姓名")
    print("2. 輸入國文成績")
    print("3. 輸入數學成績")
    print("4. 輸入英文成績")
    print("5. 顯示成績單")
    print("0. 結束程式")
    print("-----------------------------------------------")

def enter_student_data():
    while True:
        no = int(input("座號 (0 ==> 停止輸入):"))
        if no <= 0 or no > 100: break
        name = input("姓名:")
        class_101[no] = name
        print(class_101)

def enter_score(subject_no):
    for no, name in class_101.items():
        inputText = "{}, {} 的{}成績: ".format(no, name, subjects[subject_no])
        scores[subject_no][no] = int(input(inputText))
    print(scores[subject_no])
    x=input("按Enter返回主選單")

def display_score():
    for no in class_101.keys():
        print("{:<5}:".format(class_101[no]), end="")
        sum = 0
        for subject_no in range(0,3):
            sum = sum + scores[subject_no][no]
            score_text = "{}:{:>3}".format(subjects[subject_no], scores[subject_no][no])
            print(score_text, end=" ")
        print("總分:{:>3}, 平均:{:.2f}".format(sum, float(sum)/len(scores)))
    x = input("按Enter返回主選單")

while True:
    menu()
    user_choice = int(input("請輸入您的選擇:"))
    if user_choice == 1:
        enter_student_data()
    elif user_choice == 2:
        enter_score(0)
    elif user_choice == 3:
        enter_score(1)
    elif user_choice == 4:
        enter_score(2)
    elif user_choice == 5:
        display_score()
    else:
        break
print("謝謝您的使用,再見!")