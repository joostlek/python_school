def vowels(s):
    vowel = 'aeiouAEIOU'
    for i in range(len(s)):
        if s[i] in vowel:
            print(i)

vowels('Hello WORLD')