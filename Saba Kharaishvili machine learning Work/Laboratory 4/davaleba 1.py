numbs = [21, 34, 152, 33, 55]
# რიცხვების ჯამი
addition = sum(numbs)
print(addition)

# არითმეტიკული საშუალო
arith = sum(numbs) / len(numbs)
print(arith)

# მინიმალური
min = min(numbs)
print(min)

# მაქსიმალური
max = max(numbs)
print(max)

# 102 ის დამატება
numbs.append(102)
print(numbs)

# მესამე ელემენტად ჩასმა
numbs[3] = 205
print(numbs)

# 4_ ელემენტის წაშლა
del numbs[4]
print(numbs)

# ზრდადობა
numbs.sort()
print(numbs)
