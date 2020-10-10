#插入排序，归并排序，快速排序运行时间

# 计时函数
import random
import time
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort

def time(a, sortname):
    time_start = time.time()

    if sortname == 'Insertion':
        insertionSort(a)
    if sortname == 'Merge':
        mergeSort(a)
    if sortname == 'Quick':
        quickSort(a)

    time_end = time.time()
    return (time_end - time_start)


def timeRandomInput(sortname, length, numberOfArrays):
    totalTime = 0
    # 测试数组数
    for i in range(numberOfArrays):
        # 数组大小
        a = []
        for j in range(length):
            # a.append(random.randint(1,10))#1-10的随机整数
            a.append(random.random())  # 0-100的随机浮点数
        totalTime += time(a, sortname)
    return totalTime


if __name__ == '__main__':

    sortname1 = 'Insertion'
    sortname2 = 'Merge'
    sortname3 = 'Quick'

    length = 1000
    numberOfArrays = 10

    print("InsertionSort's total time:")
    print(timeRandomInput(sortname1, length, numberOfArrays))

    print("MergeSort's total time:")
    print(timeRandomInput(sortname2, length, numberOfArrays))

    print("QuickSort's total time:")
    print(timeRandomInput(sortname3, length, numberOfArrays))


