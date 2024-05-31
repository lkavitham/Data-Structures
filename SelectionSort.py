def selection_sort(a):
    # Loop through each element in the list except the last one
    for i in range(len(a)-1):
        minIndex=i
        # Loop through the rest of the list to find the actual smallest element
        for j in range(i+1,len(a)):
            # If a smaller element is found, update minIndex
            if a[j]< a[minIndex]:
                minIndex=j
       # If minIndex is not the same as i, swap the elements
        if i!=minIndex:
            a[i],a[minIndex]=a[minIndex],a[i]
            
            
list1=[6,3,1,5,9,8]
selection_sort(list1)
print(list1)

list2=[2,3,5,39,11,8,9,166,45,23]
selection_sort(list2)
print(list2)

list3=[1,2,3,4,5,6,7,8,9,10]
selection_sort(list3)
print(list3)

list4=[10,9,8,7,6,5,4,3,2,1]
selection_sort(list4)
print(list4)

list5=[4]
selection_sort(list5)
print(list5)