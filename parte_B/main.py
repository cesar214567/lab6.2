import numpy
import pandas as pd
import csv
file1= open("../docs/libro1.txt")
file2= open("../docs/libro2.txt")
file3= open("../docs/libro3.txt")
file4= open("../docs/libro4.txt")
file5= open("../docs/libro5.txt")
file6= open("../docs/libro6.txt")

stoplist=open("../stoplist.txt", encoding='latin-1'  )

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

lista = {}
diccionario = {}
alr = {}
for word in data1_filtered:
    diccionario[word] = 0
    alr[word] = 0
    lista[word] = []
    

for word in data2_filtered:
    diccionario[word] = 0
    alr[word] = 0
    lista[word] = [] 
    
for word in data3_filtered:
    diccionario[word] = 0
    alr[word] = 0
    lista[word] = [] 
    
for word in data4_filtered:
    diccionario[word] = 0
    alr[word] = 0
    lista[word] = [] 
    
for word in data5_filtered:
    diccionario[word] = 0        
    alr[word] = 0
    lista[word] = [] 
    

for word in data6_filtered:
    diccionario[word] = 0        
    alr[word] = 0
    lista[word] = [] 
    
for word in data1_filtered:
    diccionario[word] += 1
    if alr[word] == 0:
        lista[word].append(1)
        alr[word] = 1

for word in data2_filtered:
    diccionario[word] += 1
    if alr[word] <= 1:
        lista[word].append(2)
        alr[word] = 2

for word in data3_filtered:
    diccionario[word] += 1
    if alr[word] <= 2:
        lista[word].append(3)
        alr[word] = 3

for word in data4_filtered:
    diccionario[word] += 1
    if alr[word] <= 3:
        lista[word].append(4)
        alr[word] = 4

for word in data5_filtered:
    diccionario[word] += 1       
    if alr[word] <= 4:
        lista[word].append(5)
        alr[word] = 5

for word in data6_filtered:
    diccionario[word] += 1        
    if alr[word] <= 5:
        lista[word].append(6)
        alr[word] = 6

sorted_lista = sorted(diccionario.items(), key=lambda kv: kv[1],reverse = True)

i =  0
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)
for word in sorted_lista:
    palabra =  word[0] + ", " + str(word[1]) + ", "
    for arc in lista[word[0]]:
        palabra += str(arc) + ", "
    #print(palabra)
    csvWriter.writerow([palabra])
    if(i == 99):
        break
    i += 1


def NOT(array):
    arr = []
    for i in range(1,7,1):
        if(i not in array):
            arr.append(i)
    return arr

def AND(array1,array2):
    arr = []
    for x in array1:
        if x in array2:
            arr.append(x)
    return arr

def L(word):
    if (not lista[word]):
        exit("the word that you are looking for, is not in the text books ")
    return lista[word]

def OR(array1,array2):
    arr = array1
    for x in array2:
        if x not in arr:
            arr.append(x)
    return arr

print(OR(L("obra"),L("atención")))
print(L('comienza'))
print(NOT(L('comienza')))
print(AND(OR(L("obra"),L("atención")),L('comienza')))
