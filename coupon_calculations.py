# This program is showing how to calculate the subtotal with the quotient of multiple percentages,
# also along with the discount of a single 5 or 10 dollar off. To get the final price with the discount of
# percentages and cash off.

# Purchasing items
first_name = input("Enter your first name: ")
print(f'Hello {first_name}, and welcome to my store!')
print('I am selling quite a few items.')
print('Those items are laptop, shoes, backpack, poster, textbook')
print('The laptop is $500')
print('The shoes are $85')
print('The backpack is $50')
print('The poster is $25')
print('The text book is $10')
purchase= input("Which item would like to purchase? (laptop, shoes, backpack, poster, textbook)")
if purchase.islower() == "laptop":
    price=500
elif purchase.islower() == "shoes":
    price=85
elif purchase.islower() == "poster":
    price=25
elif purchase.islower() == "textbook":
    price=10
elif purchase.islower() == "backpack":
    price=50
else:
    price=0
    print("Invalid item please restart.")


# Finding shipping price
sub_total = float(input("Please enter the initial cost of your purchase: $"))


if sub_total >= 50:
    print("Your shipping is free")
elif sub_total >= 30:
    print("Your shipping is $11.95")
elif sub_total >= 10:
    print("Your shipping is $7.95")
elif sub_total <= 10:
    print("Your shipping is $5.95")

# asking for cash off coupon

cashCoup = 0
askcash = str(input('Do you have any cash off coupons? yes/no'))
if askcash.islower() == 'yes':
    cashAm = input('Awesome! How much do you have off? (5 or 10?)')
    if cashAm == 5:
        cashCoup = 5
    elif cashAm == 10:
        cashCoup = 10
    elif askcash.islower() == 'no':
        print(f'That is fine! We will move on')

# asking for percent off coupon

percentCoup = 0
askpercent = input('Do you have any percent coupons? yes/no')

if askpercent.islower() == 'yes':
    percentA_m = input('Awesome! How much do you have off? (10, 20, or 30?)')
elif percent_Am == 10:
            percentCoup = 10
elif percent_Am == 20:
            percentCoup = 20
elif percent_Am == 30:
            percentCoup = 30
elif askpercent.islower() == 'no':
    print('That is alright no percent off.')

# calculating order

def calTotal (price, cashCoup, percentCoup):
    afterCash = price - cashCoup
    afterPercent = afterCash - (afterCash * percentCoup / 100)
    afterTax = afterPercent + (afterPercent * 6) / 100

# if/else order calculation

if afterTax <=10:
    newPrice= afterTax+5.95
elif afterTax >10 and afterTax <=30:
    newPrice= afterTax+7.95
elif afterTax >30 and afterTax <=50:
    newPrice= afterTax+11.95
else:
    newPrice= afterTax

finalPrice = calTotal(newPrice, cashCoup, percentCoup)
print('Calculating order total.......')
print('your order total is $" +str(round(finalPrice, 2)))')