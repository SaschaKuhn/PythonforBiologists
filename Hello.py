import os

username = os.environ.get('USER', os.environ.get('USERNAME'))

print(f'Welcome {username}!')
print('Thanks for doing your pre-course homework. You are now all set.')
print('See you Tuesday,')
print('Cheers!')