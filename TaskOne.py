allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,2,3,4]
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter")

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
