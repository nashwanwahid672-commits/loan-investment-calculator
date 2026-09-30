"""Core financial calculations: loan payments, amortization, and investment growth."""


def _validate(principal, annual_rate, years):
    """raise value error if inputs are invalid"""
    if principal <= 0:
        raise ValueError("principal must be greater than 0")
    if annual_rate < 0:
        raise ValueError("annual_rate cannot be negative")
    if years <= 0:
        raise ValueError("years must be greater than 0")


def monthly_payment(principal, annual_rate, years):
    """Return the fixed monthly payment for a loan.

    annual_rate is a percentage, e.g. 5 for 5%.
    Formula: P * r / (1 - (1 + r) ** -n), where r is the monthly rate
    and n is the number of monthly payments.
    """
    _validate(principal, annual_rate, years)
    n = round(years * 12)
    r = annual_rate / 100 / 12
    if r == 0:
        return principal / n
    return principal * r / (1 - (1 + r) ** -n)


def amortization_schedule(principal, annual_rate, years):
    """Return a list of dicts, one per month, describing each payment."""
    payment = monthly_payment(principal, annual_rate, years)
    n = round(years * 12)
    r = annual_rate / 100 / 12
    balance = principal
    schedule = []
    for month in range(1, n + 1):
        interest = balance * r
        principal_paid = payment - interest
        balance -= principal_paid
        if month == n:  # clear tiny floating point leftovers
            balance = 0.0
        schedule.append({
            "month": month,
            "payment": payment,
            "interest": interest,
            "principal": principal_paid,
            "balance": max(balance, 0.0),
        })
    return schedule


def total_interest(principal, annual_rate, years):
    """Total interest paid over the life of the loan."""
    payment = monthly_payment(principal, annual_rate, years)
    return payment * round(years * 12) - principal


def future_value(principal, annual_rate, years, monthly_contribution=0.0):
    """Return the value of an investment after `years`, compounded monthly.

    Contributions are made at the end of each month.
    Formula: P * (1 + r)**n + C * ((1 + r)**n - 1) / r
    """
    if principal < 0 or monthly_contribution < 0:
        raise ValueError("principal and monthly_contribution cannot be negative")
    if annual_rate < 0:
        raise ValueError("annual_rate cannot be negative")
    if years <= 0:
        raise ValueError("years must be greater than 0")
    n = round(years * 12)
    r = annual_rate / 100 / 12
    if r == 0:
        return principal + monthly_contribution * n
    growth = (1 + r) ** n
    return principal * growth + monthly_contribution * (growth - 1) / r


def growth_by_year(principal, annual_rate, years, monthly_contribution=0.0):
    """Return a list of (year, balance) pairs, handy for printing or charting."""
    return [
        (year, future_value(principal, annual_rate, year, monthly_contribution))
        for year in range(0, int(years) + 1)
        if year > 0
    ]
