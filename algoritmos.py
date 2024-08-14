#1
def fat(n):
    if n==1:
        return 1
    return n*fat(n-1)

print(fat(4))

#2
def som(n):
    if n==0:
        return 0
    return n+som(n-1)

print(som(4))

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

#6
def convBase2(n):
    if n==0:
        return ""  
    if n%2==0:
        return convBase2(int(n/2))+"0"
    return convBase2(int(n/2))+"1"

print(convBase2(3))
#9
def findSubStr(str, match):
    if len(str)<len(match):
        return False
    if str[0]==match[0]:
        return True
    if str[0]==match[0]:
        return findSubStr(str[1:len(str)],match[1:len(match)])
    return findSubStr(str[1:len(str)],match)
    
print(findSubStr("eu amo", "choro"))

#10
def nroDigit(n):
    if n<10:
        return 1
    return 1+nroDigit(int(str(n)[1:]))

print(nroDigit(6545))

