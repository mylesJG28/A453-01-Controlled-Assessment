Task One
=========

Design
========
Creating a currency converter that 
 a) has exchange rates that can be regularly changed by the user.
 b) user should be able to enter an amount, select chosen currnecy, and the currency to convert it into.
 c) figure shown should be to two decimal places.
 
 Currencys required: GBP (Great British Pound) EUR (Euro) USD (US Dollar) JPY (Japanese Yen)

Development
============
Ask for what currency you're asking to covert from
Ask what currency you're converting too
Ask how much you are wanting to convert
print result

From this plan I was going to attempt using python to make this happen
 my first test was as followed:


 var1 = None
 while var1 not in range(len(allowables)):
    print('Please type the currency you wish to convert from')
      for index, currency in enumerate(allowables):
         print ('enter {0} for {1}'.format(index, currency))
     var1 = input("Please type what currency you wish to convert from ")
 var1 = int(var1)

 var2 = None
 while var2 not in range(len(allowables)):
     print('Please type the currencyyou wish to convert to')
     for index, currency in enumerate(allowables):
         print ('enter {0} for {1}'.format(index, currency))
     var2 = input("Please type the currency that you wish to convert to ")
 var2 = int(var2)

 var3 = float(input("Please type the amount of currency you wish to convert "))

 ammount = var3/rates[var1] *rates[var2]
 print(' your converted ammount is {0} {1}'.format(ammount,allowables[var2]))


this works, but I decided to make some changes to make it work better.
in the end I decided on using:

allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,1.7,1.25, 173] #shows exchange rates for each of the currencies
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter") #when it is started this will be shown so they know what it is

def getCurr(dir):
    answer = None
    while answer not in range(len(allowables)):
        print('Please type the currency you wish to convert {0}'.format(dir))
        for index, currency in enumerate(allowables):
            print ('enter {0} for {1}'.format(index, currency))
        answer = input("Please type what currency you wish to convert {0}".format(dir))
    return (answer)    

def getVal(c1, c2, c3):
    
    ammount = c3/rates[c1] *rates[c2]
    return (ammount)

if __name__ == "__main__":
    var1 = getCurr('from')
    var2 = getCurr('to')
    var3 = float(input("Please type the amount of currency you wish to convert "))
    print('Your converted ammount is {0:.2f}{1}'.format(getVal(var1,var2,var3),allowables[var2]))

this test worked, at it worked exactly how i wanted it too.
this test is better because you can see clearly what it is doing and it shows both the currency names and exchange rates.
it also stores the variables to make the result more clear

Evaluation and Testing
===========================
