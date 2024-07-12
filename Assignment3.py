list = [13,16,48,32,34,62,21,75,35,7]

def avg_finder(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

def even_finder(list):
    container = []
    for i in list:
        if i % 2 == 0:
            container.append(i)
    return container

def avg_even_finder(container):
    sum = 0
    for i in container:
        sum += i
    return sum/len(container)

def my_min(list):
    min = None
    for i in list:
        if min is None or i < min:
            min = i
    return min

def my_max(list):
    max = None
    for i in list:
        if max is None or i > max:
            max = i
    return max

print("Average of the list: ",avg_finder(list))
print("Even in the list: ",even_finder(list))
print("Average of even: ",avg_even_finder(even_finder(list)))
print("Min no.: ",my_min(list))
print("Max no.: ",my_max(list))