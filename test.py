"""
t = ["a", "b", "c", "d"]
re = ["a", "b", "c", "d"]
i = 1
d = 3
temp = ["a", "b", "c", "d"]

while i < d:
    for j in re[:]:
        temp = temp[temp.index(j[-1])+1:]
        for k in temp:
            re.append(j + k)
        re.remove(j)
        temp = ["a", "b", "c", "d"]
    i += 1

print(re)
print(len(re))
"""
"""
def plzh(lst, d):
    lst = ["a", "b", "c", "d"]
    i = 1
    temp = ["a", "b", "c", "d"]
    while i < d:
        for j in lst[:]:
            temp = temp[temp.index(j[-1]) + 1:]
            for k in temp:
                lst.append(j + k)
            lst.remove(j)
            temp = ["a", "b", "c", "d"]
        i += 1
    return lst

print(plzh(["a", "b", "c", "d"], 2))
"""
def plzh(lst, d):

    #size问题?
    # d-combination
    temp = lst[:]
    countDigit = 0
    re = [""]
    while countDigit < d:
        for elementWaitAdd in re[:]:

            try:
                dot = temp.index(elementWaitAdd[-1])
            except (IndexError, ValueError):
                dot = -1
            temp = temp[dot + 1:]
            #temp = temp[countDigit:]

            for elementToAddOn in temp:
                #if elementWaitAdd != elementToAddOn:
                #    re.append(elementWaitAdd + elementToAddOn)
                re.append(elementWaitAdd + elementToAddOn)
            re.remove(elementWaitAdd)
            temp = lst[:]
        countDigit += 1
    return re if re[0] != "" else []


print(plzh(["a", "b", "c", "d"], 2))
print("abc"[2:0:-1])

a = dict()
a[1] = 1,2
print(a)
