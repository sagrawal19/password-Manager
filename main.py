import random
import string
#password manager
#input the information that we want to save

password_list = []
def new_password():
    website = input('What is the Website? ')
    username = input('What is the username? ')
    password = input('What is the password? ')
    if password == 'random' :
        num_of_digits = int(input('How many character long should the password be? '))
        random_password = ''.join(random.choice(string.ascii_letters +string.digits) for _ in range(num_of_digits))
        print(f'This is the random password: {random_password}')
        password = random_password
    else:
        pass

    website_entry = dict([("website", website),("username", username),("password", password)])
    password_list.append(website_entry)
    print (password_list)


def find_password():
    looked_for_website = input('what website is it for? ')
    for entry in password_list:
       found_website= entry.get('website')
       if found_website == looked_for_website:
          print(entry.password)
       else:
          print("Website doesn't exit")



while True:
    print('''
    Welcome to the password manager ya dingus.
    Type "new" to create a new password.
    Type "show" to look up a password.
    ''')

    user_choice = input('Whatcha wanna do?')
    if user_choice == 'new':
        pass
    elif user_choice == 'show':
        find_password
    else:
        print("Hwat?? That didn't compute ")
    
# print(website)
# print(username)
# print(password)

