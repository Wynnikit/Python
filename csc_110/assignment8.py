#assignment8.py
#module to sort file data into new classes
#by S. Allen


##doesnt need a print statement!  just list with the objects in it!
#-----------------------------------------------------

class Person:

    def __init__(self, name, bizname, overseer):
        self.name = name 
        self.bizname = bizname
        self.overseer = overseer

    #actions
    def chname(self, newname):
        self.name = newname

    def chbiz(self, newbiz):
        self.bizname = newbiz

    def chboss(self, newboss):
        self.overseer = newboss


    #getters
    def getname(self):
        return self.name

    def getbiz(self):
        return self.bizname

    def getmgmt(self):
        return self.overseer

    


class Employee(Person):

    def __init__(self, name, title, bizname, overseer, salary, startdate):
        
        Person.__init__(self, name, bizname, overseer)

        self.title = title
        self.dept = bizname  #bizname becomes dept name
        self.salary = float(salary) #check how to format extra zero
        self.startdate = startdate
    
    #actions
    def chtitle(self, newtitle):
        self.title = newtitle

    def chdept(self, newdept):
        self.dept = newdept

    def chsalary(self, newsal):
        self.salary = float(newsal)

    #getters
    def getTitle(self):
        return self.title

    def getdept(self):
        return self.dept

    def getsal(self):
        return self.salary

    def getstart(self):
        return self.startdate



class Customer(Person):

    def __init__(self, name, bizname, overseer, accnumb, accsize):

        Person.__init__(self, name, bizname, overseer)
        
        self.accnumb = accnumb
        self.accsize = accsize

    #actions
    def chaccnum(self, newnumb):
        self.accnumb = newnumb

    def chsize(self, newsize):
        self.accsize = newsize

    #getters
    def getnumb(self):
        return self.accnumb

    def getsize(self):
        return self.accsize




class BPartner(Person):

    def __init__(self, name, bizname, overseer, biztype):

        Person.__init__(self, name, bizname, overseer)

        self.biztype = biztype #string on what business does

    #action
    def chtype(self, newtype):
        self.biztype = newtype
    
    #getter
    def getbiztype(self):
        return self.biztype
    



def main():
    

    fname = input('What is the filename? ')
        # this will be a8class.dat

    infile = open(fname, 'r')


    #create lists:
    emplist = []
    custlist = []
    bpartlist = []
    pointer = []
    finallist = []

    #pull data out of file
    for line in infile:
        pointer = line.split(',')

        if pointer[0] == 'Employee':
            newperson = Employee(pointer[1],pointer[2],pointer[3],pointer[4],pointer[5],pointer[6])
            emplist.append(newperson)
 
        elif pointer[0] == 'Customer':
            newperson = Customer(pointer[1],pointer[2],pointer[3],pointer[4],pointer[5])
            custlist.append(newperson)

        elif pointer[0] == 'Business Partner':
            newperson = BPartner(pointer[1],pointer[2],pointer[3],pointer[4])
            bpartlist.append(newperson)

        finallist.append(newperson)
        
    #for x in finallist:  ## TEST ONLY
        #print(x.getname())

    infile.close()

    return finallist
    

    

main()


