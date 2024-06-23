
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = i*(result)
    return result
'''print(factorial(4))'''


'''1!=1
2!=2
3!=1*2*3=6
4!=1*2*3*4=24=3!*4
5!=4!*5
n!=(n-1)!*n'''

def facrecursia(n : int) -> int:
    if n==1:
        return 1
    if n > 1:
        result =facrecursia(n-1)*n
        return result
print(facrecursia(5))

