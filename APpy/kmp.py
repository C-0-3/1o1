def Lps(pattern):
  lps = [0] * len(pattern)
  i = 0
  j = 1
  while j < len(pattern):
    if pattern[i] == pattern[j]:
      lps[j] = i + 1
      i += 1
      j += 1
    else:
      if i != 0:
        i = lps[i - 1]
      else:
        lps[j] = 0
        j += 1
  return lps

def kmp(pat, txt):
  lps = Lps(pat)
  i = 0 
  j = 0 
  matches = []

  while i < len(txt):
    if pat[j] == txt[i]:
      i += 1
      j += 1
    if j == len(pat):
      matches.append(i - j)
      j = lps[j - 1]
    elif i < len(txt) and pat[j] != txt[i]:
      if j != 0:
        j = lps[j - 1]
      else:
        i += 1

  return matches

txt = "ABAABCABAABABAE"
pat = "ABAABABA"
matches = kmp(pat, txt)

print("LPS:", Lps(pat))
print("Pattern found at indices:", matches)

