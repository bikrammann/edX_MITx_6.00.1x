def calculate_balance(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0
    remainingBalance = balance
    minimumMonthlyPayment = 0

    while True:
        minimumMonthlyPayment += 10

        for _ in range(0,12):
            monthlyUpaidBalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = round(monthlyUpaidBalance + (monthlyInterestRate * monthlyUpaidBalance),2)

        if remainingBalance < 0:
            break
        else:
            remainingBalance = balance

    print("Lowest Payment: {}".format(minimumMonthlyPayment))

calculate_balance(balance, annualInterestRate)