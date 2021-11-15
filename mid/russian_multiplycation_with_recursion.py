def half(n):
    return int(n/2)

def double(n):
    return n * 2

def multiply(left, right, result = 0):
    if left % 2 != 0:
        result = result + right
        right = double(right)
        left = half(left)
    if left % 2 == 0:
        right = double(right)
        left = half(left)
    if left != 0:
        return multiply(left, right, result)
    return result
    
s=multiply(52,5)

print(s)
