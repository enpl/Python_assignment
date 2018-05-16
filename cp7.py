dic = dict()

def input_to_dic(e_word):
    print("단어를 추가합니다.")
    k_word = input("한글 단어 : ")
    dic[e_word] = k_word

while True:
    e_word = input("영어 단어 : ")
    if e_word == "":
        break
    elif dic == {}:
        print("사전이 비어있습니다.")
        input_to_dic(e_word)
        
    elif e_word not in dic:
        print(e_word, "단어가 등록되어 있지 않습니다.")
        input_to_dic(e_word)
    else:
        print(e_word, ":", dic[e_word])

print(dic)
