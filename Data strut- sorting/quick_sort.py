#partition to find the pivot and arrange them here pivot is select as the last element in array
def partition(array,low,high):
    i=low-1
    pivot=array[high]

    for j in range(low,high):

        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]

    array[i+1],array[high]=array[high],array[i+1]
    return i+1





#quicksort function to split the array with pivot element
def quicksort(array,low,high):
    if len(array)==1:
        return array
    if low<high:
        pi=partition(array,low,high)

        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)




#program starts here
array= [12,34,1,2,10,5,34,78,23]

lenght=len(array)

quicksort(array,0,lenght-1)

print('Final Result')
print(array)