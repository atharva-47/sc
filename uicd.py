# Slip: 1, 5, 11, 15

# Define two fuzzy sets as dictionaries: {element: membership_value}
A = {'a': 0.2, 'b': 0.5, 'c': 0.7}
B = {'a': 0.4, 'b': 0.3, 'c': 0.9}

# Union of A and B: max(A(x), B(x))
union = {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

# Intersection of A and B: min(A(x), B(x))
intersection = {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

# Complement of A: 1 - A(x)
complement_A = {x: 1 - A[x] for x in A}

# Difference A - B: min(A(x), 1 - B(x))
difference = {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in A}

# Cartesian Product: returns a set of tuples ((x, y), min(A(x), B(y)))
def cartesian_product(A, B):
    result = {}
    for x in A:
        for y in B:
            result[(x, y)] = min(A[x], B[y])
    return result

cartesian = cartesian_product(A, B)

# Display Results
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("\nUnion (A ∪ B):", union)
print("Intersection (A ∩ B):", intersection)
print("Complement of A (A'):", complement_A)
print("Difference (A - B):", difference)
print("Cartesian Product (A × B):")
for pair in cartesian:
    print(f"{pair}: {cartesian[pair]}")
