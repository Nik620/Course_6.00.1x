# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:14:23 2020

@author: Nikola
"""

#Pset 2 Credit Card Debt
#import math

#not in submission code
balance = float(input("Enter balance: "))
annualInterestRate = float(input("Enter annual interest rate: "))
monthlyPaymentRate = float(input("Enter monthly payment rate: "))

#code
previousBalance = balance
monthlyInterestRate = annualInterestRate / 12


for i in range(1,13):
    minMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    #temporary to check
    #print('Month',i,"Remaining balance:",round(updatedBalance,2))
    previousBalance = updatedBalance

#desired output
print("Remaining balance:",round(updatedBalance,2))




