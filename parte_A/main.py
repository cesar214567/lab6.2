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


print(list_keywords)
y=len(list_keywords)
x=6
print(len(list_keywords))
matrix= numpy.zeros((y,x))
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


def NOT(word:str):
    if word not in list_keywords:
        exit("the word that you are looking for, is not in the text books ")
    num=list_keywords.index(word)
    temp =  matrix[num]
    for it in range(len(temp)):
        temp[it]=not temp[it]
    return temp     

def AND(word1:str,word2:str):
    if (word1 not in list_keywords or word2 not in list_keywords):
        exit("the word that you are looking for, is not in the text books ")
    num1=list_keywords.index(word1)
    num2=list_keywords.index(word2)
    temp1=matrix[num1]
    temp2=matrix[num2]
    for it in range(len(temp1)):
        temp1[it]=temp1[it] and temp2[it]
    return temp1

def OR(word1:str,word2:str):
    if (word1 not in list_keywords or word2 not in list_keywords):
        exit("the word that you are looking for, is not in the text books ")
    num1=list_keywords.index(word1)
    num2=list_keywords.index(word2)
    temp1=matrix[num1]
    temp2=matrix[num2]
    for it in range(len(temp1)):
        temp1[it]=temp1[it] or temp2[it]
    return temp1


print(list_keywords)
print(OR("obra","atención"))