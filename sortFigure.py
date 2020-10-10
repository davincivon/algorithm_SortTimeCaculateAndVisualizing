#插排，快排，归并消耗时间可视化对比

import matplotlib.pyplot as plt
import random

#计时
def time(a, sortname):
    import time
    from insertionSort import insertionSort
    from mergeSort import mergeSort
    from quickSort import quickSort
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

#生成折线图
def timeFigure(name_lis,time_lis):
    x=name_lis
    y=time_lis
    plt.plot(x, y, linewidth=4)

    # 设置图表标题，并给坐标轴添加标签
    plt.title("Sort Method Compare",fontsize=20)
    plt.xlabel("sort method", fontsize=12)
    plt.ylabel("time", fontsize=12)

    # 设置坐标轴刻度标记的大小
    plt.tick_params(axis='both',labelsize=10)
    plt.show()

if __name__ == '__main__':

    sortname1 = 'Insertion'
    sortname2 = 'Merge'
    sortname3 = 'Quick'
    name_lis=['InsertionSort','MergeSort','QuickSort']

    length = 1000
    numberOfArrays = 10


    time_insert=timeRandomInput(sortname1, length, numberOfArrays)
    time_merge=timeRandomInput(sortname2, length, numberOfArrays)
    time_quick=timeRandomInput(sortname3, length, numberOfArrays)

    time_lis=[]
    time_lis.append(time_insert)
    time_lis.append(time_merge)
    time_lis.append(time_quick)
    timeFigure(name_lis,time_lis)
#    timeFigure(sortname2,time_merge)
#    timeFigure(sortname3,time_quick)

