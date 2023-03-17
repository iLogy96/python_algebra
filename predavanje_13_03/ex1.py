# list = [1, 2, 3, 4]


# def findSecondSmallestNum(list):
#     list.remove(min(list))
#     return min(list)


# findSecondSmallestNum(list)

array = [-2, -3, 2, 45, 1, 78, 55, 101, 7]


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[i]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

bubbleSort(array)
print(array)
