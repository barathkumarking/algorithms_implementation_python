array=[22,34,5,74,21,3,65,7,1]
lenght=len(array)

#divide the array and returns the middle position
gap=lenght//2


#checking with the gap value
while(gap>=1):
    j=gap
    while(j<lenght):#iterate through the lenght
        i=j-gap
        while(i>=0):#swap the elements
            if(array[i+gap]>array[i]):
                break
            else:
                temp=array[i+gap]
                array[i+gap]=array[i]
                array[i]=temp
            i=i-gap
        j=j+1
    gap=gap//2


print('Final Result')
print(array)

