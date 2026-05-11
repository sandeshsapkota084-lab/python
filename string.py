a='ram'
b='kumar'
print(f'Hello, {a}!')
print(a)
print(f'my name is {2+3} {2*5}')
print('My name is {0} {1}'.format(a,b))
print('My name is {1} {0}'.format(a,b))
print('My name is {:s}'.format(a))
print('My name is {:10s}'.format(a))
print('My name is {:>10s}'.format(a))
print('My name is {x} {y}'.format(x='atharva',y='bhosale'))
name='hari'
print(f'Hello, {name.upper()}!')
print(f'Hello, {name.lower()}!')
print(f'Hello, {name.capitalize()}!')
print(f'Hello, {name.title()}!')
print(f'Hello, {name.center(20)}!')
print(f'Hello, {name.ljust(20)}!') #in case of odd number of characters in name, formula for left side=(n-1)/2 right side=(n+1)/2
print(f'Hello, {name.rjust(20)}!') #in case of even number of characters in name, formula for both sides=n/2
print(f'Hello, {name.zfill(20)}!') #fills with 0s on the left side
print(type(name))
f_name=['apple','banana','cherry']
print(f_name)
append='orange'