# Finance Calculator

A Python command-line tool for calculating loan payments, amortization schedules, and investment growth, with CSV export.

## Features

- **Loan calculator:** monthly payment, total interest, and total cost for a fixed-rate loan
- **Amortization schedule:** a month-by-month breakdown of interest, principal, and remaining balance
- **Investment projections:** compound growth with optional monthly contributions
- **CSV export:** save amortization schedules and yearly investment balances to a file
- **Growth chart:** optional matplotlib chart of investment growth over time
- **Input validation:** clear error messages for invalid values
- **Unit tests** with pytest

## Installation

Requires Python 3.8 or newer.

```
git clone https://github.com/nashwanwahid672-commits/finance-calculator.git
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

### Saving results to CSV

Add `--output` with a filename to either command:

```
python main.py loan --amount 10000 --rate 6 --years 1 --output schedule.csv
python main.py invest --amount 1000 --rate 6 --years 3 --monthly 200 --output growth.csv
```

The loan command saves one row per month:

```
month,payment,interest,principal,balance
1,860.66,50.0,810.66,9189.34
2,860.66,45.95,814.72,8374.62
```

The invest command saves one row per year:

```
year,balance
1,3528.79
2,6213.55
3,9063.9
```

The files open in Excel, Google Sheets, or any spreadsheet program.

### Options

| Command  | Option       | Description                                  |
|----------|--------------|----------------------------------------------|
| `loan`   | `--amount`   | Loan amount                                  |
| `loan`   | `--rate`     | Annual interest rate (%)
