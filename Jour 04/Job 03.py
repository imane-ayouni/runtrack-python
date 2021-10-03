n = input("Choose a number ")
x=3
def Power(n):
    if n == 1:
        return x
    else:
        return (x * Power(int(n)-1))
print(x, " to the power of ", n , " is ", Power(n))