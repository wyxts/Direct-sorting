# 直接插入排序
def insert_sort(list):
    # 遍历列表中的所有元素,其中0号索引元素默认已排序,因此从1开始
    for i in range(1, len(list)):
        # 将该元素(j+1)与已排序好的元素(j)从右到左依次比较,如果比该元素(j)小,则交换
        # range(i-1,-1,-1)
        for j in range(i - 1, -1, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == '__main__':
    list = [1, 3, 5, 6, 24, 58, 24, 67, 1, 3, 5]
    insert_sort(list)
    print(list)

