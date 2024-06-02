def binary_search(a,n,searchValue):
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2
        if searchValue<a[mid]:
            last=mid-1
        elif searchValue>a[mid]:
            first=mid+1
        else:
            return mid
    return -1

n=int(input("Enter the no. of elements : "))
a=[None]*n
print("Enter the elements in sorted order ")
for i in range(n):
    a[i]=int(input("Enter element : "))
a.sort()
searchValue=int(input(("Enter the search value : ")))
index=binary_search(a,n,searchValue)

if index == 1:
    print("Value ",searchValue," not present")
else:
    print("Value",searchValue," present at the index",index)
