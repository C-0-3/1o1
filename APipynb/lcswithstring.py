def lcs(s1, s2):
    # Create the LCS matrix
    mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Fill the matrix
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                mat[i + 1][j + 1] = mat[i][j] + 1
            else:
                mat[i + 1][j + 1] = max(mat[i][j + 1], mat[i + 1][j])

    # Print the matrix (optional, for debugging purposes)
    for m in mat:
        print(m)

    # Reconstruct the LCS string
    i, j = len(s1), len(s2)
    lcs_str = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])  # Add character to LCS
            i -= 1
            j -= 1
        elif mat[i - 1][j] > mat[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the list to get the correct order
    lcs_str = ''.join(reversed(lcs_str))
    print(f"LCS: {lcs_str}")

# Test the function
lcs('ELEPHANT', 'RELEVANT')
