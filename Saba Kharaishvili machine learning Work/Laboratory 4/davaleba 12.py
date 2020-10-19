
x = int(input('რანდომ რიცხვი >: '))

print("მთლიანი რიცხვი არის " + str(x))
res = [int(i) for i in str(x)]

print("დაყოფილი რიცხვის სია " + str(res))
print('სიის ჯამი',sum(res))