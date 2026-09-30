# Finance Calculator

A Python command-line tool for calculating loan payments, amortization schedules, and investment growth.

## Features

- **Loan calculator:** monthly payment, total interest, and total cost for a fixed-rate loan
- **Amortization schedule:** a month-by-month breakdown of interest, principal, and remaining balance
- **Investment projections:** compound growth with optional monthly contributions
- **Growth chart:** optional matplotlib chart of investment growth over time
- **Input validation:** clear error messages for invalid values
- **Unit tests** with pytest

## Installation

Requires Python 3.8 or newer.

```
git clone https://github.com/YOUR-USERNAME/finance-calculator.git
cd finance-calculator
pip install -r requirements.txt
```

## Usage

### Loan payments

```
python main.py loan --amount 200000 --rate 5 --years 25
```

```
Monthly payment:  $1,169.18
Total interest:   $150,754.02
Total paid:       $350,754.02
```

Add `--schedule` to print the full amortization schedule.

### Investment growth

```
python main.py invest --amount 1000 --rate 6 --years 20 --monthly 200
```

```
Final balance:    $95,718.38
Total contributed: $49,000.00
Growth earned:    $46,718.38
```

Add `--plot` to show a growth chart (requires matplotlib).

### Options

| Command  | Option       | Description                          |
|----------|--------------|--------------------------------------|
| `loan`   | `--amount`   | Loan amount                          |
| `loan`   | `--rate`     | Annual interest rate (%)             |
| `loan`   | `--years`    | Loan term in years                   |
| `loan`   | `--schedule` | Print the amortization schedule      |
| `invest` | `--amount`   | Starting amount (default 0)          |
| `invest` | `--rate`     | Expected annual return (%)           |
| `invest` | `--years`    | Years to invest                      |
| `invest` | `--monthly`  | Monthly contribution (default 0)     |
| `invest` | `--plot`     | Show a growth chart                  |

Run `python main.py --help` for the full list.

## How it works

The monthly loan payment uses the standard amortization formula:

```
payment = P * r / (1 - (1 + r) ** -n)
```

where `P` is the loan amount, `r` is the monthly interest rate (annual rate / 12), and `n` is the total number of monthly payments.

Investment growth uses monthly compounding with contributions made at the end of each month:

```
FV = P * (1 + r) ** n + C * ((1 + r) ** n - 1) / r
```

where `C` is the monthly contribution.

## Project structure

```
finance-calculator/
├── finance.py        # core calculations (no input or output)
├── main.py           # command-line interface
├── requirements.txt
└── tests/
    └── test_finance.py
```

## Running the tests

```
pytest
```

## Limitations

- Interest compounds monthly. Canadian fixed-rate mortgages typically compound semi-annually, so results will differ slightly from a bank's calculator.
- Assumes a fixed interest rate and fixed payments.
- Does not account for taxes, fees, or inflation.
- Investment projections are illustrative only and are not financial advice.
