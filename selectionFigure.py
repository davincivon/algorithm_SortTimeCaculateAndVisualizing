#selection问题消耗时间可视化
#selection问题（快排和减治）
# 划分操作辅助函数
def split(lis, first, last):
    pivot = lis[first]

    left = first
    right = last
    while left < right:
        while pivot < lis[right]:
            right = right - 1
        while left < right and (lis[left] < pivot or lis[left] == pivot):
            left = left + 1
        if left < right:
            lis[left], lis[right] = lis[right], lis[left]
    # 确定好基准位置
    pos = right
    lis[first] = lis[pos]
    lis[pos] = pivot
    return pos

#快速排序
def quicksort(lis, first, last):
    if first < last:
        pos = split(lis, first, last)
        quicksort(lis, first, pos-1)
        quicksort(lis, pos+1, last)
    return lis

#减治
def k_find(lis, k):
    pivot = lis[len(lis) // 2]
    left = 0
    right = len(lis) - 1

    lis[0], lis[len(lis) // 2] = lis[len(lis) // 2], lis[0]
    while left < right:
        while pivot < lis[right]:
            right = right - 1
        while left < right and (lis[left] < pivot or lis[left] == pivot):
            left = left + 1
        if left < right:
            lis[left], lis[right] = lis[right], lis[left]
    # 确定好基准位置
    pos = right
    lis[0] = lis[pos]
    lis[pos] = pivot

    count = pos + 1
    if count == k:
        return pivot
    elif count > k:
        return k_find(lis[0:pos], k)
    else:
        return k_find(lis[pos:], k - pos)

#生成折线图
def timeFigure(name_lis,time_lis):
    import matplotlib.pyplot as plt

    x=name_lis
    y=time_lis
    plt.plot(x, y, linewidth=4)

    # 设置图表标题，并给坐标轴添加标签
    plt.title("Decrease And QuickSort Compare",fontsize=20)
    plt.xlabel("sort method", fontsize=12)
    plt.ylabel("time", fontsize=12)

    # 设置坐标轴刻度标记的大小
    plt.tick_params(axis='both',labelsize=10)
    plt.show()


if __name__ == "__main__":
    import random
    import cProfile

    #     产生100000个随机数组
    num = 100000
    #     array = [random.randint(1, 1000) for i in range(num)]
    array = []
    a = 1
    for i in range(num):
        a = a + (random.random()*100)
        array.append(a)

    # 乱序操作
    random.shuffle(array)
    random.shuffle(array)

    import copy

    # 进行一个深度拷贝，用于测试
    arraycopy = copy.deepcopy(array)

    #     用O(n)的算法得到第k小的数
    k = 4999

    import time

    name_lis=['decrease','quickSort']
    time_lis=[]
    starttime = time.time()
    n = k_find(array, k)
    endtime = time.time()
    decrease_time=endtime-starttime

    time_lis.append(decrease_time)
    # print("使用线性查找的时间为:",decrease_time)
    # print("查找得到的数为:", n)

    starttime = time.time()
    quicksort(arraycopy, 0, len(arraycopy) - 1)
    endtime = time.time()
    quick_time=endtime-starttime

    time_lis.append(quick_time)

    timeFigure(name_lis,time_lis)
    # print("使用快排查找的时间为:", quick_time)
    # print("查找得到的数为:", arraycopy[k - 1])
    #
    # print(time_lis)