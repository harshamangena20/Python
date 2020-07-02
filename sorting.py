import time
class sorting():
    def __init__(self,A):
        self.A=A #intializing the class variable
    def bubblesort(self): 
        start_time=time.time()
        #BubbleSort : Here we check all the numbers and put the highest value in the last till the array is sorted
        #Complexicity : o(n2) -> Worst, Best, Average
        #Advanced : o(n)
        arr=self.A#arr=self.A-> so thath we access the variable
        for i in range(len(arr)): # Looping for ith Element 
            for j in range(len(arr)-i-1): # inner loop from 0 to but one of (n-i)
                if arr[j]>arr[j+1]: # Checking the condition -> Swap
                    # Advanced (if the array is already sorted for first n**2 iterations will stop the forward process) take an flag
                    arr[j],arr[j+1]=arr[j+1],arr[j] 
        end_time=time.time()
        print("Run Time of BubbleSort: ", end_time-start_time)
        return arr
    def selectionsort(self):
        start_time=time.time()
        #SelectionSort : selects the least element from an ith index and swap its position with current index
        #Complexicity : o(n2) -> Worst, Best, Average & suitable for small arrays
        arr=self.A 
        for i in range(len(arr)):# Looping from 0-n
            least=i # intializing the index 
            for j in range(i+1,len(arr)): # inner loop from (i+1)th element to end off the list
                if arr[least]>arr[j]: # Checking the Condition->Swap
                    arr[least],arr[j]=arr[j],arr[least]
        end_time=time.time()
        print("Run time of SelectionSort : ",end_time-start_time)
        return arr 
    def insertionsort(self):
        start_time=time.time()
        #InsertionSort : We'll sort the element as it enters the array, so that assuming array into sorted & unsorted
        #Complexicity : o(n**2)
        #Accurate than BubbleSort & SelectionSort
        #insertionSort > SelectionSort > BubbleSort (All have complexicity : o(n**2))
        arr=self.A
        for i in range(1,len(arr)):
            k=i 
            temp=arr[i] #initializing the current element to temp
            while k>0 and temp < arr[k-1]: # check if current element is less than previous element or not
                #if it is then reduce k to k-1 (less than current index)
                arr[k]=arr[k-1] #So that the k will the k+1 element
                k-=1 
            arr[k]=temp #temp will be the kth indexed element
        end_time=time.time()
        print("Run time of InsertionSort : ",end_time-start_time)
        return arr 
    def sort(self): #MergeSort
        #start_time=time.time()
        #MergeSort is an recurrsive algorithm it is based on Divide - Conquer 
        #Complexicity : o(nlogn)
        arr=self.A 
        if len(arr)>1:
            mid=len(arr)//2# Divide the array based on the mid
            left=arr[:mid] #intialize the divided array(left-part) to left
            right=arr[mid:] #intialize the divided array(left-right) to right
            # N.O.T.E :-  Here we are not passing any arguments to the method sort(mergesort)
            # As it is an recurrsive algorithm we pass left and right as the class instances 
            ls=sorting(left)
            ls.sort()
            rs=sorting(right)
            rs.sort()
            i=j=k=0 # indices for left, right sub arrays , index of array
            while len(left) > i and len(right) > j: # Divide the array so if the element in the left sub array is smaller than the element in the right sub array then a[k] will be left[i] -> increament i & k
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1 
                elif left[i]>right[j]: # Similarly to the right
                    arr[k]=right[j]
                    j+=1 
                k +=1 
            while len(left)>i: # if all elements in right sub array are sorted then we follow up to sort the left sub array
                arr[k]=left[i]
                i+=1 
                k+=1 
            while len(right)>j: # Similarly to right 
                arr[k]=right[j]
                j+=1
                k+=1 
        #end_time=time.time()
        #print("Run time of MergeSort : ",end_time-start_time)
        return arr
        
    def quicksort(self):
        start_time=time.time()
        #Complexicity : o(nlogn) -> best & Average cases
        #Complexicity : o(n) -> worst case
        #Take a pivot sort all elements S.T left array contains the numbers less than pivot & right sub array coontains numbers greater than pivot 
        arr=self.A 
        if len(arr)<=1:
            return arr 
        else:
            pivot=arr.pop() #Taking pivot as last element
        items_greater=[]
        items_less=[]
        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_less.append(item)
        end_time=time.time()
        print("Run time of QuickkSort : ",end_time-start_time)
        return items_less + [pivot] + items_greater
        
        
A=[int(x) for x in input().split()]
o=sorting(A)
print(o.bubblesort())
print(o.selectionsort())
print(o.insertionsort())
print(o.sort())
print(o.quicksort())
