'''
12. Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email

'''

def emailSlicer(email):
    print(email.find("@"))
    print(email.find("#"))
    if email.find("@") != -1:
        username = email[:email.index("@")]  # username value = from 0 to index < @
        domain = email[email.index("@") + 1:]  # domain value = from index > @ to end
        print("Your username is: ", username)
        print("Your domain is: ", domain)
    else:
        print("Please enter a valid Email Id.")




if __name__ == '__main__':
    email = input("enter your email").strip()
    emailSlicer(email)
