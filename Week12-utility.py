# https://github.com/rkreigler/Week12
# Ryan Kreigler
# CSCI 102 - Section C
# Week 12 - Part B

def PrintOutput(s):
    print("OUTPUT", s)

def LoadFile(filename):
    file = open(filename)
    contents = file.read()
    list = []
    t = 0
    for i in range(len(contents)):
        if contents[i] == "\n":
            list.append(contents[t:i])
            t = i
        elif i == len(contents) - 1:
            list.append(contents[t:i+1])
    for i in range(1,len(list)):
        list[i] = list[i][1:]
    return list

def UpdateString(s1, s2, n):
    s1 = s1[0:n] + s2 + s1[n+1:]
    print("OUTPUT", s1)

def FindWordCount(a, s):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            n = a[i][j:]
            if s in n and n[0:len(s)] == s:
                count += 1
    return count

def ScoreFinder(a, b, s):
    for i in range(len(a)):
        if a[i] == s or a[i].lower() == s:
            print("OUTPUT", a[i], "got a score of", b[i])
            break
        elif i == len(a) - 1:
            print("OUTPUT player not found")

def Union(a, b):
    list = []
    for i in range(len(a)):
        if a[i] not in list:
            list.append(a[i])
    for i in range(len(b)):
        if b[i] not in list:
            list.append(b[i])
    return list

def Intersection(a, b):
    list = []
    for i in range(len(a)):
        if a[i] in b and a[i] not in list:
            list.append(a[i])
    for i in range(len(b)):
        if b[i] in a and b[i] not in list:
            list.append(b[i])
    return list

def NotIn(a, b):
    list = []
    for i in range(len(a)):
        if a[i] not in b:
            list.append(a[i])
    return list
