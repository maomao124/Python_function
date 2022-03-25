"""
 * Project name(项目名称)：Python函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 19:31
 * Version(版本): 1.0
 * Description(描述)：
 def 函数名(参数列表):
    //实现特定功能的多行代码
    [return [返回值]]
 """


def getMaxNum(n1, n2):
    """
    获得较大值
    :param n1: 数字1
    :param n2: 数字2
    :return: 较大值
    """
    if n1 > n2:
        return n1
    else:
        return n2


def getMaxByList(a_list):
    """
    获得一个列表的元素最大值
    :param a_list: 列表
    :return: 最大值
    """
    max2 = a_list[0]
    for i in a_list:
        if max2 < i:
            max2 = i
    return max2


if __name__ == '__main__':
    max1 = getMaxNum(3, 6)
    print(max1)
    max1 = getMaxNum(9, 6)
    print(max1)
    max1 = getMaxNum(97.365, 5)
    print(max1)
    max1 = getMaxNum(-698.5, -642.69)
    print(max1)
    max1 = getMaxNum("123", "22")
    print(max1)

    print(getMaxByList([2, 5, 9, 4, 3]))
    print(getMaxByList([2, 5, 9, 99, 3]))
    print(getMaxByList([-78, -6, -9, -123, -8]))
