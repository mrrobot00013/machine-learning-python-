
# კენტის ამოშლა

numbers = [14, 33, 34, 135, 2, 57, 12, 155, 1002, 46, 51]
def remove(l):
    for i in numbers:
        if i % 2:
            l.remove(i)
    return l
print(remove((numbers)))