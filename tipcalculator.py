...
As the finance officer of Asanka Hotel, the food and beverages director has requested a program that calculates the total amount of a meal purchased with a fixed tip. 

Below are the requirements for the program:

The program should ask the user to enter the charge for the food.
It should then calculate the amounts of an 18 percent tip and 7 percent sales tax on the charge of the food and display each of these amounts.
Finally, it should add everything together and display the charge of the food plus tip and sales tax.
Based on this data, your program should generate script that meets the requirements. 
...

#Below is an example execution of the program: 
#input
#Charge for food = $50.00
#output
#Tip = $9.00         0.18 x 50
#Sales tax = $3.50   0.07 x 50
#Grand total = $62.50

chargeForFood = input("kindly input the charge for the food")
tipPercentage = 0.18
salesTaxPercentage = 0.07
tip = float(tipPercentage) * float(chargeForFood)
salesTax = float(salesTaxPercentage) * float(chargeForFood)
grandTotal = tip + salesTax + chargeForFood
print()
print()

print()
print()
print()

print()
print()
print()

print()
print()
print()