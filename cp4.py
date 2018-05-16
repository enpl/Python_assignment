grade = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F',\
         0:'F'}

while True:
    num = eval(input("점수 : "))
    if (num<=100 and num>=0):
        break
    else:
        print("입력 가능한 점수 범위는 0~100입니다.")

print(num, ":", grade[num//10])

