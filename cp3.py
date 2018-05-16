while True:
    num = eval(input("점수 : "))
    if (num<=100 and num>=0):
        break
    else:
        print("입력 가능한 점수 범위는 0~100입니다.")

if num<60:
    print(num, ": F")
elif num<70:
    print(num, ": D")
elif num<80:
    print(num, ": C")
elif num<90:
    print(num, ": B")
else:
    print(num, ": A")

