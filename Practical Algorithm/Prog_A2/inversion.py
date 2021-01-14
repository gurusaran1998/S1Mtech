# verify the inout integers are within the defined range
def valid_range(n):
    # Checking the length of the array
    if 1<=n<=106:
        list=[]
        # Checking the numbers entered in array within the defined range
        for i in range(0, n):
            a=int(input())
            if 0<=a<=108:
                list.append(a)
            else:
                print("Entered number is not in the given range")
                exit()
        return list
    else:
        print("Length is out of defined range( between 1 and 106)")
        exit()

#Initilize merge sort function
def inversion(array):
    x=mergesort(array,0,len(array)-1)
    return x

 #Function for merge sort
def mergesort(array,l,r):
    x=0
    # Checking if indexes haven't crossed
    if l<r:
        # Getting middle index
        mid=(l+r)//2
        # Recursively calling merge function with left part of array
        x=mergesort(array,l,mid)
        # Recursively calling merge function with right part of array
        x+=mergesort(array,mid+1,r)
        # Calling helper function to merge left and right subarrays
        x+=merge(array,l,mid,r)
    return x

# Helper function to merge two sub arrays
def merge(arr,l,mid,r):
    if (arr[mid]<=arr[mid+1]):
        return 0
    # Initialize count variable for counting no of inversions
    count=0
    #Make copies of both arrays we are trying to merge
    left=arr[l:mid+1]
    right=arr[mid+1:r+1]

    # Initialising indexes for subarrays
    i,j,k=0,0,l

    # Length of left and right subarrays
    len_l=mid+1-l
    len_r=r-mid

    # Comparing two subarrays and check which one is smaller, and then insert the smaller element into the merged array, continue till either of the left array is emptied
    while i<len_l and j<len_r:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1

        else:
            arr[k]=right[j]
            j=j+1
            count+=len_l-i
        k=k+1

    # Copy the rest of the elements that remain in the left array
    while i<len_l:
        array[k]=left[i]
        i=i+1
        k=k+1

    # Copy the rest of the elements that remain in the right array
    while j<len_r:
        array[k]=right[j]
        j=j+1
        k=k+1

    return count

n = int(input())
array=valid_range(n)
result=inversion(array)
print(result)