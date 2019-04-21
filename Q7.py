# Question No 7
test1=int(input("Enter Your Score For Test 1: "))

test2=int(input("Enter Your Score For Test 2: "))

Mainexam=int(input("Enter Your Score For The Main Exam: "))

Total_score=test1+test2+Mainexam

if test1>25 or test1<0:
    print("Invalid Score")

elif test2>25 or test2<0:
    print("Invalid Score")

elif Mainexam>50 or Mainexam<0:
    print("Invalid Score")

if Mainexam<25:
    print("Fail")
 
elif Total_score>80:
        print("Distintion")
    
elif Total_score >=50 and Total_score<=59:
        print("Pass")

elif Total_score >=60 and Total_score<=79:
        print("Credit")

print("Total Score: ",Total_score)