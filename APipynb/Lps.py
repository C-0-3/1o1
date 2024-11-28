def lps(pat):
    LPS = [0] * len(pat)
    i = 0
    j = 1
    LPS[0] = 0
    while j < len(pat):
        if pat[i] == pat[j]:
            LPS[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                LPS[j] = 0
                j += 1
            else:
                i = LPS[i - 1]
    return LPS
pat = "abcdababa"
LPS = lps(pat)
print(LPS)
    

