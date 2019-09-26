'''
Find a total number of overlapping squares in a given gird.
**
**
-> 4 + 1 = 5

***
***
-> 6 + 2 -> 8

**_
***
***

->8+3 = 11


#of individual squares +

'''

def overlapping_squares(input):
    rowLen = len(input)
    colLen = len(input[0])

    result = 0
    A = [[0]*colLen for row in range(rowLen)]
    print(A)

    for row in range(rowLen):
        for col in range(colLen):
            if not input[row][col]:
                continue

            top = A[row-1][col] if row > 0 else 0
            left = A[row][col-1] if col > 0 else 0
            top_left = A[row-1][col-1] if (row > 0 and col >0) else 0
            A[row][col] = 1 + min(top, min(left, top_left))
            result += A[row][col]

    return result



    return -1

input = [[1,1],[1,1]]
print(overlapping_squares(input))

input = [[1,1,0],[1,1,1],[1,1,1]]
print(overlapping_squares(input))
