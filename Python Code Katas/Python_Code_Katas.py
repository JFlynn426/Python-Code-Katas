def Descending_Order(num):
    list = []
    string = ""
    for number in str(num):
        list.append(number)
    list.sort()
    for char in range (len(list)-1, -1, -1):
        string = string + list[char]
    return int(string)
