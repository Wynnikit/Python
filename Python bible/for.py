#for number in range(1,11, 2):
   # print(number)


#vowels = 0
#consonants = 0

#for letter in "supercalifragilisticexpialidocious":
 #   if letter.lower() in "aeiou":
 #       vowels = vowels + 1
  #  elif letter == " ":
   #     pass
    #else:
     #   consonants = consonants + 1

#print("There are {} vowels".format(vowels))
#print("There are {} consonants".format(consonants))





students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "a"in name:
            print(name)
