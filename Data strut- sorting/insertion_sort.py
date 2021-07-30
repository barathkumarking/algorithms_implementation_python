# insertion sort
a=[5,6,1,2,3,6,5]

#call for loop
for i in range(0,len(a)):
    j=i-1
    temp=a[i]
    while(j>=0 and temp<a[j]): #compare the values andmswap
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp

print(a)



# Time complexity:
# Best case - o(n)
# worst case- o(n^2)
# average case=  o(n^2)

# Space complexity: o(1)