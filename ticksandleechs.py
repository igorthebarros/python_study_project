import sys
from datetime import datetime

f_name = input('Please, enter your first name: ')
l_name = input('Now, enter your last name: ')
print(f'Thank you, {f_name} {l_name}.')

b_date = input(f'Hey, {f_name}, do you want to see something cool? Enter your birth date(Y-M-D): ')
t_date = datetime.now()
delta = t_date - (datetime.strptime(b_date, '%Y-%m-%d'))
print(f'You have been alive for {delta.days} days!')

print('Have you checked if your Python version is updated? You are running the version: ')
print(sys.version)
