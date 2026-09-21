def calculate_avg(scr1, scr2, scr3):
    return (scr1 + scr2 + scr3)

num_students = int(input("how many students are there: "))
for i in range(num_students):
    print("Students", i + 1)

    name = input("Enter your name: ")
    act1 = int(input("Enter your score for Activity 1: "))
    act2 = int(input("Enter your score for Activity 2: "))
    act3 = int(input("Enter your score for Activity 3: "))