def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    
    while low<=high:
        mid=(low + high) // 2
    
        if arr[mid]==key:
            return mid

        elif arr[mid]<key:
            low = mid +1
        
        else:
            high = mid -1
    
    return -1
        
numbers = [10,20,30,40,50,60,70,80]
element = 50
result = binary_search(numbers,element)

if result != -1:
    print("Element found at index: ",result)
else:
    print("Element not found")