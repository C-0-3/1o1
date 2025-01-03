def merge_lists(L1, L2):
    """Merge two sorted lists."""
    merged = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
           
    merged.extend(L1[i:])
    merged.extend(L2[j:])
    return merged

def trim(L, delta):
    """Trim the list L using the parameter delta."""
    trimmed = [L[0]]  # Start with the first element
    last = L[0]
    for y in L[1:]:
        if y > last * (1 + delta):
            trimmed.append(y)
            last = y
    return trimmed

def approximate_subset_sum(S, t, epsilon):
    """Approximate the Subset Sum problem."""
    n = len(S)
    L = [0]  # Initialize with the empty subset
    print(f"Initial L: {L}")

    for i in range(n):
        print(f"\nIteration {i + 1} with element {S[i]}:")
       
        # Create new list with current element added
        new_elements = [x + S[i] for x in L]
        print(f"New elements generated by adding {S[i]}: {new_elements}")
       
        L = merge_lists(L, new_elements)  # Merge the lists
        print(f"Merged L: {L}")

        # Trim the list
        L = trim(L, epsilon / (2 * n))
        print(f"Trimmed L: {L}")

        # Remove elements greater than t
        L = [x for x in L if x <= t]
        print(f"L after removing elements greater than {t}: {L}")

    # Return the largest element in the final list
    result = max(L) if L else 0  # Return 0 if no valid subset found
    print(f"\nFinal result: {result}")
    return result

# Example usage:
S = [1, 4, 5]
t = 9
epsilon = 0.1

result = approximate_subset_sum(S, t, epsilon)
print(f"\nThe approximate subset sum is: {result}")