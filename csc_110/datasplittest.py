def main():
    fname = input('What is the filename? ')
        # this will be a8class.dat

    infile = open(fname, 'r')

    
    #for line in infile:
        #x = line.split(',')
        #print(x)

    templist = []

    for line in infile:
        templist = line.split(',')

    print(templist)
    

main()
