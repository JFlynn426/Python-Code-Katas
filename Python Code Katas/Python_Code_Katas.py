def Descending_Order(num):
    list = []
    string = ""
    for number in str(num):
        list.append(number)
    list.sort()
    for char in range (len(list)-1, -1, -1):
        string = string + list[char]
    return int(string)


def row_sum_odd_numbers(n):
    x = 1
    y = 0
    for i in range (1, n):
        x += 2 * i
    for j in range (1, n):
        y += 2 * j
    return (n * x + y)


import math

def is_square(n):
    if n < 0:
        return False
    elif int(math.sqrt(n)) == math.sqrt(n):
        return True
    else:
        return False

def duplicate_count(text):
    text = text.lower()
    SortedString = list(text)
    SortedString.sort()
    count = 0
    i = 0
    while i < len(SortedString) - 1:
        if SortedString[i] == SortedString[i + 1]:
            count += 1
            while SortedString[i] == SortedString[i + 1] and i < len(SortedString) - 2:
                i += 1
        else:
            i += 1
    return count

def countBits(n):
    count = 0
    while n:
        if n % 2 == 0:
            n = n / 2
        else:
            count += 1
            n = n - 1
    return count