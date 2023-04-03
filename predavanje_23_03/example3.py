# palindrom
word = input("Daj mi riječ da provjerimo jel palilndrom: ")
char_lst = []

# reversing a string:
# word.reverse()
# word[::-1]

# reverse
# for i in word:
    # char_lst.insert(0, i)

i = 0
length = len(word)
while i < length:
    slovo = word[i]
    char_lst.insert(0, slovo)
    i+=1

palindrom = "".join(char_lst)

if word == palindrom:
    print(f"Riječ \"{word}\" JE palindrom!!")
else:
    print(f"Riječ \"{word}\" NIJE palindrom!!")