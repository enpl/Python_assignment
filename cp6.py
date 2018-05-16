dic = dict()

while True:
    e_word = input("영어 단어 : ")
    k_word = input("한글 단어 : ")

    if e_word == "":
        break

    else:
        dic[e_word] = k_word


print(dic)
