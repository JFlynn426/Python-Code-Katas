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
