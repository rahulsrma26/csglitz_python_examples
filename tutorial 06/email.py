email = 'bruce.wayne@wayne.org'
username, domain = email.split('@')
firstname = username.split('.')[0]
company, _ = domain.rsplit('.')

print(f'Welcome {firstname.title()}')
print(f'Username: {username}')
print(f' Company: {company}')
print(f'  Domain: {domain}')
