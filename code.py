vowels = ['a', 'e', 'i', 'o', 'u', 'y']
newvowels = []
wordlist = []
word = input()
for x in range(0, len(word)):
  wordlist.append(word[x])
  if word[x] in vowels:
    newvowels.append(word[x]) 
y = len(newvowels) - 1
for x in range(0, len(wordlist)):
  if wordlist[x] in newvowels:
    wordlist[x] = newvowels[y]
    y -= 1
print("" . join(wordlist))
