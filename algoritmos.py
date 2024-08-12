


#3
def fib(n):
    if n==0:
        return "0"
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(6))

#4
def entre(k, j):
    if k<j:
        return k+entre(k+1,j)
    if k==j:
        return k
    return k+entre(k-1,j)

print(entre(4,6))

#5
def isPal(s):
    if len(s)==1:
        return True
    if s[len(s)-1]==s[0]:
        return isPal(s[1:len(s)-1])
    return False

print(isPal("ovo"))

#10
def nroDigit(n):
    if n<10:
        return 1
    return 1+nroDigit(int(str(n)[1:]))

print(nroDigit(6545))

