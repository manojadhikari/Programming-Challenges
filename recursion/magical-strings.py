'''
Rules: a, e, and i must be followed by the following.
a -> e
e -> a, i
i -> a, e, i
 
input -> n
output -> Number of strings of length n
'''
 
 
def magical_strings_helper(n, cur_str, count):
 if n == 0:
   count += 1
   return count
 for char in cur_str:
   if char == 'a':
     count = magical_strings_helper(n-1, 'e', count)
 
   elif char == 'e':
     count = magical_strings_helper(n-1, 'ai', count)
 
   elif char == 'i':
     count = magical_strings_helper(n-1, 'aei', count)
 
 return count
 
def magical_strings_helper_memo(n, cur_str, memo):
 if n == 1:
   memo[('a', 1)] = 1
   memo[('e', 1)] = 1
   memo[('i', 1)] = 1
   return len(cur_str)
 
 if n == 0:
   return 0
 
 total_count = 0
 for char in cur_str:
   if memo.get((char, n)):
     count = memo.get((char, n))
    
 
   else:
     if char == 'a':
       count = magical_strings_helper_memo(n-1, 'e', memo)
 
     elif char == 'e':
       count = magical_strings_helper_memo(n-1, 'ai',memo)
 
 
     elif char == 'i':
       count = magical_strings_helper_memo(n-1, 'aei', memo)
 
   total_count += count
   memo[(char, n)] = count
 
 return total_count
 
memo = {}
def magical_strings(n):
 if n == 0:
   return 0
 
 magical_strings_helper_memo(n, 'aei',memo)
  return memo[('a', n)] + memo[('e', n)] + memo[('i', n)]
 
 
def prev_num(n):
 if n == 0:
   return 0
 if n == 1:
   return 3
 
 total = 3
 while n > 1:
   total = total + total
   n -= 1
 
 return total
 
 
print(magical_strings(10))
print (prev_num(10))
 
'''
Approaches:
1. #For burte force
#Time: 3^n, Space: 3^n, Depends on your branch factor. Since the largest branch factor is 3, worst-case time and space is 3.
 
3. Memoization
Stopped at 4:18.
 
Have a dictionary with key as (num, char) to the number of strings you can make from there
Time: O(3^n), Space: O(n)
 
4. Dynamic Programming:
#Improvement?
#1 -> 3
#2 -> 6
#3 -> 12
#4 -> 24
#5 -> 48
 
2. #Formula:
if n == 1 return 3
half = prev_num(n-1)
return half + half
Time: O(n), Space: O(1)
 
'''
 
#Dynamic programming approach
def test_dp(n):
 dp = {}
 dp['a'] = 1
 dp['e'] = 1
 dp['i'] = 1
 dp['aprev'] = dp['a']
 dp['eprev'] = dp['e']
 dp['iprev'] = dp['i']
 while n > 1:
   dp['a'] = dp['eprev']
   dp['e'] = dp['aprev'] + dp['iprev']
   dp['i'] = dp['aprev'] + dp['iprev'] + dp['eprev']
 
   dp['aprev'] = dp['a']
   dp['eprev'] = dp['e']
   dp['iprev'] = dp['i']
   n -= 1
  
 return dp['a'] + dp['e'] + dp['i']
 
 
print(test_dp(10))