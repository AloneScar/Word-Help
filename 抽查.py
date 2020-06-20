def ch(words, chinese):
    for i in words:
        pass

e = []
c = []


with open("chinese.txt", "r") as file1:
    for i in file1.readlines:
        if i == "\n":
            break
        c.append(i)

with open("chinese.txt", "r") as file2:
    for i2 in file2.readlines:
        if i2 == "\n":
            break
        e.append(i2)

unit = input("请输入第几单元:")
if unit == "1":
    fu1 = e.index("unit2")
    words = e[0:fu1]
    chinese = c[0:fu1]
else:
    fu1 = e.index("unit"+unit)
    fu2 = e.index("unit"+str(int(unit)-1))
    words = e[fu1:fu2]
    chinese = c[fu1:fu2]
