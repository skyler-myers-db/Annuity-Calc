import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()

if args.payment:
    if int(args.payment) < 0:
        print("Incorrect parameters")
        sys.exit()

if args.type not in ['annuity', 'diff'] or not args.type:
    print("Incorrect parameters")
    sys.exit()

if args.type == 'diff' and args.payment:
    print("Incorrect parameters")
    sys.exit()

if len(sys.argv) - 1 < 4:
    print("Incorrect parameters")
    sys.exit()

if args.principal and args.periods:
    if int(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0:
        print("Incorrect parameters")
        sys.exit()

if args.type == 'diff':
    P = int(args.principal)
    n = int(args.periods)
    i = float(args.interest) / (12 * 100)
    month = 1
    total = 0
    for m in range(1, n + 1):
        diff = math.ceil(P / n + i * (P - (P * (m - 1)) / n))
        print(f"Month {month}: payment is {diff}")
        month += 1
        total += diff

    print(f"\nOverpayment = {total - P}")

if args.type == 'annuity' and not args.payment:
    P = int(args.principal)
    n = int(args.periods)
    i = float(args.interest) / (12 * 100)
    annuity = math.ceil(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    over = math.ceil(annuity * n - P)
    print(f"Your annuity payment = {annuity}!")
    print(f"\nOverpayment = {over}")

if args.type == 'annuity' and not args.principal:
    n = int(args.periods)
    i = float(args.interest) / (12 * 100)
    p = float(args.payment)
    P = math.floor(p / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    over = math.ceil(p * n - P)
    print(f"your loan principal = {P}!")
    print(f"Overpayment = {over}")

if args.type == 'annuity' and not args.periods:
    i = float(args.interest) / (12 * 100)
    P = int(args.principal)
    p = float(args.payment)
    n = math.ceil(math.log(p / (p - i * P), 1 + i))
    years = n // 12
    months = n % 12
    over = math.ceil(p * n - P)
    if n > 1 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif n <= 1 and months == 0:
        print(f"It will take {years} year to repay this loan!")
    elif n > 1 and months > 1:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif n > 1 and months <= 1:
        print(f"It will take {years} years and {months} month to repay this loan!")
    elif n <= 1 and months > 1:
        print(f"It will take {years} year and {months} month to repay this loan!")
    elif n <= 1 and months <= 1:
        print(f"It will take {years} year and {months} month to repay this loan!")
    print(f"Overpayment = {over}")


print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
calc = input()

if calc == 'n':
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the monthly payment:")
    payment = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    nominal = interest / 1200
    months = math.ceil(math.log(payment / (payment - nominal * principal), 1 + nominal))
    years = months // 12
    months = months % 12
    print(f"It will take {years} years and {months} months to repay this loan!")

elif calc == 'a':
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the number of periods:")
    periods = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    nominal = interest / 1200
    annuity = principal * ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1))
    print(f"Your monthly payment = {math.ceil(annuity)}!")

elif calc == 'p':
    print("Enter the annuity payment:")
    annuity = float(input())
    print("Enter the number of periods:")
    periods = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    nominal = interest / 1200
    principal = annuity / ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1))
    print(f"Your loan principal = {math.floor(principal)}!")

#if args.type == 'diff':

