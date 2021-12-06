vowels = ['a', 'e', 'i', 'o', 'u']
string = input("Enter a string: ")
prev_vowel = False
for i in range(len(string)):
    if string[i] in vowels:
        if prev_vowel:
            print(i+1)
            break
        else:
            prev_vowel = True
