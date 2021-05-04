# FIleChlg_v2.py
# A program that reads  a set of first and last names
# and saves it to a different file.
#by S. Allen

def main():

    fname = input('What is the filename? ')
    # this will be Names.txt
    print()

    infile = open(fname, 'r')
    outfile = open('welcome.dat', 'w')


    for line in infile:
       first, last =  line.split()

       

       print('Hello, {0} {1}. Your intials are {2}.{3}.'.format(first,last,
                    first[0].capitalize(),last[0].capitalize()), file=outfile)

    infile.close()
    outfile.close()

    
main()
