def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print("实时求和函数，直接返回结果值：", calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("延时求和函数，直接返回函数：", f1)

f = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(":", f == f1)
print("延时求和函数：", f)
print("延时求和函数结果：", f())
