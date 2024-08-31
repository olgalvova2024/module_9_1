def sorted(a):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

def correct(a):
    fl = True
    for i in range(len(a)):
        if isinstance(a[i], (int,float)):
            fl = True
        else:
            fl = False
            break
    return fl

def max(a):
    max_ = a[0]
    for i in range(len(a)):
        if a[i] > max_:
            max_ = a[i]
    return max_

def sum(a):
    sum_ = 0
    for i in a:
            sum_ += i
    return sum_


def len(a):
    s = 0
    for i in a:
        s += 1
    return s

def apply_all_func(int_list, *functions):
    if correct(int_list):
        result = {}
        for f in functions:
            result[f.__name__] = f(int_list)
        return result
    else:
        print('Передан некорректный список')
        exit()

print(apply_all_func([4,-1,10,5,0.5,-3,-100], max,min,sorted,sum,len))

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, '15', 9], sorted))

