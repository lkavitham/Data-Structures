def insertion_sort(a):
    # Start from the second element (index 1) because the single element at index 0 is sorted
    for i in range(1,len(a)):
        # Store the current element to be compared
        temp=a[i]
        # Initialize j to the index of the element just before the current element
        j=i-1
        # Move elements of a[0..i-1], that are greater than temp, to one position ahead of their current position
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j=j-1
            # Place temp (the original a[i]) into its correct location
        a[j+1]=temp



list1=[6,3,1,5,9,8]
insertion_sort(list1)
print(list1)

list2=[2,3,5,39,11,8,9,166,45,23]
insertion_sort(list2)
print(list2)

list3=[1,2,3,4,5,6,7,8,9,10]
insertion_sort(list3)
print(list3)

list4=[10,9,8,7,6,5,4,3,2,1]
insertion_sort(list4)
print(list4)

list5=[4]
insertion_sort(list5)
print(list5)