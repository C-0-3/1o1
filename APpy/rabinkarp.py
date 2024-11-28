def rabin_karp(text, pattern):

    n = len(text)
    m = len(pattern)
    d = 256  
    q = 101
    pattern_hash = 0
    text_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    result = []

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                result.append(i)

        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q

    return result

text = "ABCCDDAEFG"
pattern = "CDD"
result = rabin_karp(text, pattern)
print(f"Pattern '{pattern}' found at indices: {result}")