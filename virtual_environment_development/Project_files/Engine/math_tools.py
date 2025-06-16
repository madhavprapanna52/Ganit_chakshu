import math

def f(i):
    return math.factorial(i)

def factorial_simplification(expression):  # working with simple numbers 
    '''
    Simplifies factorial expression through approach of expansion and cancilation computations and normal computations
    featuring : solving factorial expressiions 
    '''
    nums = expression.split('_')  # integer it 
    print(nums)
    n = int(nums[0])
    x = int(nums[1])
    simple_number = len(nums[0]) <= 2
    print(f'simple_number ; {simple_number}')
    if simple_number:
        deno = (f(x) * f(n-x))
        if deno == 0:
            return 1  # under denominator equates zero
        ans = f(n) / deno
        return ans
    else:
        print('Making efficient way to deal with them ')

j = factorial_simplification('20_10')
print(f'this is the out put : {j}')