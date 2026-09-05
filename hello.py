#==============Hardcoded Values==============

# print('========================')
# print('Welcome here')
# print('My first post')
# print('========================')

# username = "cool_creator"
# bio = "Fun Blogger"
# Followers = 100

# Followers += 50
# print("Day 1:", Followers)

# Followers += 20
# print("Day 2:", Followers)

# Followers -= 10
# print("Day 3:", Followers)

# print('Username:', username)
# print('Bio:', bio)
# print('Followers:', Followers)

#==============Interactive Profile==============
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print('\nInstagram Profile')
print('========================')
print('Username:', username)
print('Age:', age)
print('Category:', category)

if age>40 and category == 'fun':
    print(' you are old what is fun for you??')
