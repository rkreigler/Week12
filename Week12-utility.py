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
    print(s1)


