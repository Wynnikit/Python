

#NEW, Trial 2:
        grades = 'ABCDF'

        if len(score) == 2:

            if score[0] <6: letterscore = grades[4]
            elif 6 <= score[0] <7: letterscore = grades[3]
            elif 7 <= score[0] <8: letterscore = grades[2]
            elif 8 <= score[0] <9: letterscore = grades[1]
            else 9 <= score[0]: letterscore = grades[0]

        elif len(score) == 3 : letterscore = grades[0]

        else: letterscore = grades[4]



if int(score)>=90: letterscore = 'A'
elif 80 <= int(score) <90: letterscore = 'B'
elif 70 <= int(score) <80: letterscore = 'C'
elif 60 <= int(score) <70: letterscore = 'D'
else: letterscore = 'F'
    
        
        
        
