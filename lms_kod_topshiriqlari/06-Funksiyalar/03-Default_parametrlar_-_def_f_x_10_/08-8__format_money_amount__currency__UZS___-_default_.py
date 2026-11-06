def format_money(amount, currency = 'UZS'):
   return f'{amount} {currency}'
print(format_money(*input().split()))