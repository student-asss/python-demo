# 6.1.

def sumFirst100():
    ret = 0
    for i in range(100):
        ret += i
    print(ret)

sumFirst100()

# 6.2.

def sumFirst100(n):
    ret = 0
    for i in range(n):
        ret += i
    print(ret)

sumFirst100(101)

# 6.3.

def sumFirstN(n):
    ret = 0
    for i in range(n):
        ret += i
    return ret

print(sumFirstN(101))  # The first way of call

suma = sumFirstN(101) # The second way of call
print(suma)

# 6.4.

def entriesLists(n):
    list = []
    for i in range(n):
        listMember = input("> ")
        list.append(listMember)
    return list

list = entriesLists(5)
print(list)

# 6.5.

def entryNumber(comment):
    number = int(input(comment))
    return number

number = entryNumber("> ")
print(number)

# 6.6.

def averageListValue(list):
    listSize = len(list)
    sum = 0
    for i in list:
        sum += i
    return sum/listSize

list = [1, 2, 3, 4, 5]
value = averageListValue(list)
print(value)

# 6.7.

def maxListValue(list):
    max = list[0]
    for i in list:
        if max < i:
            max = i
    return max

def minListValue(list):
    min = list[0]
    for i in list:
        if min > i:
            min = i
    return min

list = [1, 2, 3, 4, 5, 6, 7]
maxValue = maxListValue(list)
print(maxValue)
minValue = minListValue(list)
print(minValue)

# 6.8.

def squareNumber(number):
    square = number * number
    return square

result = squareNumber(4)
print(result)

# 6.9.

def sortList(list):
    n = len(list)
    for i in range(n):
        for j in range(i, n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

list = [1, 2, 3, 4, 5, 6]
value = sortList(list)
print(value)

# 6.10.

TAX = 20
def inputProfit():
    profit = int(input("Enter profit: "))
    return profit

def taxOnProfit(profit):
    tax = profit * TAX/100
    return tax

def printOnScreen(tax):
    print("Tax: " + str(tax))

profit = inputProfit()
tax = taxOnProfit(profit)
printOnScreen(tax)

    
    
    






