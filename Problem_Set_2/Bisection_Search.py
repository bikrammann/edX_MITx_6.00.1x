def calculate_balance(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12
    upperBound = (balance * (1+ monthlyInterestRate)**12)/12
    minimumMonthlyPayment = (upperBound + lowerBound)/2.0

    while True:
        remainingBalance = balance

        for _ in range(0,12):
            monthlyUpaidBalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = round(monthlyUpaidBalance + (monthlyInterestRate * monthlyUpaidBalance),2)

        if remainingBalance <= 0 and remainingBalance >= -0.01:
            break
        else:
            if remainingBalance > 0:
                lowerBound = minimumMonthlyPayment
            else:
                upperBound = minimumMonthlyPayment
        minimumMonthlyPayment = (upperBound + lowerBound)/2.0

    print("Lowest Payment: {}".format(round(minimumMonthlyPayment,2)))

calculate_balance(balance, annualInterestRate)