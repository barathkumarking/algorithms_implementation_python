array=[90,14,1320,23,167,34,56,78]
lenght=len(array)


#get the max number to find the largest digit
max_num =max(array)
limit=1

#compute the largest decimal point that is 1's 10's 100's place
while(max_num>0):
    max_num=max_num//10
    limit=limit*10
limit=limit


#sorting according to the decimal places
b=10
while(b<=limit):
    for i in range(lenght):
        for j in range(0,lenght):
            if (array[j]%b) > (array[i]%b):
                temp=array[j]

                array[j]=array[i]
                array[i]=temp
    b=b*10
    print("%d 's place result:"%(b//100)) # print result of each iteration
    print(array)
    print('')


#printing the final result
print('Final Result')
print(array)

