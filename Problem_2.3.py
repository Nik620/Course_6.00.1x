# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:24:17 2020

@author: Nikola
"""


#pset2.3

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
        
adjustedPayment = round(minFixedPayment,2)
print("Lowest Payment:", adjustedPayment)