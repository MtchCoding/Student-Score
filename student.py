def calculate_avg(scr1, scr2, scr3):
    return (scr1 + scr2 + scr3) / 3

num_students = int(input("how many students are there: "))
for i in range(num_students):
    print("Student: ", i + 1)

    name = input("Enter your name: ")
    act1 = float(input("Enter your score for Activity 1: "))
    act2 = float(input("Enter your score for Activity 2: "))
    act3 = float(input("Enter your score for Activity 3: "))

    avg = calculate_avg(act1, act2, act3) 

    if avg >= 90:
        msg = "Great Job"
    elif avg >= 80: 
        msg = "Good Job"
    elif avg >= 70:
        msg = "You can do Better next time"
    else:
        msg = "You Failed, Please work harder next time"


    print("_______________________________________")
    print(msg) 
    print("Average", round(avg, 2))
    print("Student: ", i + 1 )
    print("_______________________________________\n")