#LCS

def lcs(s1, s2):
    mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                mat[i + 1][j + 1] = mat[i][j] + 1
            else:
                mat[i + 1][j + 1] = max(mat[i][j +1], mat[i + 1][j])

    for m in mat:
        print(m)

lcs('ELEPHANT', 'RELEVANT')
