str1 = input("문자열 : ")

print("개별 문자 출력 : ", end="")

for i in range(len(str1)):
    print(str1[i], end="")

print()


print("역순 개별 문자 출력 : ", end="")

for i in range(len(str1)-1, -1, -1):
    print(str1[i], end="")
