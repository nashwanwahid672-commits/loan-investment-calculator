"""Command-line interface for the finance calculator.

Examples:
    python main.py loan --amount 200000 --rate 5 --years 25
    python main.py loan --amount 200000 --rate 5 --years 25 --schedule
    python main.py invest --amount 1000 --rate 6 --years 20 --monthly 200
    python main.py invest --amount 1000 --rate 6 --years 20 --monthly 200 --plot
"""
import argparse

import finance


def money(value):
    return f"${value:,.2f}"


def run_loan(args):
    payment = finance.monthly_payment(args.amount, args.rate, args.years)
    interest = finance.total_interest(args.amount, args.rate, args.years)
    print(f"Monthly payment:  {money(payment)}")
    print(f"Total interest:   {money(interest)}")
    print(f"Total paid:       {money(args.amount + interest)}")
    if args.schedule:
        print(f"\n{'Month':>5} {'Payment':>12} {'Interest':>12} {'Principal':>12} {'Balance':>14}")
        for row in finance.amortization_schedule(args.amount, args.rate, args.years):
            print(f"{row['month']:>5} {money(row['payment']):>12} {money(row['interest']):>12} "
                  f"{money(row['principal']):>12} {money(row['balance']):>14}")


def run_invest(args):
    final = finance.future_value(args.amount, args.rate, args.years, args.monthly)
    contributed = args.amount + args.monthly * round(args.years * 12)
    print(f"Final balance:    {money(final)}")
    print(f"Total contributed: {money(contributed)}")
    print(f"Growth earned:    {money(final - contributed)}")
    if args.plot:
        plot_growth(args)


def plot_growth(args):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nInstall matplotlib to use --plot:  pip install matplotlib")
        return
    data = finance.growth_by_year(args.amount, args.rate, args.years, args.monthly)
    years = [y for y, _ in data]
    balances = [b for _, b in data]
    plt.plot(years, balances, marker="o")
    plt.title("Investment growth")
    plt.xlabel("Year")
    plt.ylabel("Balance ($)")
    plt.grid(True)
    plt.show()


def build_parser():
    parser = argparse.ArgumentParser(description="Loan and investment calculator")
    sub = parser.add_subparsers(dest="command", required=True)

    loan = sub.add_parser("loan", help="Calculate loan payments")
    loan.add_argument("--amount", type=float, required=True, help="loan amount")
    loan.add_argument("--rate", type=float, required=True, help="annual interest rate in %%")
    loan.add_argument("--years", type=float, required=True, help="loan term in years")
    loan.add_argument("--schedule", action="store_true", help="print full amortization schedule")
    loan.set_defaults(func=run_loan)

    invest = sub.add_parser("invest", help="Project investment growth")
    invest.add_argument("--amount", type=float, default=0.0, help="starting amount")
    invest.add_argument("--rate", type=float, required=True, help="expected annual return in %%")
    invest.add_argument("--years", type=float, required=True, help="years to invest")
    invest.add_argument("--monthly", type=float, default=0.0, help="monthly contribution")
    invest.add_argument("--plot", action="store_true", help="show a growth chart")
    invest.set_defaults(func=run_invest)
    return parser


def main():
    args = build_parser().parse_args()
    try:
        args.func(args)
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
