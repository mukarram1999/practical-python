# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
original_payment = 2684.11
total_paid = 0.00
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = original_payment + extra_payment 
    else:
        payment = original_payment

    month = month + 1
     
    principal = principal * (1 + rate / 12) - payment
    if principal < 0:
        principal = 0

    total_paid = total_paid + payment

    print(month - 1, round(payment, 2), round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Total months', month - 1)