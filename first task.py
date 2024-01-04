#This is my first task
#First question
for i in range(1,11):
    for n in range(1, i+1):
        print(i*n, end=" ")
    print()
#second question(The score of the student)
term = float(input("enter the term score"))
midterm = float(input("enter the midterm score"))
quiz1 = float(input("enter the quiz1 score"))
quiz2 = float(input("enter the quiz2 score"))
score = (quiz1 + quiz2) * 5 * 0.25 + midterm * 0.25 + term * 0.5
if score >= 90:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
elif score < 60:
    print("E")
#third question
t = 0
for i in range(0, 3):
    for j in range(0,6):
        for k in range(0, 11):
            for m in range(0, 21):
                a = i*500 + j*200 + k*100 + m*50
                if a == 1000:
                    t += 1
                    print(i, "* 500 +", j, "* 200 +", k, "* 100 +", m, "* 50")
print(t)





