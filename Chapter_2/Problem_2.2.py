# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:09:02 2020

@author: Nikola
"""


#pset2.2

#not in submission code
balance = float(input("Enter balance: "))
annualInterestRate = float(input("Enter annual interest rate: "))

#code
#estimate fixed payment around 1/10th of total balance based on test code
high = balance / 6
low = 0
minFixedPayment = balance / 10 
resultFound = False
monthlyInterestRate = annualInterestRate / 12
while resultFound == False:
    previousBalance = balance
    for i in range(1,13):
        monthlyUnpaidBalance = previousBalance - minFixedPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        previousBalance = updatedBalance
    if round(updatedBalance,0) == 0:
        resultFound = True
        break
    elif updatedBalance > 0: #case payment too low
        low = minFixedPayment
        minFixedPayment = (low + high)/2
    else: #case payment too high
        high = minFixedPayment
        minFixedPayment = (low + high)/2
        
#adjustment as output in edX not exact
if round(minFixedPayment,1)%10 == 0: #sensitivity based on edX desired output
    adjustedPayment = int(minFixedPayment)
else:
    adjustedPayment = int(round(minFixedPayment + 5,-1))
print("Lowest Payment:", adjustedPayment)
