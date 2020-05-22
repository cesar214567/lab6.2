import numpy
file1= open("docs/libro1.txt")
file2= open("docs/libro2.txt")
file3= open("docs/libro3.txt")
file4= open("docs/libro4.txt")
file5= open("docs/libro5.txt")
file6= open("docs/libro6.txt")

stoplist=open("stoplist.txt", encoding='latin-1'  )

data1=file1.read().lower().replace('\n'," ").split(' ')
data2=file2.read().lower().replace('\n'," ").split(' ')
data3=file3.read().lower().replace('\n'," ").split(' ')
data4=file4.read().lower().replace('\n'," ").split(' ')
data5=file5.read().lower().replace('\n'," ").split(' ')
data6=file6.read().lower().replace('\n'," ").split(' ')

stoplist_data=stoplist.read().split("\n")

data1_filtered = list(filter(lambda x : x not in stoplist_data, data1))
data2_filtered = list(filter(lambda x : x not in stoplist_data, data2))
data3_filtered = list(filter(lambda x : x not in stoplist_data, data3))
data4_filtered = list(filter(lambda x : x not in stoplist_data, data4))
data5_filtered = list(filter(lambda x : x not in stoplist_data, data5))
data6_filtered = list(filter(lambda x : x not in stoplist_data, data5))


list_keywords =[]
for word in data1_filtered:
    if word not in list_keywords:
        list_keywords.append(word)
for word in data2_filtered:
    if word not in list_keywords:
        list_keywords.append(word)

for word in data3_filtered:
    if word not in list_keywords:
        list_keywords.append(word)
for word in data4_filtered:
    if word not in list_keywords:
        list_keywords.append(word)
for word in data5_filtered:
    if word not in list_keywords:
        list_keywords.append(word)                

for word in data6_filtered:
    if word not in list_keywords:
        list_keywords.append(word)                


x=len(list_keywords)
y=6
matrix= numpy.zeros((x,y))

for it in data1_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][0]=1

for it in data2_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][1]=1

for it in data3_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][2]=1

for it in data4_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][3]=1

for it in data5_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][4]=1

for it in data6_filtered:
    if (it in list_keywords):
        matrix[list_keywords.index(it)][5]=1

#printeamos la matriz en el archivo "matrix.txt "
out= open("docs/matrix.txt","w+")
out.truncate()
for i in range(x):
    out.write(list_keywords[i]+": ")
    for j in range(y):
        out.write(str(int(matrix[i][j])))
    out.write('\n')





def NOT(array):
    for it in range(len(array)):
        array[it]=not array[it]
    return array     


def AND(array1,array2):
    for it in range(len(array1)):
        array1[it]=array1[it] and array2[it]
    return array1



def L(word):
    if (word not in list_keywords ):
        exit("the word that you are looking for, is not in the text books ")
    num1=list_keywords.index(word)
    temp1=matrix[num1]
    return temp1

def OR(array1,array2):
    for it in range(len(array1)):
        array1[it]=array1[it] or array2[it]
    return array1


print(list_keywords)
print(OR(L("obra"),L("atención")))
print(L('comienza'))
print(AND(OR(L("obra"),L("atención")),L('comienza')))