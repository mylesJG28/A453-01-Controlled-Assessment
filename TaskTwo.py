#answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ") #raw_input will save this

addresses = []
surnames = []

def ask(item):
    answer = raw_input("what is the persons {0}?".format(item))
    return (answer)

def getAddresses(): # takes the addresses
    with open('addressbook.csv') as book: #opens the address book ready to stroe the information in it 
        data = book.read()#stores data in it
        for line in data.split('\r\n'):
            address = line.split(',')
            addresses.append(address)
            
def getSurnames():
    for item in addresses:
        surnames.append(item[0])

def getRecord(surname):
    if surname in surnames:
        for item in addresses:
            if item[0] == surname:
                return (item)
    else:
        return ('no record found')

if __name__ == '__main__':        
    '''
    This allows us to run automated tests without requiring the user inputs
    '''
    getAddresses()
    getSurnames()
    answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ")
    if answer == "1" :
        print ("This is where we create a new entry")
        lastname = raw_input("What is the persons last name?")
        firstname = raw_input("What is the persons last name?")
        phone = raw_input("What is the persons phone number?")   
        email = raw_input("What is the persons email address?")
        address = raw_input("What is the persons address?")
    
    if answer == "2" :
        print ("This is where we search")
        searchcriteria = raw_input("Enter your search Criteria: Name, Phone Number, Address, Email, Postcode, or Town ")
        print searchcriteria
        temp1 = open("addressbook.csv","r")
        for line in temp1:
            if searchcriteria in line:
                print line 
            else:
                print ("No results found")

# lastname = ask('lastname')
# fisrstname = ask('first name')

    
# if answer == "1" : 
  

#     lastname = raw_input("What is the persons last name?")
#     firstname = raw_input("What is the persons last name?")
#     phone = raw_input("What is the persons phone number?")
#     email = raw_input("What is the persons email address?")
#     address = raw_input("What is the persons address?")

#     #create or append addressbookdata

#     temp1 = open("addressbookdata","a")
    
#     #create string to print to file
#     #print temp1
#     #print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address) 

#     temp1.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
#     temp1.write("\n")

# # SEARCHING FOR A RECORD

# elif answer == "2" :
#     print ("This is where we search")
#     searchcriteria = raw_input("Enter your search Criteria: Name, Phone Number, Address, Email, Postcode, or Town ")
#     print searchcriteria
#     temp1 = open("addressbookdata","r")
#     for line in temp1:
#         if searchcriteria in line:
#             print line 
#         else:
#             print ("No results found")


# #This means that the user chose neither of the options
# else:
#     print ("Incorrect Answer")
#     exit()