"""
This function is use to convert a list of integers into its integer representation.
For example, given a list: [8,3,5,1], the output will be 8351.
We could achieve this getting the appropriate digit for each number,
by the example we know that the length of the list will be 4 which means that
the integer will have 4 digits which consist of thousand, hundred, ten, and one.
Thus we will build up our output from that, 8000 + 300 + 50 + 1 = 8351. This
value can be obtain by multiply it with the digit (initially 10 * n-1) and
will be added to the output in each iteration by dividing it by 10 each time.
"""

def convert_to_integer(lst):
    digit = 10 ** (len(lst)-1)  # initialise the digit variable
    num = 0 # set the num variable to 0
    for i in range(0, len(lst)):    # loop through the input lst
        num += (lst[i] * digit)    # add the current value (element at index i in the lst to its digit)
        digit //= 10    # decrease the digit by dividing it by 10
    return num  # return the number

# test cases
print(convert_to_integer([8,3,5,1]))
print(convert_to_integer([6,0,1]))
print(convert_to_integer([0]))
