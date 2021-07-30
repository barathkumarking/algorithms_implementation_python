arr=[7,1,5,3,2,8,6]
lenght=len(arr)

for i in range(lenght-2,0,-1):
    for j in range(i+1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)


# Time complexity:
# Best case - o(n)
# worst case- o(n^2)
# average case=  o(n^2)

# Space complexity: o(1)