'''Given two arrays of integers, Find a pair of values (one value from each arrays) that you can swap to give each arrays the same sum.
'''
#This is approach 2

def exists(target, arr):
 start = -1
 end = len(arr)

 while start + 1 < end:
   mid = (start + end) // 2
   if arr[mid] == target:
     return True
   elif(arr[mid] < target):
     start = mid
   else:
     end = mid
 return False



def sum_swap(arr1, arr2):
 sum1 = sum(arr1)
 sum2 = sum(arr2)

 if(sum1%2 != sum2%2):
   return None
 mid = (sum1 + sum2) // 2
 arr2.sort()

 for num1 in arr1:
   target = mid - (sum1 - num1)
   if exists(target, arr2):
     return (num1, target)

 return None

'''
Test:
[4, 1, 2, 1, 1, 2]    [3, 6, 3, 3]
11                      15
Mid = 13
sum1 - num1 + num2 = Mid -> Can Swap
3+1 = 4

-> (1,3)

Approaches:
1. Naive Approach: Calculate sum1 and sum2. Nested loop through both arrays to see which pairs can be swapped. O(n^2)

 sum1 = sum(arr1)
 sum2 = sum(arr2)
 for num1 in arr1:
   for num2 in arr2:
     if (sum1 - num1 + num2) == (sum2 - num2 + num1):
       return (num1, num2)

 return None


2. Does Sorting help? O(nlogn) time. O(1) space
 1 1 1 2 2 4             3 3 3 6
 3 ->

#If you sort both arrays, more efficient than what’s implemented above. Target = (sum1 - sum2) / 2
while (i < len(arr1) and j < len(arr2)):
 a = arr1[i]
 b = arr2[j]

 difference = a - b

 if difference == target:
   return (a, b)
 elif difference < target:
   i += 1
 else:
   j += 1


3. Extra Space: Keep set2 = set(arr2). Check to see if target exist in set2. What's target?
     target = mid - (sum1 - num1)
     If we have sum2=17 and sum1 = 16, mid can't exist.

     O(n) time and O(n) space

 sum1 = sum(arr1)
 sum2 = sum(arr2)

 if(sum1%2 != sum2%2):
   return None
 mid = (sum1 + sum2) // 2
 set2 = set(arr2)

 for num1 in arr1:
   target = mid - (sum1 - num1)
   if target in set2:
     return (num1, target)

 return None
'''

result = sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])
print(result)


#Check exists function
# result = exists(4, [1,2,3,4])
# print (result)
'''
If this is called multiple times and we have a preprocessing step above, how can we make it more efficient?
-> Approach 2 where both arrays come in sorted and you traverse through them rather than having to sort arrays every time

If arrays were sorted, approach 2 gives O (n+m) time. We can’t do better because we have to look at every pair in worst case.

'''
