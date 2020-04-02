data1 = [['Rachel', -50],['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]


data1.sort()


def removeLowst(data1):
    result = min(data1, key=lambda x: x[1])
    result = result[1]
    for elements in data1:
        if elements[1]==result:
            data1.remove(elements)
    print(data1)

removeLowst(data1)
def findLowest(data1):
    result = min(data1, key=lambda x: x[1])
    result = result[1]
    for elements in data1:
        if elements[1]==result:
            print(elements[0])
findLowest(data1)


