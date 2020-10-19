

list = [45, 20, 11, 50, 17, 45, 50,13, 45]
print(list)
res = max(set(list), key = list.count)
z = list.count(res)
print("ყველაზე ხშირი რიცხვი:",res)
print("რამდენჯერ გამეორდა ხშირად გამოყენებული რიცხვი:",z)