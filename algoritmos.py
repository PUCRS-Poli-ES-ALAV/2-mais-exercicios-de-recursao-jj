

def entre(k, j):
    if k<j:
        return k+entre(k+1,j)
    if k==j:
        return k
    return k+entre(k-1,j)

print(entre(4,6))