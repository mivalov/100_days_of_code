# Day 6: If-elif statements

print('Secure Login')
print(12 * '=')
username = input('What is your username? ')
password = input('What is your password? ')

if username == 'John' and password == 'Secre7Pass':
    print('Welcome, John! Have a nice day!')
elif username == 'Michelle' and password == '7qs25&3$[!-':
    print('Hi Michelle! You look fantastic today!')
elif username == 'Danny' and password == 'Dan49py':
    print('Hello Danny! How are you doing?')
elif username == 'Sarah' and password == '}D12&!s3%4L[':
    print('Hi Sarah! You look lovely today!')
else:
    print("Access denied!")
