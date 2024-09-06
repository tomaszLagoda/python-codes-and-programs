balance = 320000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def calculateBalanceAfterTimePeriod(balance, annualInterestRate, monthlyPaymentRate, num_months: int = 12):
    """ 
    Function will return outstanding balance of a credic card after x months

    balance, annualInterestRate, monthlyPaymentRate: positive floats or itegers
    num_months: positive integer

    returns: float 

    """
    interest_rate = annualInterestRate / 12

    for x in range(num_months):
        balance += balance * interest_rate
        balance -= balance * monthlyPaymentRate

    return round(balance, 2)

def calculateBalanceAfterTimePeriodFixed(balance, annualInterestRate, monthly_fixed_rate, num_months: int = 12):
    """ 
    Function will return outstanding balance of a credic card after x months deducting a fixed rate

    balance, annualInterestRate, monthlyPaymentRate: positive floats or itegers
    num_months: positive integer

    returns: float 

    """
    interest_rate = annualInterestRate / 12

    for x in range(num_months):
        balance -= monthly_fixed_rate
        balance += balance * interest_rate

    return round(balance, 2)

def calculateMinimumMonthlyPayment(balance, annualInterestRate, monthlyPaymentRate = 0, num_months: int = 12):
    """
    Function will return the minimum value that user will have to pay in order to clear out outstanding balance within x months

    balance, annualInterestRate: positive floats or itegers
    num_months: positive integer

    returns: string stating Lowest Payment: x
    """
    iterations = 1
    outstanding_balance = calculateBalanceAfterTimePeriodFixed(balance, annualInterestRate, monthlyPaymentRate, num_months)

    while outstanding_balance > 0:
        iterations += 1
        monthlyPaymentRate += 10
        outstanding_balance = calculateBalanceAfterTimePeriodFixed(balance, annualInterestRate, monthlyPaymentRate, num_months)        
    # print("Iterations (loop)", iterations)
    return monthlyPaymentRate

def calculateMinimumMonthlyPaymentBisectionSearch(balance, annualInterestRate, monthlyPaymentRate = 0, num_months: int = 12):
    """
    Function will return the minimum value that user will have to pay in order to clear out outstanding balance within x months

    balance, annualInterestRate: positive floats or itegers
    num_months: positive integer

    returns: string stating Lowest Payment: x
    """
    iterations = 0

    lower_payment_limit = balance / num_months
    upper_payment_limit = (balance * (1 + annualInterestRate)**num_months) / num_months

    monthy_pay_rate = lower_payment_limit
    outstanding_balance = balance

    while abs(outstanding_balance) > 0.01:
        iterations += 1

        # We are paying to much
        if outstanding_balance < 0.01:
            upper_payment_limit = monthy_pay_rate
        # We are paying not enough
        else:
            lower_payment_limit = monthy_pay_rate

        # Find middle point for bisection search
        monthy_pay_rate =  (lower_payment_limit + upper_payment_limit) / 2
        outstanding_balance = calculateBalanceAfterTimePeriodFixed(balance, annualInterestRate, monthy_pay_rate, num_months)

    # print("Iterations (bisection method)", iterations)
    return round(monthy_pay_rate, 2)


result = calculateMinimumMonthlyPayment(balance, annualInterestRate)
print("Lowest Payment (loop) : " + str(result))

result = calculateMinimumMonthlyPaymentBisectionSearch(balance, annualInterestRate)
print("Lowest Payment (bisection) : " + str(result))

