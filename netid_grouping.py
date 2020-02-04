import numpy


#Naming of text files - enter file names here
a = "netids.txt"
b = "prefs.txt"

#read in the text file with netids
f = open(a, "r")
lines = f.read().splitlines()
f.close()
#print lines
num_netids =  len(lines)

#read in the text file with preferences
g = open(b, "r")
lines2 = g.read().splitlines()
g.close()
#print lines2
num_groups = len(lines2)

double_groups = []
single_groups = []

num1 = []
num2 = []
num3 = []
num4 = []
num5 = []
num6 = []
num7 = []




#iterate through all of the preferences
for i in lines2:
    values = [len(num1), len(num2), len(num3), len(num4), len(num5), len(num6), len(num7)]
    group = i.replace(",", "")
    group = group.split(" ")

    if len(group) == 5:
        if values[int(group[2])-1] <= values[int(group[3])-1] and values[int(group[2])-1] <= values[int(group[4])-1]:
            if int(group[2]) == 1:
                num1.append(group[0])
                num1.append(group[1])
            if int(group[2]) == 2:
                num2.append(group[0])
                num2.append(group[1])
            if int(group[2]) == 3:
                num3.append(group[0])
                num3.append(group[1])
            if int(group[2]) == 4:
                num4.append(group[0])
                num4.append(group[1])
            if int(group[2]) == 5:
                num5.append(group[0])
                num5.append(group[1])
            if int(group[2]) == 6:
                num6.append(group[0])
                num6.append(group[1])
            if int(group[2]) == 7:
                num7.append(group[0])
                num7.append(group[1])
        if values[int(group[3])-1] <= values[int(group[2])-1] and values[int(group[3])-1] <= values[int(group[4])-1]:
            if int(group[3]) == 1:
                num1.append(group[0])
                num1.append(group[1])
            if int(group[3]) == 2:
                num2.append(group[0])
                num2.append(group[1])
            if int(group[3]) == 3:
                num3.append(group[0])
                num3.append(group[1])
            if int(group[3]) == 4:
                num4.append(group[0])
                num4.append(group[1])
            if int(group[3]) == 5:
                num5.append(group[0])
                num5.append(group[1])
            if int(group[3]) == 6:
                num6.append(group[0])
                num6.append(group[1])
            if int(group[3]) == 7:
                num7.append(group[0])
                num7.append(group[1])

        if values[int(group[4])-1] <= values[int(group[2])-1] and values[int(group[4])-1] <= values[int(group[3])-1]:
            if int(group[4]) == 1:
                num1.append(group[0])
                num1.append(group[1])
            if int(group[4]) == 2:
                num2.append(group[0])
                num2.append(group[1])
            if int(group[4]) == 3:
                num3.append(group[0])
                num3.append(group[1])
            if int(group[4]) == 4:
                num4.append(group[0])
                num4.append(group[1])
            if int(group[4]) == 5:
                num5.append(group[0])
                num5.append(group[1])
            if int(group[4]) == 6:
                num6.append(group[0])
                num6.append(group[1])
            if int(group[4]) == 7:
                num7.append(group[0])
                num7.append(group[1])

    if len(group) == 4:
        if values[int(group[1])-1] <= values[int(group[2])-1] and values[int(group[1])-1] <= values[int(group[3])-1]:
            if int(group[1]) == 1:
                num1.append(group[0])
            if int(group[1]) == 2:
                num2.append(group[0])
            if int(group[1]) == 3:
                num3.append(group[0])
            if int(group[1]) == 4:
                num4.append(group[0])
            if int(group[1]) == 5:
                num5.append(group[0])
            if int(group[1]) == 6:
                num6.append(group[0])
            if int(group[1]) == 7:
                num7.append(group[0])
        if values[int(group[2])-1] <= values[int(group[1])-1] and values[int(group[2])-1] <= values[int(group[3])-1]:
            if int(group[2]) == 1:
                num1.append(group[0])
            if int(group[2]) == 2:
                num2.append(group[0])
            if int(group[2]) == 3:
                num3.append(group[0])
            if int(group[2]) == 4:
                num4.append(group[0])
            if int(group[2]) == 5:
                num5.append(group[0])
            if int(group[2]) == 6:
                num6.append(group[0])
            if int(group[2]) == 7:
                num7.append(group[0])

        if values[int(group[3])-1] <= values[int(group[1])-1] and values[int(group[3])-1] <= values[int(group[2])-1]:
            if int(group[3]) == 1:
                num1.append(group[0])
            if int(group[3]) == 2:
                num2.append(group[0])
            if int(group[3]) == 3:
                num3.append(group[0])
            if int(group[3]) == 4:
                num4.append(group[0])
            if int(group[3]) == 5:
                num5.append(group[0])
            if int(group[3]) == 6:
                num6.append(group[0])
            if int(group[3]) == 7:
                num7.append(group[0])

#splitting preferences into groups of 4:
def splitter(l, n):
    list = [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]
    print list


print "Preference 1:"
splitter(num1, 4)
print "\n"
print "Preference 2:"
splitter(num2, 4)
print "\n"
print "Preference 3:"
splitter(num3, 4)
print "\n"
print "Preference 4:"
splitter(num4, 4)
print "\n"
print 'Preference 5:'
splitter(num5, 4)
print "\n"
print 'Preference 6:'
splitter(num6, 4)
print "\n"
print "Preference 7;"
splitter(num7, 4)
print "\n"
