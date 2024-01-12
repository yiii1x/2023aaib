motherA = 0
motherB = 0
N = len(s)
a = s[:N//2]
b = s[N//2:]
for c in s:
  if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    motherA += 1
  if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    motherA += 1
for c in b:
  if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    motherB += 1
  if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    motherB += 1
if motherA == motherB: return Ture
else: return Flase