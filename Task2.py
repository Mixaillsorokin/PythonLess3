# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

Spisok=[2,3,4,5,6,]
compList=[]
ind=0
comp=0
for i in range(len(Spisok)):
    if i < len(Spisok)/2:
        ind=ind-1
        comp=Spisok[i]*Spisok[ind]
        i+=1
        compList.append(comp)


print(f'{Spisok} => {compList}')
