def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print u'请输入数字：'
x=raw_input();
xx=my_abs(x)

print x+u'的绝对值为：'+ xx

