
# ნებისმიერი სიის ელემენტების ნამრავლი

list2 = [23, 32, 51, 14]
list3 = [56, 1, 15, 46, 0]
list1 = [2, 3, 5, 1]

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply(list1))
print(multiply(list2))
print(multiply(list3))