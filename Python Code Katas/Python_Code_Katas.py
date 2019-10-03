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

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) >= 4:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

def sort_array(source_array):
    sorted_array = sorted([i for i in source_array if i % 2 == 1])
    counter = 0
    for j in range(0,len(source_array)):
        if source_array[j] % 2 == 1:
            source_array[j] = sorted_array[counter]
            counter += 1
    return source_array

def flatten_and_sort(array):
    return_array = []
    for arr in array:
        for value in arr:
            return_array.append(value)
    return_array.sort()
    return return_array

def sockMerchant(n, ar):
    ar.sort()
    i = 0
    count = 0
    while i < n - 1:
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()



def countingValleys(n, s):
    elevation = 0
    count = 0
    for letter in s:
        if letter == 'U':
            elevation += 1
            if elevation == 0:
                count += 1
        else:
            elevation -= 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
