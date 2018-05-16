
items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}
total_cost = 0

while True:
    item = input("제품명 : ")

    if item=="":
        break
    elif item not in items:
        print("%s is not in the item list" % (item))
    else:
        total_cost += items[item]
        print("[%s:%d] > %d" % (item, items[item], total_cost))

print("총 급액 :", total_cost)
