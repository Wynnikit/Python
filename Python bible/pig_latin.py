#ask user for sentence

original = input("Please enter a sentence: ").lower().strip()

#convert words in sentence to list

words = original.split()



                                    #print(words[0:5:2])  <- prints x as the part of list(a string) at the position

                                    #for x in range(0,5,2):  <- prints x as an integer position in index
                                        #print(words[x])
                                        #print(x)

#loop thru words and convert sentence into pig latin
new_words = []

#if a vowel begins the word, add -yay
for x in words:  #x being the word from the list
    if x[0] in "aeiou":
        new_word = x + "yay"
        new_words.append(new_word)

#if consonant begins word, add -ay to word
    else:
        vowel_pos = 0  #the vowel's position
        for letter in x:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break     #breaks out of for/while loop,  pass merely skips that element of the list

        cons = x[:vowel_pos]
        the_rest = x[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

#stick words into sentence

output = " ".join(new_words)   # joins all parts of "x" list into new string with spaces between them

#output final string
print(output)


