
def union(A, B):
    Y = {}
    for x in A:
        Y[x] = max(A[x], B[x])
    return Y
def intersection(A, B):
    Y = {}
    for x in A:
        Y[x] = min(A[x], B[x])
    return Y

def complement(A):
    Y = {}
    for x in A:
        Y[x] = round(1 - A[x],2)
    return Y

def difference(A, B):
    Y = intersection(A, complement(B))
    return Y   

def cartesian_product(A, B):
    Y = {}
    for x in A:
        for y in B:
            Y[(x,y)] = min(A[x], B[y])
    return Y


A = {'a' : 0.2 , 'b': 0.5, 'c': 0.8}
B = {'a' : 0.4 , 'b': 0.1, 'c': 0}


print(difference(A, B))
print("\n")
print(complement(B))
print(union(A, B))
print("\n")
print(intersection(A, B))
print("\n")
Y = cartesian_product(A, B)
for x in Y:
    print(x,":", Y[x]," \n" )
