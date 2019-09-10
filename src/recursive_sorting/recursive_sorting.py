# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
  # we know it takes in two sorted arrays
  # keeps track of total number of elements in given arrays
  elements = len( arrA ) + len( arrB )
  # merged_arr = [0] * elements  <--  throwing me off, so going in dif direction
  merged_arr = [] # setting to empty array instead
  # must loop through both arrays the correct number of times
  # must compare first elements in each array
  # must add smallest element to new array and delete from old array
  a = arrA
  b = arrB
  for i in range(elements):
    # if one array is empty, since it's sorted, we can just add the rest of what's left of the other
    if a == []:
      merged_arr.append(b[0])
      b.pop(0)
    elif b == []:
      merged_arr.append(a[0])
      a.pop(0)
    elif a[0] < b[0]:
      merged_arr.append(a[0])
      a.pop(0)
    else:
      merged_arr.append(b[0])
      b.pop(0)
    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # split each array in half and again until each array has just one element
    if len(arr) > 1:
      mid = len(arr)//2
      c = (arr[:mid])
      d = (arr[mid:])
      
    #eventually merge each piece of the OG array 
    #return merge(c , d)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
