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
# def plzh(lst, d):

#     #size问题?
#     # d-combination
#     temp = lst[:]
#     countDigit = 0
#     re = [""]
#     while countDigit < d:
#         for elementWaitAdd in re[:]:

#             try:
#                 dot = temp.index(elementWaitAdd[-1])
#             except (IndexError, ValueError):
#                 dot = -1
#             temp = temp[dot + 1:]
#             #temp = temp[countDigit:]

#             for elementToAddOn in temp:
#                 #if elementWaitAdd != elementToAddOn:
#                 #    re.append(elementWaitAdd + elementToAddOn)
#                 re.append(elementWaitAdd + elementToAddOn)
#             re.remove(elementWaitAdd)
#             temp = lst[:]
#         countDigit += 1
#     return re if re[0] != "" else []


# print(plzh(["a", "b", "c", "d"], 2))
# print("abc"[2:0:-1])

# a = dict()
# a[1] = 1,2
# print(a)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
    
if __name__ == '__main__':
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))


    
