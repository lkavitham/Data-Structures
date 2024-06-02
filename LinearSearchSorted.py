def Search(a,n,searchValue):
    for i in range(n):
        if a[i]>=searchValue:
            if a[i]==searchValue:
                return i
            break
        else:
            return -1

n=int(input("Enter the no. of elements : "))
a=[None]*n
print("Enter the elements in sorted order - ")
for i in range(n):
    a[i]=int(input("Enter the element : "))

searchValue=int(input("Enter the search value  : "))
index=Search(a,n,searchValue)

if index==-1:
    print("Value ",searchValue," not present ")
else:
    print("Value ",searchValue," is present at index",index)