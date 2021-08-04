array=[23,45,5,3,2,1,57,34,12]#array of elements

#nested for loops to check the condition and make a swap
for i in range(len(array)):
    min = i
    for j in range(i + 1, len(array)):
        if array[min] > array[j]:
            min = j
    array[i], array[min] = array[min], array[i]

print('Final Result')
print(array)