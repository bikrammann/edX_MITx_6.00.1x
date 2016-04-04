def calculate_balance(balance, annualInterestRate, monthlyPaymentRate):

    totalPaid = 0
    remainingBalance = balance

    for month in range(1,13):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = round((monthlyPaymentRate * remainingBalance),2)
        totalPaid += minimumMonthlyPayment
        monthlyUpaidBalance = remainingBalance - minimumMonthlyPayment
        remainingBalance = round(monthlyUpaidBalance + (monthlyInterestRate * monthlyUpaidBalance),2)

        print("Month: {}".format(month))
        print("Minimum monthly payment: {}".format(minimumMonthlyPayment))
        print("Remaining Balance: {}".format(remainingBalance))

    print("Total paid: {}".format(totalPaid))
    print("Remaining Balance: {}".format(remainingBalance))



calculate_balance(balance, annualInterestRate, monthlyPaymentRate)
