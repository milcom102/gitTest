#-*-coding:utf-8-*-



b = ["a","b","c"]
len_1 = b.__len__()
for i in range(len_1):
    del b[0]
    print b